import pb2 as _pb2
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()
import asyncio

class MatchState:
    Idle = 0
    PreMatch = 1
    WaitForStartOfMatch = 2
    Match = 3
    PostMatch = 4
    
class RobotCommands:
    def __init__(self, robot):
        self._robot = robot
        
class RobotMain:
    def sequence(self, func):
        self._sequences[func.__name__] = func
        
    def snapGirouette(self):
        self.girouette = self._last_girouette
        print(self.girouette)
        
    def __init__(self):
        config_path = f'config/test/'
        config = _pb2.get_symbol('goldo.nucleo.robot.Config')()
        config.ParseFromString(open(config_path + 'robot_config.bin', 'rb').read())
        self._config_proto = config   
        self.side = 0        
        self.commands = RobotCommands(self)
        self._sequences = {}
        self._match_state = MatchState.Idle
        self._current_task = None
        self._last_girouette = None
        self.girouette = None
        
    async def configNucleo(self, msg):
        buff = self._config_proto.data
        await self._broker.publishTopic('nucleo/in/robot/config/load_begin', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadBegin')(size=len(buff)))
        #Upload codes by packets        
        while len(buff) > 0:
            await self._broker.publishTopic('nucleo/in/robot/config/load_chunk', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadChunk')(data=buff[0:32]))
            buff = buff[32:]
        #Finish programming
        await self._broker.publishTopic('nucleo/in/robot/config/load_end', _sym_db.GetSymbol('goldo.nucleo.robot.ConfigLoadEnd')(crc=self._config_proto.crc))        
    
    async def onConfigStatus(self, msg):
        await self._broker.publishTopic('gui/in/nucleo_config_status', msg)
        
    async def onNucleoReset(self, msg):
        await self._broker.publishTopic('gui/in/nucleo_reset', msg)         
        
    async def onPreMatch(self, msg):
        print("prematch side = {}".format({0: 'unset', 1: 'blue', 2:'yellow'}[self.side]))
        await self._broker.publishTopic('nucleo/in/match/timer/start')
        
        self._match_state = MatchState.PreMatch
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state))
        asyncio.create_task(self._prematchSequence())
        
    async def _prematchSequence(self):
        await self._sequences['prematch']()
        self._match_state = MatchState.WaitForStartOfMatch
        await self._broker.publishTopic('gui/in/match_state', _sym_db.GetSymbol('google.protobuf.Int32Value')(value=self._match_state))
        
    async def onCameraDetections(self, msg):
        for d in msg.detections:
            if d.tag_id == 17:
                # south up
                if d.uy > 0:
                    self._last_girouette = 's'
                else:
                    self._last_girouette = 'n'
        
    def _setBroker(self, broker):
        self._broker = broker
        broker.registerCallback('gui/out/side', self.onSetSide)
        broker.registerCallback('gui/out/commands/config_nucleo', self.configNucleo)
        broker.registerCallback('gui/out/commands/prematch', self.onPreMatch)
        broker.registerCallback('nucleo/out/robot/config/load_status', self.onConfigStatus)
        broker.registerCallback('nucleo/out/os/reset', self.onNucleoReset)
        broker.registerCallback('camera/out/detections', self.onCameraDetections)
    
    async def test(self):
        self._fut = asyncio.Future()
        await self._fut
        print('finished')
        
    async def onSetSide(self, msg):
        self.side = msg.value
        print(msg)
        
robot = RobotMain()
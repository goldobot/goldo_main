from enum import Enum, IntEnum

import logging

LOGGER = logging.getLogger(__name__)

class CurrentActionState(IntEnum):
    Idle = 0
    # in prepare_sequence
    Prepare = 1
    # ready
    PrepareFinished = 2
    # in prepare_cancel_sequence
    PrepareCancel = 3
    # sequence
    Sequence = 4

class Action(object):
    def __init__(self, name, proto):
        self.name = name
        self.enabled = False
        self._proto = proto
        print(proto)
        # action start pose, x, y, yaw
        self.start_pose = (0,0,0)
        self.priority = 0
        # sequence to start once arrived at action location
        #self.sequence = proto.sequence
        # sequence launched when starting to travel towards action location
        self.prepare_sequence = None
        # sequence launched after prepare_sequence if the action is cancelled 
        # due to another robot moving in for exemple
        self.prepare_cancel_sequence = None
        
class StrategyEngine(object):
    def __init__(self, robot):
        self._robot = robot
        self._actions = []
        self._current_action = None
        self._current_action_state = CurrentActionState.Idle
        self._current_sequence = None
        
    def loadConfig(self):
        config_proto = self._robot._config_proto.strategy
        for k, v in config_proto.actions.items():
            self._actions.append(Action(k, v))
            
        
    @property
    def robot_state(self):
        return self._robot._state_proto
        
    async def run(self):
        await self.runSequence('start_match')
        
    async def runSequence(self, name):   
        LOGGER.debug('start sequence %s', name)
        try:
            await self._robot._sequences[name]()
        except Exception as e:
            LOGGER.exception('exception in sequence %s', name)
            raise e
            
        LOGGER.debug('finish sequence %s', name)
        
        
    
        
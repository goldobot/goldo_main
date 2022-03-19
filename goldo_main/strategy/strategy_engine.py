from enum import Enum, IntEnum
import astar
import asyncio
import logging
import math
import pb2 as _pb2
from goldo_main.enums import *
import google.protobuf as _pb
_sym_db = _pb.symbol_database.Default()


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
        self.priority = proto.default_priority
        self.start_pose = (self._proto.start_pose.position.x, self._proto.start_pose.position.y, self._proto.start_pose.yaw * math.pi/180)
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
        self._actions_by_name = {}
        self._running = False
        self._timer_callbacks = []
        self._tasks = {}
        self._astar = astar.AStarWrapper()

       
        

    async def try_astar(self):
        #return
        self._astar.resetCosts()
        #self._astar.fillRect(35,0,125, 55)
        if self._robot.side == Side.Blue or True:
            #port
            #self._astar.fillRect(200-55,90,200, 150)
            #adversary start area
            #self._astar.fillRect(35,300-55,125, 300)
            #self._astar.fillRect(0,300-55,35, 300)
            #self._astar.fillRect(125,300-55,165, 300)
            pass
            
        self._astar.setDisk((1.7,-0.3), 30)

        msg = _sym_db.GetSymbol('google.protobuf.BytesValue')(value=self._astar.getArr())

        await self._robot._broker.publishTopic('strategy/debug/astar_arr', msg)
        print(self._astar.computePath((1.8, -1.3), (1.8, 1.3)))
        
    async def display_astar(self):
        msg = _sym_db.GetSymbol('google.protobuf.BytesValue')(value=self._astar.getArr())
        await self._robot._broker.publishTopic('strategy/debug/astar_arr', msg)

    @property
    def actions(self):
        return self._actions_by_name
        
    def addTimerCallback(self, timer, callback):
        self._timer_callbacks.append((timer, callback))            
        
    def loadConfig(self):
        config_proto = self._robot._config_proto.strategy
        self._actions = []
        for k, v in config_proto.actions.items():
            self._actions.append(Action(k, v))
        self._actions_by_name = {a.name: a for a in self._actions}
            
        
    @property
    def robot_state(self):
        return self._robot._state_proto
        
    async def run(self):
        self._running = True
        try:
            await self.runSequence('start_match')
        except asyncio.CancelledError:
            raise
        except Exception:
            LOGGER.exception('error in start_match sequence')
        print('finish start match')
            
        while self._running:            
            action, path = self._selectNextAction()
            if action is not None:
                
                LOGGER.debug('selected action: %s', action.name)
            await asyncio.sleep(1)
            
    async def runSequence(self, name):   
        LOGGER.debug('start sequence %s', name)
        try:
            await self._robot._sequences[name]()
        except Exception:
            LOGGER.exception('exception in sequence %s', name)
            raise
        LOGGER.debug('finish sequence %s', name)
        
    def _onMatchTimer(self, value):
        l = []
        for timer, callback in self._timer_callbacks:
            if value <= timer:
                task = asyncio.create_task(callback())
                self._tasks[id(task)] = task
            else:            
                l.append((timer, callback))
        self._timer_callbacks = l
        
    def _selectNextAction(self):
        self._actions.sort(key=lambda a: -a.priority)
        ok = False
        for action in self._actions:
            if action.enabled:
                ok, path, cost = self._computePathForAction(action)
                if ok:
                    return action, path
        return None, None

                
    
        
    def _computePathForAction(self, action):
        current_pose = self.robot_state.robot_pose
        current_pose = (current_pose.position.x, current_pose.position.y, current_pose.yaw)
        return True, [(current_pose[0], current_pose[1]), (action.start_pose[0], action.start_pose[1])], 10
       
        
    
        
        
    
        

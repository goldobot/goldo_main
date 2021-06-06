from enum import Enum, IntEnum

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
    def __init__(self):
        self.name = ''
        self.enabled = False
        # action start pose, x, y, yaw
        self.pose = (0,0,0)
        self.priority = 0
        # sequence to start once arrived at action location
        self.sequence = None
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
        
    async def run(self):
        await self.runSequence('start_match')
        
    async def runSequence(self, name):
        print('start sequence,' name)
        
    
        
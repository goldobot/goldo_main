from enum import Enum

class MatchState(Enum):
    Idle = 0
    PreMatch = 1
    WaitForStartOfMatch = 2
    Match = 3
    MatchFinished = 4
    
__all = [MatchState]
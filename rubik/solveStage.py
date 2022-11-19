
from enum import Enum, unique

@unique
class SolveStage(Enum):
    """ Represents one of the stages in the process to solve a cube """
    
    # these ordered stages comprise the overall algorithm to solve any cube
    DOWN_CROSS = 1
    DOWN_LAYER = 2
    DOWN_AND_MIDDLE_LAYERS = 3
    DOWN_MID_LAYERS_AND_UP_FACE = 4
    ENTIRE_CUBE = 5

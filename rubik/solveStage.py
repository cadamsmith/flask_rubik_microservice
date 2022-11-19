
from enum import Enum, unique

@unique
class SolveStage(Enum):
    """ Represents one of the stages in the process to solve a cube """
    
    # these ordered stages comprise the overall algorithm to solve any cube
    UP_DAISY = 1
    DOWN_CROSS = 2
    DOWN_LAYER = 3
    DOWN_AND_MIDDLE_LAYERS = 4
    DOWN_MID_LAYERS_AND_UP_CROSS = 5
    DOWN_MID_LAYERS_AND_UP_FACE = 6

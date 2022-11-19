
from enum import Enum, unique

@unique
class SolveStage(Enum):
    """ Represents one of the stages in the process to solve a cube """
    
    # these 5 stages are in order in the algorithm to solve the cube
    UP_DAISY = 1
    DOWN_CROSS = 2
    DOWN_LAYER_SOLVED = 3
    DOWN_AND_MIDDLE_LAYERS_SOLVED = 4
    DOWN_MID_LAYERS_AND_UP_CROSS = 5

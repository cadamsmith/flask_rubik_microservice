
from enum import Enum, unique

@unique
class CubeState(Enum):
    """ Represents a way to "solve" a cube """
    
    UP_DAISY = 1
    DOWN_CROSS = 2
    DOWN_LAYER_SOLVED = 3

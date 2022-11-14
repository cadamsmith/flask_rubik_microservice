
from enum import Enum, unique

@unique
class FaceCubeletPosition(Enum):
    """ Represents the position of one of the cubelets on a 3x3x3 cube """
    
    UP_LEFT = 'UL'
    UP = 'U'
    UP_RIGHT = 'UR'
    LEFT = 'L'
    CENTER = 'C'
    RIGHT = 'R'
    DOWN_LEFT = 'DL'
    DOWN = 'D'
    DOWN_RIGHT = 'DR'

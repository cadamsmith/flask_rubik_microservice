
from enum import Enum, unique

@unique
class CubeRotationDirection(Enum):
    """ Represents a way to rotate a single cube """
    
    FLIP_FORWARD = 'FF'
    FLIP_BACKWARD = 'FB'
    FLIP_LEFTWARD = 'FL'
    FLIP_RIGHTWARD = 'FR'
    SPIN_LEFTWARD = 'SL'
    SPIN_RIGHTWARD = 'SR'


from enum import Enum, unique

@unique
class CubeRotationDirection(Enum):
    FORWARD = 'F'
    BACKWARD = 'B'
    LEFTWARD = 'L'
    RIGHTWARD = 'R'

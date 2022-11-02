
from enum import Enum, unique

@unique
class CubeFacePosition(Enum):
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'

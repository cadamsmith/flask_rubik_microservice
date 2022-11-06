
from enum import Enum, unique

@unique
class CubeFacePosition(Enum):
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'
    
    @classmethod
    def hasValue(cls, value):
        return value in cls._value2member_map_ 


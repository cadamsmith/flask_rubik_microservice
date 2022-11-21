
from enum import Enum, unique

@unique
class CubeColor(Enum):
    """ represents one of the colors on the outside of the cube """
    
    BLUE = 'b'
    RED = 'r'
    GREEN = 'g'
    ORANGE = 'o'
    YELLOW = 'y'
    WHITE = 'w'

    @classmethod
    def hasValue(cls, value):
        """ determines whether a value is a valid color code """
        
        return value in cls._value2member_map_
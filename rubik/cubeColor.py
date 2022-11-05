
from enum import Enum, unique

@unique
class CubeColor(Enum):
    BLUE = 'b'
    RED = 'r'
    GREEN = 'g'
    ORANGE = 'o'
    YELLOW = 'y'
    WHITE = 'w'
    NONE = '#'
    
    @staticmethod
    def getFaceColors():
        return [
            CubeColor.BLUE,
            CubeColor.RED,
            CubeColor.GREEN,
            CubeColor.ORANGE,
            CubeColor.YELLOW,
            CubeColor.WHITE
        ]

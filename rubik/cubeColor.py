
from enum import Enum, unique

@unique
class CubeColor(Enum):
    '''represents one of the colors on the outside of the cube'''
    
    BLUE = 'b'
    RED = 'r'
    GREEN = 'g'
    ORANGE = 'o'
    YELLOW = 'y'
    WHITE = 'w'
    
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

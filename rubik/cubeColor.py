
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
    
    def getFaceColors(self):
        return [
            self.BLUE,
            self.RED,
            self.GREEN,
            self.ORANGE,
            self.YELLOW,
            self.WHITE
        ]

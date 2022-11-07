
from enum import Enum, unique

@unique
class FaceRotationDirection(Enum):
    '''Represents a way to rotate an outer cube face'''
    
    CLOCKWISE = 'CW'
    COUNTERCLOCKWISE = 'CCW'

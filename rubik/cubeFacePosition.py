
from enum import Enum, unique

from rubik.cubeRotationDirection import CubeRotationDirection

@unique
class CubeFacePosition(Enum):
    """ Represents the position of one of a cube's outer faces """
    
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'
    
    @classmethod
    def hasValue(cls, value):
        return value in cls._value2member_map_
    
    @classmethod
    def rotate(cls, facePosition, direction: CubeRotationDirection):
        """ returns the new face position if the cube were rotated """
        
        assert (isinstance(direction, CubeRotationDirection))
        
        if direction is CubeRotationDirection.FLIP_FORWARD:
            return cls._flipForward(facePosition)
        
        elif direction is CubeRotationDirection.FLIP_BACKWARD:
            return cls._flipBackward(facePosition)
        
        elif direction is CubeRotationDirection.FLIP_LEFTWARD:
            return cls._flipLeftward(facePosition)
        
        elif direction is CubeRotationDirection.FLIP_RIGHTWARD:
            return cls._flipRightward(facePosition)
        
        elif direction is CubeRotationDirection.SPIN_LEFTWARD:
            return cls._spinLeftward(facePosition)
        
        elif direction is CubeRotationDirection.SPIN_RIGHTWARD:
            return cls._spinRightward(facePosition)
    
    @classmethod
    def _flipForward(cls, facePosition):
        """ returns the new face position if it were flipped forward """
        
        transform = {
            cls.UP: cls.FRONT,
            cls.FRONT: cls.DOWN,
            cls.DOWN: cls.BACK,
            cls.BACK: cls.UP
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]
    
    @classmethod
    def _flipBackward(cls, facePosition):
        """ returns the new face position if it were flipped backward """
        
        transform = {
            cls.UP: cls.BACK,
            cls.BACK: cls.DOWN,
            cls.DOWN: cls.FRONT,
            cls.FRONT: cls.UP
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]
    
    @classmethod
    def _flipLeftward(cls, facePosition):
        """ returns the new face position if it were flipped leftward """
        
        transform = {
            cls.UP: cls.LEFT,
            cls.LEFT: cls.DOWN,
            cls.DOWN: cls.RIGHT,
            cls.RIGHT: cls.UP
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]
    
    @classmethod
    def _flipRightward(cls, facePosition):
        """ returns the new face position if it were flipped rightward """
        
        transform = {
            cls.UP: cls.RIGHT,
            cls.RIGHT: cls.DOWN,
            cls.DOWN: cls.LEFT,
            cls.LEFT: cls.UP
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]
    
    @classmethod
    def _spinLeftward(cls, facePosition):
        """ returns the new face position if it were spun leftward """
        
        transform = {
            cls.FRONT: cls.LEFT,
            cls.LEFT: cls.BACK,
            cls.BACK: cls.RIGHT,
            cls.RIGHT: cls.FRONT
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]
    
    @classmethod
    def _spinRightward(cls, facePosition):
        """ returns the new face position if it were spun rightward """
        
        transform = {
            cls.FRONT: cls.RIGHT,
            cls.RIGHT: cls.BACK,
            cls.BACK: cls.LEFT,
            cls.LEFT: cls.FRONT
        }
        
        # face position unchanged if not in transform domain
        if facePosition not in transform.keys():
            return facePosition
        
        # otherwise transform it
        return transform[facePosition]


from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeColor import CubeColor
from rubik.cubeRotationDirection import CubeRotationDirection

class Cubelet:
    """ Represents one of the smaller cubes that make up a Rubik's Cube """

    def __init__(self, coloredFaces = {}):
        """ instantiate Cubelet from info about its face colors """
        
        # make sure coloredFaces is dict<K, V> where:
        # - keys K are of type CubeFacePosition
        # - values V are of type CubeColor
        assert (isinstance(coloredFaces, dict))
        assert (all(isinstance(face, CubeFacePosition) for face in coloredFaces.keys()))
        assert (all(isinstance(color, CubeColor) for color in coloredFaces.values()))
        
        # make sure that no more than 3 cubelet faces are colored
        assert (len(coloredFaces) <= 3)
        
        # initialize all cubeData to no color
        self.faces = {cf: None for cf in CubeFacePosition}
        
        self.faces.update(coloredFaces)
        
    def setFaceColor(self, facePosition: CubeFacePosition, color: CubeColor):
        """ colors one of the cubelet's faces """
        
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(color, CubeColor))
        
        self.faces[facePosition] = color
    
    def rotate(self, direction: CubeRotationDirection):
        """ rotates the cubelet in some direction """
        
        # make sure direction is a CubeRotationDirection
        assert (isinstance(direction, CubeRotationDirection))
        
        if direction is CubeRotationDirection.FLIP_FORWARD:
            self.__flipForward__()
        elif direction is CubeRotationDirection.FLIP_BACKWARD:
            self.__flipBackward__()
        elif direction is CubeRotationDirection.FLIP_LEFTWARD:
            self.__flipLeftward__()
        elif direction is CubeRotationDirection.FLIP_RIGHTWARD:
            self.__flipRightward__()
        elif direction is CubeRotationDirection.SPIN_LEFTWARD:
            self.__spinLeftward__()
        elif direction is CubeRotationDirection.SPIN_RIGHTWARD:
            self.__spinRightward__()
    
    def __flipForward__(self):
        """ flips the cubelet forward """
        
        alteredFaces = {
            CubeFacePosition.UP: self.faces[CubeFacePosition.BACK],
            CubeFacePosition.BACK: self.faces[CubeFacePosition.DOWN],
            CubeFacePosition.DOWN: self.faces[CubeFacePosition.FRONT],
            CubeFacePosition.FRONT: self.faces[CubeFacePosition.UP]
        }
        
        self.faces.update(alteredFaces)
        
    def __flipBackward__(self):
        """ flips the cubelet backward """
        
        alteredFaces = {
            CubeFacePosition.UP: self.faces[CubeFacePosition.FRONT],
            CubeFacePosition.FRONT: self.faces[CubeFacePosition.DOWN],
            CubeFacePosition.DOWN: self.faces[CubeFacePosition.BACK],
            CubeFacePosition.BACK: self.faces[CubeFacePosition.UP]
        }
        
        self.faces.update(alteredFaces)
        
    def __flipLeftward__(self):
        """ flips the cubelet leftward """
        
        alteredFaces = {
            CubeFacePosition.UP: self.faces[CubeFacePosition.RIGHT],
            CubeFacePosition.RIGHT: self.faces[CubeFacePosition.DOWN],
            CubeFacePosition.DOWN: self.faces[CubeFacePosition.LEFT],
            CubeFacePosition.LEFT: self.faces[CubeFacePosition.UP]
        }
        
        self.faces.update(alteredFaces)
        
    def __flipRightward__(self):
        """ flips the cubelet rightward """
        
        alteredFaces = {
            CubeFacePosition.UP: self.faces[CubeFacePosition.LEFT],
            CubeFacePosition.LEFT: self.faces[CubeFacePosition.DOWN],
            CubeFacePosition.DOWN: self.faces[CubeFacePosition.RIGHT],
            CubeFacePosition.RIGHT: self.faces[CubeFacePosition.UP]
        }
        
        self.faces.update(alteredFaces)
        
    def __spinLeftward__(self):
        """ spins the cubelet leftward """
        
        alteredFaces = {
            CubeFacePosition.FRONT: self.faces[CubeFacePosition.RIGHT],
            CubeFacePosition.RIGHT: self.faces[CubeFacePosition.BACK],
            CubeFacePosition.BACK: self.faces[CubeFacePosition.LEFT],
            CubeFacePosition.LEFT: self.faces[CubeFacePosition.FRONT]
        }
        
        self.faces.update(alteredFaces)
        
    def __spinRightward__(self):
        """ spins the cubelet rightward """
        
        alteredFaces = {
            CubeFacePosition.FRONT: self.faces[CubeFacePosition.LEFT],
            CubeFacePosition.LEFT: self.faces[CubeFacePosition.BACK],
            CubeFacePosition.BACK: self.faces[CubeFacePosition.RIGHT],
            CubeFacePosition.RIGHT: self.faces[CubeFacePosition.FRONT]
        }
        
        self.faces.update(alteredFaces)
        


from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeColor import CubeColor
from rubik.cubeRotationDirection import CubeRotationDirection

class Cubelet:

    def __init__(self, faces = {}):
        
        # initialize all faces to no color
        self.faces = {cf: None for cf in CubeFacePosition}
        
        # make sure that no more than 3 cubelet faces are colored
        assert (len(faces) <= 3)
        
        # make sure that the param faces is a dictionary with CubeFacePosition keys and CubeColor values
        assert (all(isinstance(face, CubeFacePosition) for face in faces.keys()))
        assert (all(isinstance(color, CubeColor) for color in faces.values()))
        
        self.faces.update(faces)
        
    def rotate(self, direction):
        
        # make sure direction is a CubeRotationDirection
        assert (isinstance(direction, CubeRotationDirection))
        
        if direction is CubeRotationDirection.FORWARD:
            self.__rotateForward__()
        elif direction is CubeRotationDirection.BACKWARD:
            self.__rotateBackward__()
        elif direction is CubeRotationDirection.LEFTWARD:
            self.__rotateLeftward__()
        elif direction is CubeRotationDirection.RIGHTWARD:
            self.__rotateRightward__()
        
    def __rotateForward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.FRONT]
        self.faces[CubeFacePosition.FRONT] = temp
        
    def __rotateBackward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.FRONT]
        self.faces[CubeFacePosition.FRONT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = temp
        
    def __rotateLeftward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = temp
        
    def __rotateRightward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = temp
        

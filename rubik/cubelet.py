
from rubik.cubeFace import CubeFace
from rubik.cubeColor import CubeColor
from rubik.cubeRotationDirection import CubeRotationDirection

class Cubelet:

    def __init__(self, faces = {}):
        
        # initialize all faces to no color
        self.faces = {cf: None for cf in CubeFace}
        
        # make sure that no more than 3 cubelet faces are colored
        assert (len(faces) <= 3)
        
        # make sure that the param faces is a dictionary with CubeFace keys and CubeColor values
        assert (all(isinstance(face, CubeFace) for face in faces.keys()))
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
        
        temp = self.faces[CubeFace.FRONT]
        
        self.faces[CubeFace.FRONT] = self.faces[CubeFace.UP]
        self.faces[CubeFace.UP] = self.faces[CubeFace.BACK]
        self.faces[CubeFace.BACK] = self.faces[CubeFace.DOWN]
        self.faces[CubeFace.DOWN] = temp
        
    def __rotateBackward__(self):
        
        temp = self.faces[CubeFace.FRONT]
        
        self.faces[CubeFace.FRONT] = self.faces[CubeFace.DOWN]
        self.faces[CubeFace.DOWN] = self.faces[CubeFace.BACK]
        self.faces[CubeFace.BACK] = self.faces[CubeFace.UP]
        self.faces[CubeFace.UP] = temp
        
    def __rotateLeftward__(self):
        
        temp = self.faces[CubeFace.UP]
        
        self.faces[CubeFace.UP] = self.faces[CubeFace.RIGHT]
        self.faces[CubeFace.RIGHT] = self.faces[CubeFace.DOWN]
        self.faces[CubeFace.DOWN] = self.faces[CubeFace.LEFT]
        self.faces[CubeFace.LEFT] = temp
        
    def __rotateRightward__(self):
        
        temp = self.faces[CubeFace.UP]
        
        self.faces[CubeFace.UP] = self.faces[CubeFace.LEFT]
        self.faces[CubeFace.LEFT] = self.faces[CubeFace.DOWN]
        self.faces[CubeFace.DOWN] = self.faces[CubeFace.RIGHT]
        self.faces[CubeFace.RIGHT] = temp
        


from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeColor import CubeColor
from rubik.cubeRotationDirection import CubeRotationDirection

class Cubelet:

    def __init__(self, cubeData = {}):
        
        # initialize all cubeData to no color
        self.faces = {cf: None for cf in CubeFacePosition}
        
        # make sure that no more than 3 cubelet cubeData are colored
        assert (len(cubeData) <= 3)
        
        # make sure that the param cubeData is a dictionary with CubeFacePosition keys and CubeColor values
        assert (all(isinstance(face, CubeFacePosition) for face in cubeData.keys()))
        assert (all(isinstance(color, CubeColor) for color in cubeData.values()))
        
        self.faces.update(cubeData)
        
    def setFaceColor(self, facePosition, color):
        # make sure that the facePosition is a FacePosition and color is a CubeColor
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(color, CubeColor))
        
        self.faces[facePosition] = color
        
    def rotate(self, direction):
        
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
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.FRONT]
        self.faces[CubeFacePosition.FRONT] = temp
        
    def __flipBackward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.FRONT]
        self.faces[CubeFacePosition.FRONT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = temp
        
    def __flipLeftward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = temp
        
    def __flipRightward__(self):
        
        temp = self.faces[CubeFacePosition.UP]
        
        self.faces[CubeFacePosition.UP] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = self.faces[CubeFacePosition.DOWN]
        self.faces[CubeFacePosition.DOWN] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = temp
        
    def __spinLeftward__(self):
        
        temp = self.faces[CubeFacePosition.FRONT]
        
        self.faces[CubeFacePosition.FRONT] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = temp
        
    def __spinRightward__(self):
        
        temp = self.faces[CubeFacePosition.FRONT]
        
        self.faces[CubeFacePosition.FRONT] = self.faces[CubeFacePosition.LEFT]
        self.faces[CubeFacePosition.LEFT] = self.faces[CubeFacePosition.BACK]
        self.faces[CubeFacePosition.BACK] = self.faces[CubeFacePosition.RIGHT]
        self.faces[CubeFacePosition.RIGHT] = temp
        


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
        
        self.__rotateForward__()
        
        
        
    def __rotateForward__(self):
        
        temp = self.faces[CubeFace.FRONT]
        
        self.faces[CubeFace.FRONT] = self.faces[CubeFace.UP]
        self.faces[CubeFace.UP] = self.faces[CubeFace.BACK]
        self.faces[CubeFace.BACK] = self.faces[CubeFace.DOWN]
        self.faces[CubeFace.DOWN] = temp
        
        print(self.faces)
        

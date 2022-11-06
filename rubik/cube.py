
import itertools
from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeRotationDirection import CubeRotationDirection

class Cube:
    '''
    Rubik's cube
    '''
    
    cubelets = {}
    
    FRONT_FACE_CUBELET_COORDS = [
        (0, 0, 0), (1, 0, 0), (2, 0, 0),
        (0, 1, 0), (1, 1, 0), (2, 1, 0),
        (0, 2, 0), (1, 2, 0), (2, 2, 0)
    ]
    
    BACK_FACE_CUBELET_COORDS = [
        (0, 0, 2), (1, 0, 2), (2, 0, 2),
        (0, 1, 2), (1, 1, 2), (2, 1, 2),
        (0, 2, 2), (1, 2, 2), (2, 2, 2)
    ]
    
    LEFT_FACE_CUBELET_COORDS = [
        (0, 0, 0), (0, 1, 0), (0, 2, 0),
        (0, 0, 1), (0, 1, 1), (0, 2, 1),
        (0, 0, 2), (0, 1, 2), (0, 2, 2)
    ]
    
    RIGHT_FACE_CUBELET_COORDS = [
        (2, 0, 0), (2, 1, 0), (2, 2, 0),
        (2, 0, 1), (2, 1, 1), (2, 2, 1),
        (2, 0, 2), (2, 1, 2), (2, 2, 2)
    ]
    
    UP_FACE_CUBELET_COORDS = [
        (0, 0, 0), (1, 0, 0), (2, 0, 0),
        (0, 0, 1), (1, 0, 1), (2, 0, 1),
        (0, 0, 2), (1, 0, 2), (2, 0, 2)
    ]
    
    DOWN_FACE_CUBELET_COORDS = [
        (0, 2, 0), (1, 2, 0), (2, 2, 0),
        (0, 2, 1), (1, 2, 1), (2, 2, 1),
        (0, 2, 2), (1, 2, 2), (2, 2, 2)
    ]
    
    FACE_CENTER_CUBELET_COORDS = [(1, 1, 0), (1, 1, 2), (0, 1, 1), (2, 1, 1), (1, 0, 1), (1, 2, 1)]

    def __init__(self, cubeCode):
        # make sure supplied param is a valid CubeCode
        assert (isinstance(cubeCode, CubeCode))
 
        self.size = cubeCode.CUBE_WIDTH
        self.faceArea = cubeCode.CUBE_WIDTH ** 2
               
        for i, j, k in itertools.product(*[range(cubeCode.CUBE_WIDTH)] * 3):
            self.cubelets[i, j, k] = Cubelet()
        
        codeIndex = 0
        for facePosition in cubeCode.FACE_POSITION_ORDER:
            for coords in cubeCode.FACE_COORD_MAPPINGS[facePosition]:
                color = CubeColor(cubeCode.text[codeIndex])
                self.cubelets[coords].setFaceColor(facePosition, color)
                
                codeIndex += 1
                
    def rotateFace(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
        
        if facePosition is CubeFacePosition.FRONT:
            self.__rotateFrontFace(direction)
        elif facePosition is CubeFacePosition.BACK:
            self.__rotateBackFace(direction)
        elif facePosition is CubeFacePosition.LEFT:
            self.__rotateLeftFace(direction)
        elif facePosition is CubeFacePosition.RIGHT:
            self.__rotateRightFace(direction)
        elif facePosition is CubeFacePosition.UP:
            self.__rotateUpFace(direction)
        elif facePosition is CubeFacePosition.DOWN:
            self.__rotateDownFace(direction)
        
        
    def __rotateFrontFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (2 - y, x, z)
            cubeletRotationDirection = CubeRotationDirection.FLIP_RIGHTWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.FRONT_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
        
    def __rotateBackFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (y, 2 - x, z)
            cubeletRotationDirection = CubeRotationDirection.FLIP_LEFTWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.BACK_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
        
    def __rotateLeftFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (x, 2 - z, y)
            cubeletRotationDirection = CubeRotationDirection.FLIP_FORWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.LEFT_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
        
    def __rotateRightFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (x, z, 2 - y)
            cubeletRotationDirection = CubeRotationDirection.FLIP_BACKWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.RIGHT_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
        
    def __rotateUpFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (2 - z, y, x)
            cubeletRotationDirection = CubeRotationDirection.SPIN_LEFTWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.UP_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
        
    def __rotateDownFace(self, direction: FaceRotationDirection):
        # make sure supplied params are the right types
        assert (isinstance(direction, FaceRotationDirection))
        
        coordTransform = cubeletRotationDirection = None
        
        if direction is FaceRotationDirection.CLOCKWISE:
            coordTransform = lambda x, y, z : (z, y, 2 - x)
            cubeletRotationDirection = CubeRotationDirection.SPIN_RIGHTWARD
        
        alteredCubelets = {}
        
        if direction is FaceRotationDirection.CLOCKWISE:
            for (x, y, z) in self.DOWN_FACE_CUBELET_COORDS:
                newCoord = coordTransform(x, y, z)
                
                alteredCubelets[newCoord] = self.cubelets[x, y, z]
                alteredCubelets[newCoord].rotate(cubeletRotationDirection)
        
        self.cubelets.update(alteredCubelets)
                
    def toCode(self):
        
        codeText = ''
        
        for facePosition in CubeCode.FACE_POSITION_ORDER:
            for coords in CubeCode.FACE_COORD_MAPPINGS[facePosition]:
                color = self.cubelets[coords].faces[facePosition]
                codeText += '#' if color is None else color.value
                
        return CubeCode(codeText)            
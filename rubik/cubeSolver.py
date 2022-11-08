
from rubik.cube import Cube
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolver():
    
    def __init__(self, cube: Cube):
        assert (isinstance(cube, Cube))
        
        self.cube = cube
        
    def solve(self):
        
        directions = []
        
        directions = self.__transformFromUpDaisyToBottomCross(directions)
        
        return directions
    
    def __transformFromUpDaisyToBottomCross(self, directions):
        
        # front face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.FRONT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.FRONT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.FRONT]:
            
            direction = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(direction)
            directions.push(direction)
            
        # left face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.LEFT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.LEFT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.LEFT]:
            
            direction = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(direction)
            directions.push(direction)
        
        # back face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.BACK]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.BACK]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.BACK]:
            
            direction = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(direction)
            directions.push(direction)
        
        # right face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.RIGHT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.RIGHT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.RIGHT]:
            
            direction = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(direction)
            directions.push(direction)
        
        return directions
        
        

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
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.push((rotationFace, rotationDirection))
            
        # left face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.LEFT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.LEFT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.LEFT]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.push((rotationFace, rotationDirection))
        
        # back face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.BACK]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.BACK]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.BACK]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.push((rotationFace, rotationDirection))
        
        # right face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.RIGHT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.RIGHT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.RIGHT]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.push((rotationFace, rotationDirection))
        
        return directions
        
        
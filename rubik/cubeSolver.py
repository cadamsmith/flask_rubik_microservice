
from rubik.cube import Cube
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolver():
    
    def __init__(self, cube: Cube):
        assert (isinstance(cube, Cube))
        
        self.cube = cube
        
    def solve(self):
        
        directions = []
        
        directions = self.__transformFromUpDaisyToDownCross(directions)
        
        return directions
    
    def __hasDownCross(self):
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        downColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.DOWN]
        
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        for coord in petalCoords:
            color = self.cube.cubelets[coord].faces[CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
            
        otherFacesToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        for facePosition in otherFacesToCheck:
            
            (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[facePosition]
            faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[facePosition]
            
            belowColor = self.cube.cubelets[centerX, centerY + 1, centerZ].faces[facePosition]
            
            if faceColor != belowColor:
                return False
        
        return True
        
        
    
    def __transformFromUpDaisyToDownCross(self, directions):
        if self.__hasDownCross():
            return directions
        
        # front face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.FRONT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.FRONT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.FRONT]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, FaceRotationDirection.CLOCKWISE)
            directions.append((rotationFace, rotationDirection))
            
        self.cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE))
        
        self.cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE))
            
        # left face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.LEFT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.LEFT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.LEFT]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.append((rotationFace, rotationDirection))
            
        self.cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE))
        
        self.cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE))
        
        # back face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.BACK]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.BACK]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.BACK]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.append((rotationFace, rotationDirection))
            
        self.cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE))
        
        self.cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE))
        
        # right face
        
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.RIGHT]
        aboveCenterCoord = (centerX, centerY - 1, centerZ)
        
        faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.RIGHT]
        
        while faceColor != self.cube.cubelets[aboveCenterCoord].faces[CubeFacePosition.RIGHT]:
            
            (rotationFace, rotationDirection) = (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            self.cube.rotateFace(rotationFace, rotationDirection)
            directions.append((rotationFace, rotationDirection))
            
        self.cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE))
        
        self.cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        directions.append((CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE))
        
        return directions
        
        
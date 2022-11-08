
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
        
        directions = self.__optimizeDirections(directions)
        
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
        
        flippedPetalCount = 0
        
        i = 0
        facePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # we are trying to get above color == below color
        # then we flip the petal
        
        # start with front face
        (aboveX, aboveY, aboveZ) = (1, 0, 0)
        (belowX, belowY, belowZ) = (1, 1, 0)
        facePosition = facePositions[i]
        
        # we need to flip all four daisy petals
        while (flippedPetalCount < 4):
            
            aboveColor = self.cube.cubelets[(aboveX, aboveY, aboveZ)].faces[facePosition]
            belowColor = self.cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
            
            while aboveColor != belowColor:
                self.cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                directions.append((CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE))
                
                (aboveX, aboveY, aboveZ) = self.cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
                
                i = (i + 1) % 4
                facePosition = facePositions[i]
                
                aboveColor = self.cube.cubelets[(aboveX, aboveY, aboveZ)].faces[facePosition]
                belowColor = self.cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
                
            self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
            directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
            
            self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
            directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
            
            flippedPetalCount += 1
            
            (aboveX, aboveY, aboveZ) = self.cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
            
            i = (i + 1) % 4
            facePosition = facePositions[i]
            
        return directions
    
    def __optimizeDirections(self, directions):
        
        if len(directions) < 2:
            return directions
        
        (lastFace, lastDirection) = directions[0]
        repeatCount = 1
        
        for (face, direction) in directions[1:]:
            
            # rotating a face clockwise then counterclockwise, or vice versa
            if lastFace == face and lastDirection != direction:
                # accomplishes nothing, remove these
                directions = directions[:-2]
                continue
            
            if lastFace == face and lastDirection == direction:
                repeatCount += 1
            else:
                repeatCount = 1
            
            if repeatCount == 3:
                replacementDirection = (
                    FaceRotationDirection.CLOCKWISE
                    if lastDirection is FaceRotationDirection.COUNTERCLOCKWISE
                    else FaceRotationDirection.COUNTERCLOCKWISE
                )
                
                directions = directions[:3]
                directions.append((face, replacementDirection))
                
            
            (lastFace, lastDirection) = (face, direction)
            
        return directions
        

from rubik.cube import Cube
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolver():
    """ An entity capable of determining directions for solving 3x3x3 Rubik's Cube """
    
    """ list of directions to solve the cube """
    directions = []
    
    def __init__(self, cube: Cube):
        """ instantiates a CubeSolver, supplied only a Cube """
        
        assert (isinstance(cube, Cube))
        
        self.cube = cube
        
    def solve(self):
        """ produces a list of rotation directions to solve the cube """
        
        self.directions = []
        
        # if it already has a down cross, we're done
        if self._hasDownCross():
            return
        
        # make up daisy on cube
        self.__transformToUpDaisy()
        
        # if it doesn't have an up daisy now, we've got a problem
        assert (self._hasUpDaisy())
        
        # make down cross
        self.__transformFromUpDaisyToDownCross()
        
        # optimize directions, replacing redundant rotations
        self.__optimizeDirections()
    
    def _hasUpDaisy(self):
        """ determines whether the cube has a daisy centered on the up face """
        
        # center coordinate of up face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.UP]
        # center coordinate of down face
        downCenterCoord = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, i.e. the colors of the daisy petals
        downColor = self.cube.cubelets[downCenterCoord].faces[CubeFacePosition.DOWN]
        
        # coordinates of each petal cubelet
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether the up face color is the cube's down color
            color = self.cube.cubelets[coord].faces[CubeFacePosition.UP]
            
            if color != downColor:
                return False
            
        return True
    
    def _hasDownCross(self):
        """ determines whether the cube has a cross centered on the down face """
        
        # center coordinate of down face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, i.e. the color of the plus sign of down cross
        downColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.DOWN]
        
        # coordinates of each petal cubelet around the cross
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether its down face color is the cube's down color
            color = self.cube.cubelets[coord].faces[CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check a pair of cubelet faces on all vertical side face positions of the Rubiks cube
        otherFacesToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # go thru each face position
        for facePosition in otherFacesToCheck:
            
            # pair to check is center cubelet and cubelet below it
            (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[facePosition]
            (belowX, belowY, belowZ) = (centerX, centerY + 1, centerZ)
            
            # determine whether their color is the same
            faceColor = self.cube.cubelets[(centerX, centerY, centerZ)].faces[facePosition]
            belowColor = self.cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
            
            if faceColor != belowColor:
                return False
        
        return True
    
    def __transformToUpDaisy(self):
        """ makes a daisy centered on the up face of the cube """
        
        if self._hasUpDaisy():
            return
        
        downCenterCoord = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        downColor = self.cube.cubelets[downCenterCoord].faces[CubeFacePosition.DOWN]
        
        topEdgeCoords = [(1, 0, 0), (0, 0, 1), (1, 0, 2), (2, 0, 1)]
        middleEdgeCoords = [(2, 1, 0), (0, 1, 0), (0, 1, 2), (2, 1, 2)]
        bottomEdgeCoords = [(1, 2, 0), (0, 2, 1), (1, 2, 2), (2, 2, 1)]
        
        verticalFacePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        index = 0
        
        while not self.__hasUpDaisy():
            petalCoord = topEdgeCoords[index % 4]
            
            leftEdgeCoord = middleEdgeCoords[(index + 1) % 4]
            downEdgeCoord = bottomEdgeCoords[index % 4]
            rightEdgeCoord = middleEdgeCoords[index % 4]
            
            facePosition = verticalFacePositions[index % 4]
            relativeLeftFacePosition = verticalFacePositions[(index + 1) % 4]
            relativeRightFacePosition = verticalFacePositions[(index - 1) % 4]
            
            edgeCandidateColors = [
                self.cube.cubelets[leftEdgeCoord].faces[relativeLeftFacePosition],
                self.cube.cubelets[downEdgeCoord].faces[CubeFacePosition.DOWN],
                self.cube.cubelets[rightEdgeCoord].faces[relativeRightFacePosition]
            ]
            
            petalColor = self.cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
            
            while downColor in edgeCandidateColors:
                
                while petalColor == downColor:
                    self.cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    self.directions.append((CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE))
                    
                    petalColor = self.cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                    
                while petalColor != downColor:
                    self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
                    self.directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
                    
                    petalColor = self.cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                    
                edgeCandidateColors = [
                    self.cube.cubelets[leftEdgeCoord].faces[relativeLeftFacePosition],
                    self.cube.cubelets[downEdgeCoord].faces[CubeFacePosition.DOWN],
                    self.cube.cubelets[rightEdgeCoord].faces[relativeRightFacePosition]
                ]
                
            faceCandidateCoords = [ leftEdgeCoord, downEdgeCoord, rightEdgeCoord ]
            if petalColor != downColor:
                faceCandidateCoords.append(petalCoord)
            
            faceCandidateColors = list(map(
                lambda coord : self.cube.cubelets[coord].faces[facePosition],
                faceCandidateCoords
            ))
            
            if downColor in faceCandidateColors and faceCandidateColors[0] != downColor:
                
                while petalColor == downColor:
                    self.cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    self.directions.append((CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE))
                    
                    petalColor = self.cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                
                while faceCandidateColors[0] != downColor:
                    self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
                    self.directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
                    
                    faceCandidateColors = list(map(
                        lambda coord : self.cube.cubelets[coord].faces[facePosition],
                        faceCandidateCoords
                    ))
                    
            index += 1
    
    def __transformFromUpDaisyToDownCross(self):
        """ makes a down cross for the cube if it already has an up daisy """
        
        if self._hasDownCross():
            return
        
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
                self.directions.append((CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE))
                
                (aboveX, aboveY, aboveZ) = self.cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
                
                i = (i + 1) % 4
                facePosition = facePositions[i]
                
                aboveColor = self.cube.cubelets[(aboveX, aboveY, aboveZ)].faces[facePosition]
                belowColor = self.cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
                
            self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
            self.directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
            
            self.cube.rotateFace(facePosition, FaceRotationDirection.CLOCKWISE)
            self.directions.append((facePosition, FaceRotationDirection.CLOCKWISE))
            
            flippedPetalCount += 1
            
            (aboveX, aboveY, aboveZ) = self.cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
            
            i = (i + 1) % 4
            facePosition = facePositions[i]
    
    def __optimizeDirections(self):
        """ takes a list of directions and optimizes them, removing redundancy """
        
        if len(self.directions) < 2:
            return
        
        newDirections = []
        
        (lastFace, lastDirection) = self.directions[0]
        newDirections.append(self.directions[0])
        
        repeatCount = 1
        
        for (face, direction) in self.directions[1:]:
            
            # rotating a face clockwise then counterclockwise, or vice versa
            if lastFace == face and lastDirection != direction:
                # accomplishes nothing, remove these
                newDirections = newDirections[:-1]
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
                
                newDirections = newDirections[:-2]
                newDirections.append((face, replacementDirection))
                
            else:
                newDirections.append((face, direction))
            
            (lastFace, lastDirection) = (face, direction)
            
        self.directions = newDirections
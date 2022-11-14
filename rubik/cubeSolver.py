
from rubik.cube import Cube
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeState import CubeState

class CubeSolver():
    """ An entity capable of determining a solution for solving 3x3x3 Rubik's Cube """
    
    def __init__(self, cube: str | CubeCode | Cube):
        """ instantiates a CubeSolver, supplied only a Cube """
        
        # if param is a string, turn it into a CubeCode
        if isinstance(cube, str):
            cube = CubeCode(cube)
        
        # if param is a CubeCode, turn it into a Cube
        if isinstance(cube, CubeCode):
            cube = Cube(cube)
        
        assert isinstance(cube, Cube)
        
        self._solution = []
        self._cube = cube
        
    def solve(self, state: CubeState = CubeState.DOWN_CROSS):
        """ produces a list of rotation directions to reach a certain cube state """
        
        assert isinstance(state, CubeState)
        
        # directions are not retained from previous solves
        self._clearSolution()
        
        if state is CubeState.UP_DAISY:
            self._constructUpDaisy()
            
        elif state is CubeState.DOWN_CROSS:
            self._constructDownCross()
            
        elif state is CubeState.DOWN_LAYER_SOLVED:
            self._solveDownLayer()
        
        # optimize directions, replacing redundant rotations
        self._optimizeSolution()
        
    def _addToSolution(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """ executes cube rotation and adds it to the solve directions """
        
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
        
        self._cube.rotateFace(facePosition, direction)
        self.directions.add((facePosition, direction))
        
    def getDirections(self):
        """ accessor for _solution field """
        
        return self._solution
    
    def _hasUpDaisy(self):
        """ determines whether the cube has a daisy centered on the up face """
        
        # center coordinate of up face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.UP]
        # center coordinate of down face
        downCenterCoord = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, i.e. the colors of the daisy petals
        downColor = self._cube.cubelets[downCenterCoord].faces[CubeFacePosition.DOWN]
        
        # coordinates of each petal cubelet
        petalCoords = [
            (centerX - 1, centerY, centerZ),
            (centerX, centerY, centerZ - 1),
            (centerX + 1, centerY, centerZ),
            (centerX, centerY, centerZ + 1)
        ]
        
        # check all petal cubelet coords
        for coord in petalCoords:
            
            # determine whether the up face color is the _cube's down color
            color = self._cube.cubelets[coord].faces[CubeFacePosition.UP]
            
            if color != downColor:
                return False
            
        return True
    
    def _hasDownCross(self):
        """ determines whether the cube has a cross centered on the down face """
        
        # center coordinate of down face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, i.e. the color of the plus sign of down cross
        downColor = self._cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.DOWN]
        
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
            color = self._cube.cubelets[coord].faces[CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check a pair of cubelet faces on all vertical side face positions of the cube
        otherFacesToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # go thru each face position
        for facePosition in otherFacesToCheck:
            
            # pair to check is center cubelet and cubelet below it
            (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[facePosition]
            (belowX, belowY, belowZ) = (centerX, centerY + 1, centerZ)
            
            # determine whether their color is the same
            faceColor = self._cube.cubelets[(centerX, centerY, centerZ)].faces[facePosition]
            belowColor = self._cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
            
            if faceColor != belowColor:
                return False
        
        return True
    
    def _isDownLayerSolved(self):
        """ determines whether the cube's down layer is solved """
        
        # center coordinate of down face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        
        # down color, i.e. the color of the plus sign of down cross
        downColor = self._cube.cubelets[(centerX, centerY, centerZ)].faces[CubeFacePosition.DOWN]
        
        # check all colors on down face
        for coord in self._cube.CUBELET_COORDS[CubeFacePosition.DOWN]:
             
            # determine whether each is the right color
            color = self._cube.cubelets[coord].faces[CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check more colors on each of the 4 vertical side face positions of the cube
        otherFacePositionsToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # check that the center cubelet faces and lower cubelet faces are the same color
        lowerCoords = [(0, 2, 0), (1, 2, 0), (2, 2, 0)]
        
        for facePosition in otherFacePositionsToCheck:
            
            # center color
            centerCoord = self._cube.FACE_CENTER_CUBELET_COORDS[facePosition]
            faceColor = self._cube.cubelets[centerCoord].faces[facePosition]
            
            # determine whether all 3 lower colors are the same
            lowerColors = list(map(lambda coord : self._cube.cubelets[coord].faces[facePosition], lowerCoords))
            
            if any(color != faceColor for color in lowerColors):
                return False
            
            # get next 3 lower coords
            lowerCoords = list(map(
                lambda coord : self._cube.rotateCoord(coord, CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE),
                lowerCoords
            ))
        
        return True
    
    def _constructUpDaisy(self):
        """ makes an up daisy on the cube """
        
        # if cube already has an up daisy, we're done
        if self._hasUpDaisy():
            return
        
        downCenterCoord = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.DOWN]
        downColor = self._cube.cubelets[downCenterCoord].faces[CubeFacePosition.DOWN]
        
        topEdgeCoords = [(1, 0, 0), (0, 0, 1), (1, 0, 2), (2, 0, 1)]
        middleEdgeCoords = [(2, 1, 0), (0, 1, 0), (0, 1, 2), (2, 1, 2)]
        bottomEdgeCoords = [(1, 2, 0), (0, 2, 1), (1, 2, 2), (2, 2, 1)]
        
        verticalFacePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        index = 0
        
        while not self._hasUpDaisy():
            petalCoord = topEdgeCoords[index % 4]
            
            leftEdgeCoord = middleEdgeCoords[(index + 1) % 4]
            downEdgeCoord = bottomEdgeCoords[index % 4]
            rightEdgeCoord = middleEdgeCoords[index % 4]
            
            facePosition = verticalFacePositions[index % 4]
            relativeLeftFacePosition = verticalFacePositions[(index + 1) % 4]
            relativeRightFacePosition = verticalFacePositions[(index - 1) % 4]
            
            edgeCandidateColors = [
                self._cube.cubelets[leftEdgeCoord].faces[relativeLeftFacePosition],
                self._cube.cubelets[downEdgeCoord].faces[CubeFacePosition.DOWN],
                self._cube.cubelets[rightEdgeCoord].faces[relativeRightFacePosition]
            ]
            
            petalColor = self._cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
            
            while downColor in edgeCandidateColors:
                
                while petalColor == downColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    
                    petalColor = self._cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                    
                while petalColor != downColor:
                    self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
                    
                    petalColor = self._cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                    
                edgeCandidateColors = [
                    self._cube.cubelets[leftEdgeCoord].faces[relativeLeftFacePosition],
                    self._cube.cubelets[downEdgeCoord].faces[CubeFacePosition.DOWN],
                    self._cube.cubelets[rightEdgeCoord].faces[relativeRightFacePosition]
                ]
                
            faceCandidateCoords = [ leftEdgeCoord, downEdgeCoord, rightEdgeCoord ]
            if petalColor != downColor:
                faceCandidateCoords.append(petalCoord)
            
            faceCandidateColors = list(map(
                lambda coord : self._cube.cubelets[coord].faces[facePosition],
                faceCandidateCoords
            ))
            
            if downColor in faceCandidateColors and faceCandidateColors[0] != downColor:
                
                while petalColor == downColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    
                    petalColor = self._cube.cubelets[petalCoord].faces[CubeFacePosition.UP]
                
                while faceCandidateColors[0] != downColor:
                    self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
                    
                    faceCandidateColors = list(map(
                        lambda coord : self._cube.cubelets[coord].faces[facePosition],
                        faceCandidateCoords
                    ))
                    
            index += 1
    
    def _constructDownCross(self):
        """ makes a down cross on the cube """
        
        # if cube already has a down cross, we're done
        if self._hasDownCross():
            return
        
        # have to construct up daisy first
        self._constructUpDaisy()
        
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
            
            aboveColor = self._cube.cubelets[(aboveX, aboveY, aboveZ)].faces[facePosition]
            belowColor = self._cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
            
            while aboveColor != belowColor:
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                
                (aboveX, aboveY, aboveZ) = self._cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
                
                i = (i + 1) % 4
                facePosition = facePositions[i]
                
                aboveColor = self._cube.cubelets[(aboveX, aboveY, aboveZ)].faces[facePosition]
                belowColor = self._cube.cubelets[(belowX, belowY, belowZ)].faces[facePosition]
                
            self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
            self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
            
            flippedPetalCount += 1
            
            (aboveX, aboveY, aboveZ) = self._cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
            
            i = (i + 1) % 4
            facePosition = facePositions[i]
            
    def _solveDownLayer(self):
        """ solves down layer of cube """
        
        # if down layer already solved, we're done
        if self._isDownLayerSolved():
            return
        
        # have to construct down cross first
        self._constructDownCross()
    
    def _optimizeSolution(self):
        """ optimizes solution, removing redundancy """
        
        if len(self._solution) < 2:
            return
        
        optimizedSolution = []
        
        (lastFace, lastDirection) = self._solution[0]
        optimizedSolution.append(self._solution[0])
        
        repeatCount = 1
        
        for (face, direction) in self._solution[1:]:
            
            # rotating a face clockwise then counterclockwise, or vice versa
            if lastFace == face and lastDirection != direction:
                # accomplishes nothing, remove these
                optimizedSolution = optimizedSolution[:-1]
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
                
                optimizedSolution = optimizedSolution[:-2]
                optimizedSolution.append((face, replacementDirection))
                
            else:
                optimizedSolution.append((face, direction))
            
            (lastFace, lastDirection) = (face, direction)
            
        self._solution = optimizedSolution
    
    def _clearSolution(self):
        """ resets solution """
        
        self._solution.clear()

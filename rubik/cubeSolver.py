
from rubik.cube import Cube
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeState import CubeState
from rubik.faceCubeletPosition import FaceCubeletPosition
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeSolver():
    """ An entity capable of determining a solution for solving a 3x3x3 Rubik's Cube """
    
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
        
    def solve(self, state: CubeState = CubeState.DOWN_LAYER_SOLVED):
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
        self._solution.append((facePosition, direction))
        
    def getSolution(self):
        """ accessor for _solution field """
        
        return self._solution
    
    def _hasUpDaisy(self):
        """ determines whether the cube has a daisy centered on the up face """
        
        # center coordinate of up face
        (centerX, centerY, centerZ) = Cube.FACE_CENTER_CUBELET_COORDS[CubeFacePosition.UP]
        
        # down color, also the colors the daisy petals should be
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
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
        
        # down color, also the color that the plus sign of the down cross should be
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
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
        
        # down color, also the color that every tile on down face should be
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # check all colors on down face
        for coord in self._cube.CUBELET_COORDS[CubeFacePosition.DOWN]:
             
            # determine whether each is the right color
            color = self._cube.cubelets[coord].faces[CubeFacePosition.DOWN]
            
            if color != downColor:
                return False
        
        # need to check more colors on each of the 4 vertical side face positions of the cube
        otherFacePositionsToCheck = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # check that the center tile and lower 3 tiles are the same color on each face
        lowerCoords = [(0, 2, 0), (1, 2, 0), (2, 2, 0)]
        
        for facePosition in otherFacePositionsToCheck:
            
            # center color
            faceColor = self._cube.getFaceColor(facePosition)
            
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
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
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
        assert self._hasUpDaisy()
        
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
        assert self._hasDownCross()
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # these are all of the places where the down corner pieces may show up
        
        upperLeftCandidateCoords = {
            facePosition: self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            for facePosition in self._cube.VERTICAL_FACE_CORNER_COORDS
        }
        
        upperRightCandidateCoords = {
            facePosition: self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT]
            for facePosition in self._cube.VERTICAL_FACE_CORNER_COORDS
        }
        
        lowerLeftCandidateCoords = {
            facePosition: self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
            for facePosition in self._cube.VERTICAL_FACE_CORNER_COORDS
        }
        
        lowerRightCandidateCoords = {
            facePosition: self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.DOWN_RIGHT]
            for facePosition in self._cube.VERTICAL_FACE_CORNER_COORDS
        }
        
        while not self._isDownLayerSolved():
            
            # first look for the down color in the upper left tile of all the side faces
            
            upperLeftCandidateColors = {
                facePosition: self._cube.cubelets[coord].faces[facePosition]
                for (facePosition, coord) in upperLeftCandidateCoords.items()
            }
            
            if any(color == downColor for (_, color) in upperLeftCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in upperLeftCandidateColors.items() 
                    if color == downColor
                )
                
                self._handleMatchedUpperLeftCandidateColor(facePosition)
                continue
            
            # now look for the down color in the upper right tile of all the side faces
            
            upperRightCandidateColors = {
                facePosition: self._cube.cubelets[coord].faces[facePosition]
                for (facePosition, coord) in upperRightCandidateCoords.items()
            }
            
            if any(color == downColor for (_, color) in upperRightCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in upperRightCandidateColors.items() 
                    if color == downColor
                )
                
                self._handleMatchedUpperRightCandidateColor(facePosition)
                continue
            
            # now look for the down color in all of the corner tiles of the top face
            
            topCornerCandidateColors = {
                facePosition: self._cube.cubelets[coord].faces[CubeFacePosition.UP]
                for (facePosition, coord) in upperLeftCandidateCoords.items()
            }
            
            if any(color == downColor for (_, color) in topCornerCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in topCornerCandidateColors.items() 
                    if color == downColor
                )
                
                self._handleMatchedTopCornerCandidateColor(facePosition)
                continue
            
            # now look for the down color in the lower left tile of all the side faces
            
            lowerLeftCandidateColors = {
                facePosition: self._cube.cubelets[coord].faces[facePosition]
                for (facePosition, coord) in lowerLeftCandidateCoords.items()
            }
            
            if any(color == downColor for (_, color) in lowerLeftCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in lowerLeftCandidateColors.items() 
                    if color == downColor
                )
                
                self._handleMatchedLowerLeftCandidateColor(facePosition)
                continue
            
            # now look for the down color in the lower right tile of all the side faces
            
            lowerRightCandidateColors = {
                facePosition: self._cube.cubelets[coord].faces[facePosition]
                for (facePosition, coord) in lowerRightCandidateCoords.items()
            }
            
            if any(color == downColor for (_, color) in lowerRightCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color
                    in lowerRightCandidateColors.items()
                    if color == downColor
                )
                
                self._handleMatchedLowerRightCandidateColor(facePosition)
                continue
            
    def _handleMatchedUpperLeftCandidateColor(self, facePosition: CubeFacePosition):
        """
        handles a color found on the upper left tile of vertical faces, 
        as part of the process for solving the down face
        """
        
        assert isinstance(facePosition, CubeFacePosition)
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # loop until the matched coord is in the proper place
        while True:
            
            # the coordinate where the down color was found
            matchedCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            matchedColor = self._cube.cubelets[matchedCoord].faces[facePosition]
            
            assert matchedColor == downColor
            
            # face position relatively left to the current face position
            relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
            relLeftFaceColor = self._cube.getFaceColor(relLeftFacePosition)
            
            # the coordinate adjacent to the matched coord, across the vertical edge
            adjacentCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[relLeftFacePosition][FaceCubeletPosition.UP_RIGHT]
            adjacentColor = self._cube.cubelets[adjacentCoord].faces[relLeftFacePosition]
            
            if adjacentColor == relLeftFaceColor:
                break
            
            self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            facePosition = relLeftFacePosition
        
        self._trigger(facePosition, FaceRotationDirection.CLOCKWISE)
    
    def _handleMatchedUpperRightCandidateColor(self, facePosition: CubeFacePosition):
        """
        handles a color found on the upper right tile of vertical faces, 
        as part of the process for solving the down face
        """
        
        assert isinstance(facePosition, CubeFacePosition)
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # loop until the matched coord is in the proper place
        while True:
            
            # the coordinate where the down color was found
            matchedCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT]
            matchedColor = self._cube.cubelets[matchedCoord].faces[facePosition]
            
            assert matchedColor == downColor
            
            # face position relatively left to the current face position
            relRightFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_RIGHTWARD)
            relRightFaceColor = self._cube.getFaceColor(relRightFacePosition)
            
            # the coordinate adjacent to the matched coord, across the vertical edge
            adjacentCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[relRightFacePosition][FaceCubeletPosition.UP_LEFT]
            adjacentColor = self._cube.cubelets[adjacentCoord].faces[relRightFacePosition]
            
            if adjacentColor == relRightFaceColor:
                break
            
            self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
            facePosition = relRightFacePosition
        
        self._trigger(facePosition, FaceRotationDirection.COUNTERCLOCKWISE)
    
    def _handleMatchedLowerLeftCandidateColor(self, facePosition: CubeFacePosition):
        """
        handles a color found on the lower left tile of vertical faces, 
        as part of the process for solving the down face
        """
        
        assert isinstance(facePosition, CubeFacePosition)
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # the coordinate where the down color was found
        matchedCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
        matchedColor = self._cube.cubelets[matchedCoord].faces[facePosition]
        
        assert matchedColor == downColor
        
        # face position relatively left to the current face position
        relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
        
        self._trigger(relLeftFacePosition, FaceRotationDirection.COUNTERCLOCKWISE)
    
    def _handleMatchedLowerRightCandidateColor(self, facePosition: CubeFacePosition):
        """
        handles a color found on the lower right tile of vertical faces, 
        as part of the process for solving the down face
        """
        
        assert isinstance(facePosition, CubeFacePosition)
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # the coordinate where the down color was found
        matchedCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.DOWN_RIGHT]
        matchedColor = self._cube.cubelets[matchedCoord].faces[facePosition]
        
        assert matchedColor == downColor
        
        # face position relatively left to the current face position
        relRightFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_RIGHTWARD)
        
        self._trigger(relRightFacePosition, FaceRotationDirection.CLOCKWISE)
    
    def _handleMatchedTopCornerCandidateColor(self, facePosition: CubeFacePosition):
        """
        handles a color found on one the corners of the up face,
        as part of the process for solving the down face
        """
        
        assert isinstance(facePosition, CubeFacePosition)
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # loop until the matched coord is in the proper place
        while True:
            
            # the coordinate where the down color was found
            matchedCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            matchedColor = self._cube.cubelets[matchedCoord].faces[CubeFacePosition.UP]
            
            assert matchedColor == downColor
            
            # the place where this matched color should go
            destCoord = self._cube.VERTICAL_FACE_CORNER_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
            destColor = self._cube.cubelets[destCoord].faces[CubeFacePosition.DOWN]
            
            # if destination is not down color, it is free to place our matched color here
            if destColor != downColor:
                break
            
            self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # face position relatively left to the current face position
            facePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
        
        relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
        self._trigger(relLeftFacePosition, FaceRotationDirection.COUNTERCLOCKWISE, 2)
                
    def _trigger(self, facePosition: CubeFacePosition, direction: FaceRotationDirection, degree: int = 1):
        """ adds a clockwise or counterclockwise trigger of some degree on a cube face to the solution """
        
        assert isinstance(facePosition, CubeFacePosition)
        assert isinstance(direction, FaceRotationDirection)
        
        # make sure degree is a positive integer
        assert isinstance(degree, int)
        assert degree > 0
        
        self._addToSolution(facePosition, direction)
        
        for _ in range(degree):
            self._addToSolution(CubeFacePosition.UP, direction)
        
        oppositeDirection = (
            FaceRotationDirection.CLOCKWISE
            if direction is FaceRotationDirection.COUNTERCLOCKWISE
            else FaceRotationDirection.COUNTERCLOCKWISE
        )
        
        self._addToSolution(facePosition, oppositeDirection)
    
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


import copy

from rubik.cube import Cube
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.solveStage import SolveStage
from rubik.faceCubeletPosition import FaceCubeletPosition
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeSolver():
    """ An entity capable of determining a solution for solving a 3x3x3 Rubik's Cube """
    
    def __init__(self, cube: str | CubeCode | Cube, state = SolveStage.ENTIRE_CUBE):
        """ instantiates a CubeSolver, supplied only a Cube and SolveStage """
        
        # if cube is a string, turn it into a CubeCode
        if isinstance(cube, str):
            cube = CubeCode(cube)
        
        # if cube is a CubeCode, turn it into a Cube
        if isinstance(cube, CubeCode):
            cube = Cube(cube)
        
        assert isinstance(cube, Cube)
        assert isinstance(state, SolveStage)
        
        self._solution = []
        self._cube = copy.deepcopy(cube)
        
        self._solve(state)
    
    def _solve(self, state: SolveStage):
        """ produces a list of rotation directions to reach a certain cube state """
        
        assert isinstance(state, SolveStage)
        
        # directions are not retained from previous solves
        self._clearSolution()
        
        # execute solve algorithm corresponding to the cube state provided
        solveFunctions = {
            SolveStage.DOWN_CROSS: self._solveDownCross,
            SolveStage.DOWN_LAYER: self._solveDownLayer,
            SolveStage.DOWN_AND_MIDDLE_LAYERS: self._solveDownAndMiddleLayers,
            SolveStage.DOWN_MID_LAYERS_AND_UP_FACE: self._solveDownAndMiddleLayersAndUpFace,
            SolveStage.ENTIRE_CUBE: self._solveEntireCube
        }
        solveFunctions[state]()
        
        # optimize directions, replacing redundant rotations
        self._optimizeSolution()
    
    """
    algorithms to solve cube for various cube states,
    the _solve method will start executing one of these
    
    can be viewed as a series of consecutive stages, e.g.
    _solveDownLayer will execute _solveDownCross first
    """
    
    def _solveUpDaisy(self):
        """ constructs an up daisy on the cube """
        
        # if cube already has an up daisy, we're done
        if self._cube.hasUpDaisy():
            return
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        topEdgeCoords = [(1, 0, 0), (0, 0, 1), (1, 0, 2), (2, 0, 1)]
        middleEdgeCoords = [(2, 1, 0), (0, 1, 0), (0, 1, 2), (2, 1, 2)]
        bottomEdgeCoords = [(1, 2, 0), (0, 2, 1), (1, 2, 2), (2, 2, 1)]
        
        verticalFacePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        index = 0
        
        while not self._cube.hasUpDaisy():
            petalCoord = topEdgeCoords[index % 4]
            
            leftEdgeCoord = middleEdgeCoords[(index + 1) % 4]
            downEdgeCoord = bottomEdgeCoords[index % 4]
            rightEdgeCoord = middleEdgeCoords[index % 4]
            
            facePosition = verticalFacePositions[index % 4]
            relativeLeftFacePosition = verticalFacePositions[(index + 1) % 4]
            relativeRightFacePosition = verticalFacePositions[(index - 1) % 4]
            
            edgeCandidateColors = [
                self._cube[leftEdgeCoord][relativeLeftFacePosition],
                self._cube[downEdgeCoord][CubeFacePosition.DOWN],
                self._cube[rightEdgeCoord][relativeRightFacePosition]
            ]
            
            petalColor = self._cube[petalCoord][CubeFacePosition.UP]
            
            while downColor in edgeCandidateColors:
                
                while petalColor == downColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    
                    petalColor = self._cube[petalCoord][CubeFacePosition.UP]
                    
                while petalColor != downColor:
                    self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
                    
                    petalColor = self._cube[petalCoord][CubeFacePosition.UP]
                    
                edgeCandidateColors = [
                    self._cube[leftEdgeCoord][relativeLeftFacePosition],
                    self._cube[downEdgeCoord][CubeFacePosition.DOWN],
                    self._cube[rightEdgeCoord][relativeRightFacePosition]
                ]
                
            faceCandidateCoords = [ leftEdgeCoord, downEdgeCoord, rightEdgeCoord ]
            if petalColor != downColor:
                faceCandidateCoords.append(petalCoord)
            
            faceCandidateColors = list(map(
                lambda coord : self._cube[coord][facePosition],
                faceCandidateCoords
            ))
            
            if downColor in faceCandidateColors and faceCandidateColors[0] != downColor:
                
                while petalColor == downColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                    
                    petalColor = self._cube[petalCoord][CubeFacePosition.UP]
                
                while faceCandidateColors[0] != downColor:
                    self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
                    
                    faceCandidateColors = list(map(
                        lambda coord : self._cube[coord][facePosition],
                        faceCandidateCoords
                    ))
                    
            index += 1
    
    def _solveDownCross(self):
        """ constructs a down cross on the cube """
        
        # if cube already has a down cross, we're done
        if self._cube.hasDownCross():
            return
        
        # have to construct up daisy first
        self._solveUpDaisy()
        assert self._cube.hasUpDaisy()
        
        i = 0
        facePositions = [CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT]
        
        # we are trying to get above color == below color
        # then we flip the petal
        
        # start with front face
        (aboveX, aboveY, aboveZ) = (1, 0, 0)
        (belowX, belowY, belowZ) = (1, 1, 0)
        facePosition = facePositions[i]
        
        # we need to flip all four daisy petals
        while not self._cube.hasDownCross():
            
            aboveColor = self._cube[(aboveX, aboveY, aboveZ)][facePosition]
            belowColor = self._cube[(belowX, belowY, belowZ)][facePosition]
            
            while aboveColor != belowColor:
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                
                (aboveX, aboveY, aboveZ) = self._cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
                
                i = (i + 1) % 4
                facePosition = facePositions[i]
                
                aboveColor = self._cube[(aboveX, aboveY, aboveZ)][facePosition]
                belowColor = self._cube[(belowX, belowY, belowZ)][facePosition]
                
            self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
            self._addToSolution(facePosition, FaceRotationDirection.CLOCKWISE)
            
            (aboveX, aboveY, aboveZ) = self._cube.rotateCoord((aboveX, aboveY, aboveZ), CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            (belowX, belowY, belowZ) = (aboveX, aboveY + 1, aboveZ)
            
            i = (i + 1) % 4
            facePosition = facePositions[i]
    
    def _solveDownLayer(self):
        """ solves down layer of cube """
        
        # if down layer already solved, we're done
        if self._cube.isDownLayerSolved():
            return
        
        # have to construct down cross first
        self._solveDownCross()
        assert self._cube.hasDownCross()
        
        downColor = self._cube.getFaceColor(CubeFacePosition.DOWN)
        
        # these are all of the places where the down corner pieces may show up
        
        upperLeftCandidateCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        upperRightCandidateCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        lowerLeftCandidateCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        lowerRightCandidateCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_RIGHT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        # keep executing this process until down layer solved
        while not self._cube.isDownLayerSolved():
            
            # first look for the down color in the upper left tile of all the side faces
            
            upperLeftCandidateColors = {
                facePosition: self._cube[coord][facePosition]
                for (facePosition, coord) in upperLeftCandidateCoords.items()
            }
            
            # if any are found
            if any(color == downColor for (_, color) in upperLeftCandidateColors.items()):
                
                # figure out where it is
                facePosition = next(
                    facePosition for facePosition, color 
                    in upperLeftCandidateColors.items() 
                    if color == downColor
                )
                
                # pass position to handler function, then start over at top
                self._handleMatchedUpperLeftCandidateColor(facePosition)
                continue
            
            # now look for the down color in the upper right tile of all the side faces
            
            upperRightCandidateColors = {
                facePosition: self._cube[coord][facePosition]
                for (facePosition, coord) in upperRightCandidateCoords.items()
            }
            
            # if any are found
            if any(color == downColor for (_, color) in upperRightCandidateColors.items()):
                
                # figure out where it is
                facePosition = next(
                    facePosition for facePosition, color 
                    in upperRightCandidateColors.items() 
                    if color == downColor
                )
                
                # pass position to handler function, then start over at top
                self._handleMatchedUpperRightCandidateColor(facePosition)
                continue
            
            # now look for the down color in all of the corner tiles of the top face
            
            topCornerCandidateColors = {
                facePosition: self._cube[coord][CubeFacePosition.UP]
                for (facePosition, coord) in upperLeftCandidateCoords.items()
            }
            
            # if any are found
            if any(color == downColor for (_, color) in topCornerCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in topCornerCandidateColors.items() 
                    if color == downColor
                )
                
                # pass position to handler function, then start over at top
                self._handleMatchedTopCornerCandidateColor(facePosition)
                continue
            
            # now look for the down color in the lower left tile of all the side faces
            
            lowerLeftCandidateColors = {
                facePosition: self._cube[coord][facePosition]
                for (facePosition, coord) in lowerLeftCandidateCoords.items()
            }
            
            # if any are found
            if any(color == downColor for (_, color) in lowerLeftCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color 
                    in lowerLeftCandidateColors.items() 
                    if color == downColor
                )
                
                # pass position to handler function, then start over at top
                self._handleMatchedLowerLeftCandidateColor(facePosition)
                continue
            
            # now look for the down color in the lower right tile of all the side faces
            
            lowerRightCandidateColors = {
                facePosition: self._cube[coord][facePosition]
                for (facePosition, coord) in lowerRightCandidateCoords.items()
            }
            
            # if any are found
            if any(color == downColor for (_, color) in lowerRightCandidateColors.items()):
                
                facePosition = next(
                    facePosition for facePosition, color
                    in lowerRightCandidateColors.items()
                    if color == downColor
                )
                
                # pass position to handler function, then start over at top
                self._handleMatchedLowerRightCandidateColor(facePosition)
                continue
            
            # if the down color is not found in any of these locations, then the down FACE is solved,
            # but at least 2 of the corners are in the wrong place
            
            # to solve the down LAYER, we need to handle one of these misplaced corners
            self._fixMalformedDownCorner()
    
    def _solveDownAndMiddleLayers(self):
        """ solves the down and middle layers of the cube """
        
        # if down and middle layers already solved, we are done
        if self._cube.isDownLayerSolved() and self._cube.isMiddleLayerSolved():
            return
        
        # need to solve down layer first
        self._solveDownLayer()
        assert self._cube.isDownLayerSolved()
        
        # color of the up face
        upColor = self._cube.getFaceColor(CubeFacePosition.UP)
        
        # execute algorithm until middle layer is solved
        while not self._cube.isMiddleLayerSolved():
            
            # start with front face
            facePosition = CubeFacePosition.FRONT
            candidateCoord = (1, 0, 0)
            
            # find an up petal cubelet that does not include the up face's color
            found = False
            
            for _ in range(4):
                
                # the 2 colors we need to look at
                candidateColor = self._cube[candidateCoord][CubeFacePosition.UP]
                adjacentColor = self._cube[candidateCoord][facePosition]
                
                if candidateColor != upColor and adjacentColor != upColor:
                    found = True
                    break
                
                # update our reference points
                facePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
                candidateCoord = self._cube.rotateCoord(candidateCoord, CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                
            # if we didn't find a petal cubelet we can transform, then one of the middle cubelets is messed up
            if not found:
                self._fixMalformedMiddleLayer()
                self._solveDownLayer()
                continue
                
            # spin up petal until the adjacent color and its face color match
            for _ in range(4):
                
                adjacentColor = self._cube[candidateCoord][facePosition]
                faceColor = self._cube.getFaceColor(facePosition)
                
                if adjacentColor == faceColor:
                    break
                
                # spin cube and update reference points
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                
                facePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
                candidateCoord = self._cube.rotateCoord(candidateCoord, CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
            relRightFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_RIGHTWARD)
            
            # either the left or right face has color same as the candidate color
            relLeftFaceColor = self._cube.getFaceColor(relLeftFacePosition)
            candidateColor = self._cube[candidateCoord][CubeFacePosition.UP]
            
            # this determines whether a left or right trigger will be executed
            isLeft = (relLeftFaceColor == candidateColor)
            
            # rotate up face one more time, followed by a trigger
            
            if isLeft:
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
                self._trigger(relLeftFacePosition, FaceRotationDirection.COUNTERCLOCKWISE)
            else:
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                self._trigger(relRightFacePosition, FaceRotationDirection.CLOCKWISE)
            
            # clean up down layer
            self._solveDownLayer()
            
    def _solveDownAndMiddleLayersAndUpCross(self):
        """ solves down layer, middle layer, and up cross on the cube """
        
        # need to solve down and middle layers first
        self._solveDownAndMiddleLayers()
        assert self._cube.isDownLayerSolved() and self._cube.isMiddleLayerSolved()
        
        # petals facing back and right
        backPetalCoord = self._cube.FACE_ORIENTATION_COORDS[CubeFacePosition.BACK][FaceCubeletPosition.UP]
        rightPetalCoord = self._cube.FACE_ORIENTATION_COORDS[CubeFacePosition.RIGHT][FaceCubeletPosition.UP]
        
        upColor = self._cube.getFaceColor(CubeFacePosition.UP)
        
        # execute until up cross solved
        while not self._cube.hasUpCross():
            
            # rotate until front petal color is up color
            for _ in range(4):
                if upColor == self._cube[backPetalCoord][CubeFacePosition.UP]:
                    break
                
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
                
            # if the 2 up colors are at 12 and 3 o'clock they need to be 9 and 12 instead
            if upColor == self._cube[rightPetalCoord][CubeFacePosition.UP]:
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
            
            # now we're ready for a furf!
            self._executeFurf()
    
    def _solveDownAndMiddleLayersAndUpFace(self):
        """ solves down layer, middle layer, and up face on the cube """
        
        # need to solve down, middle layers, and up cross first
        self._solveDownAndMiddleLayersAndUpCross()
        assert (
            self._cube.isDownLayerSolved() and self._cube.isMiddleLayerSolved()
            and self._cube.hasUpCross()
        )
        
        # upper left corner coords of each vertical face position,
        # also each of the corners on the up face that need to be filled in
        upLeftCornerCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        frontLeftCoord = upLeftCornerCoords[CubeFacePosition.FRONT]
        
        upColor = self._cube.getFaceColor(CubeFacePosition.UP)
        
        # continue until up face is solved
        while not self._cube.isUpFaceSolved():
            
            # count how many corners match the up color
            cornerCount = sum(
                1 for coord in upLeftCornerCoords.values()
                if self._cube[coord][CubeFacePosition.UP] == upColor
            )
            
            # if only one matched, it's a fish
            if cornerCount == 1:
                
                # get that matched corner in the front left
                while self._cube[frontLeftCoord][CubeFacePosition.UP] != upColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # otherwise, get the left side of front left cubelet to be the up color
            else:
                while self._cube[frontLeftCoord][CubeFacePosition.LEFT] != upColor:
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # now the cube is ready for the Rurr move!
            self._executeRurr()
            
            # these sequences shouldn't affect the down and middle layers
            assert self._cube.isDownLayerSolved()
            assert self._cube.isMiddleLayerSolved()
    
    def _solveEntireCube(self):
        """ solves entire cube """
        
        # need to solve down, middle layers, and up face first
        self._solveDownAndMiddleLayersAndUpFace()
        assert (
            self._cube.isDownLayerSolved() and self._cube.isMiddleLayerSolved()
            and self._cube.isUpFaceSolved()
        )
        
        # first we need to align the up face corners
        
        verticalFacePositions = [
            CubeFacePosition.FRONT, CubeFacePosition.LEFT, CubeFacePosition.BACK, CubeFacePosition.RIGHT
        ]
        
        leftCornerCoords = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            for facePosition in verticalFacePositions
        }
        
        while not self._cube.isUpCornersSolved():
            
            # attempt to align all 4 corners (maybe the up face just has to be rotated N times)
            # also keep track of the aligned corner count (maximal)
            
            maxAlignedCornerCount = -1
            
            for _ in range(4):
                if self._cube.isUpCornersSolved():
                    maxAlignedCornerCount = 4
                    break
                
                alignedCornerCount = sum(
                    1 for (facePosition, coord) in leftCornerCoords.items()
                    if self._cube[coord][facePosition] == self._cube.getFaceColor(facePosition)
                )
                
                maxAlignedCornerCount = max(alignedCornerCount, maxAlignedCornerCount)
                
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # if that solved it, we're done fixing corners
            if maxAlignedCornerCount == 4:
                break
            
            # rotate up face until aligned corners are maximal
            
            for _ in range(4):
                
                alignedCornerCount = sum(
                    1 for (facePosition, coord) in leftCornerCoords.items()
                    if self._cube[coord][facePosition] == self._cube.getFaceColor(facePosition)
                )
                
                if alignedCornerCount == maxAlignedCornerCount:
                    break
                
                self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # which corners are aligned?
            alignedLeftCornerPositions = [
                facePosition for (facePosition, coord) in leftCornerCoords.items()
                if self._cube[coord][facePosition] == self._cube.getFaceColor(facePosition)
            ]
            
            # if 2 corners are aligned, and they're not adjacent, need to rotate one more time
            if maxAlignedCornerCount == 2:
                [cornerPositionA, cornerPositionB] = alignedLeftCornerPositions
                
                if not CubeFacePosition.isAdjacent(cornerPositionA, cornerPositionB, CubeRotationDirection.SPIN_LEFTWARD):
                    self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # finally in the right position to execute corner swap algorithms
            
            # first need to obtain a frame of reference (we want solved corners on the relative 
            # left side if any exist)
            
            relLeftPosition = CubeFacePosition.LEFT
            
            if len(alignedLeftCornerPositions) == 1:
                relLeftPosition = alignedLeftCornerPositions[0]
            
            if len(alignedLeftCornerPositions) == 2:
                [cornerPositionA, cornerPositionB] = alignedLeftCornerPositions
                
                if CubeFacePosition.rotate(cornerPositionA, CubeRotationDirection.SPIN_LEFTWARD) == cornerPositionB:
                    relLeftPosition = cornerPositionB
                else:
                    relLeftPosition = cornerPositionA
            
            # now execute moves lurr and rurr
            self._executeLurr(relLeftPosition)
            self._executeRurr(relLeftPosition)
            
        # now need to solve the 4 up cubelet faces of each vertical face position
        
        while not self._cube.isUpLayerSolved():
            
            # if any of these 4 are already solved, the algorithm needs one of these
            # to serve as the relative back position for the rotation sequence
            
            relBackPosition = CubeFacePosition.BACK
            
            for facePosition in verticalFacePositions:
                
                coord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP]
                
                color = self._cube[coord][facePosition]
                faceColor = self._cube.getFaceColor(facePosition)
                
                if color == faceColor:
                    relBackPosition = facePosition
                    break
            
            # execute Ffuf and Lruf moves
            self._executeFfuf(relBackPosition)
            self._executeLruf(relBackPosition)
    
    """
    various auxiliary methods used by the cube solver algorithms
    """
       
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
            matchedCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            matchedColor = self._cube[matchedCoord][facePosition]
            
            assert matchedColor == downColor
            
            # face position relatively left to the current face position
            relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
            relLeftFaceColor = self._cube.getFaceColor(relLeftFacePosition)
            
            # the coordinate adjacent to the matched coord, across the vertical edge
            adjacentCoord = self._cube.FACE_ORIENTATION_COORDS[relLeftFacePosition][FaceCubeletPosition.UP_RIGHT]
            adjacentColor = self._cube[adjacentCoord][relLeftFacePosition]
            
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
            matchedCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_RIGHT]
            matchedColor = self._cube[matchedCoord][facePosition]
            
            assert matchedColor == downColor
            
            # face position relatively left to the current face position
            relRightFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_RIGHTWARD)
            relRightFaceColor = self._cube.getFaceColor(relRightFacePosition)
            
            # the coordinate adjacent to the matched coord, across the vertical edge
            adjacentCoord = self._cube.FACE_ORIENTATION_COORDS[relRightFacePosition][FaceCubeletPosition.UP_LEFT]
            adjacentColor = self._cube[adjacentCoord][relRightFacePosition]
            
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
        matchedCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
        matchedColor = self._cube[matchedCoord][facePosition]
        
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
        matchedCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_RIGHT]
        matchedColor = self._cube[matchedCoord][facePosition]
        
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
            matchedCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.UP_LEFT]
            matchedColor = self._cube[matchedCoord][CubeFacePosition.UP]
            
            assert matchedColor == downColor
            
            # the place where this matched color should go
            destCoord = self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
            destColor = self._cube[destCoord][CubeFacePosition.DOWN]
            
            # if destination is not down color, it is free to place our matched color here
            if destColor != downColor:
                break
            
            self._addToSolution(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
            
            # face position relatively left to the current face position
            facePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
        
        relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
        self._trigger(relLeftFacePosition, FaceRotationDirection.COUNTERCLOCKWISE, 2)
    
    def _fixMalformedMiddleLayer(self):
        """ an auxiliary method for solveDownAndMiddleLayers that fixes the state of the middle layer """
        
        # these are all of the possible problem spots, each on an edge between 2 cube faces
        possibleMalformedPositions = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.LEFT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        # first check for positions in which both cubelet faces are on the wrong face
        
        for (facePosition, coord) in possibleMalformedPositions.items():
            rightColor = self._cube[coord][facePosition]
            
            relLeftFacePosition = CubeFacePosition.rotate(facePosition, CubeRotationDirection.SPIN_LEFTWARD)
            leftColor = self._cube[coord][relLeftFacePosition]
            
            # determine whether the 2 cubelet faces are the same color as the cube faces they are on
            isLeftInPlace = (leftColor == self._cube.getFaceColor(relLeftFacePosition))
            isRightInPlace = (rightColor == self._cube.getFaceColor(facePosition))
            
            # if it's in the wrong place, fix by triggering it
            if not isLeftInPlace or not isRightInPlace:
                self._trigger(facePosition, FaceRotationDirection.CLOCKWISE)
                return
    
    def _fixMalformedDownCorner(self):
        
        # these are all of the possible problem spots, each of the down corners
        possibleMalformedCorners = {
            facePosition: self._cube.FACE_ORIENTATION_COORDS[facePosition][FaceCubeletPosition.DOWN_LEFT]
            for facePosition in self._cube.FACE_ORIENTATION_COORDS
        }
        
        # iterate over all corners
        for (facePosition, coord) in possibleMalformedCorners.items():
            
            # compare the corner color to the cube face color
            faceColor = self._cube.getFaceColor(facePosition)
            cornerColor = self._cube[coord][facePosition]
            
            # in case of mismatch
            if faceColor != cornerColor:
                # here is a malformed corner, trigger it
                self._trigger(facePosition, FaceRotationDirection.CLOCKWISE)
                return
    
    """
    methods for executing special rotation sequences on the cube,
    ones that repeatedly come up in cube solver algorithms
    
    some have abbreviated codenames I have defined for them
    """
    
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
    
    def _executeFurf(self):
        """ execute a Furf move, defined by the rotation sequence FURurf """
        
        # the 6 rotations that comprise a FURurf sequence
        rotations = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        # add each one to the solution
        for (facePosition, direction) in rotations:
            self._addToSolution(facePosition, direction)
    
    def _executeRurr(self, relLeftPosition: CubeFacePosition = CubeFacePosition.LEFT):
        """ execute a Rurr move, defined by the rotation codes RUrURUUr """
        
        # figure out relative right position from relative left position
        relRightPosition = CubeFacePosition.rotate(relLeftPosition, CubeRotationDirection.SPIN_LEFTWARD)
        relRightPosition = CubeFacePosition.rotate(relRightPosition, CubeRotationDirection.SPIN_LEFTWARD)
        
        # the 8 rotations that comprise a RUrURUUr sequence
        rotations = [
            (relRightPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.COUNTERCLOCKWISE),
        ]
        
        # add each one to the solution
        for (facePosition, direction) in rotations:
            self._addToSolution(facePosition, direction)
    
    def _executeLurr(self, relLeftPosition: CubeFacePosition = CubeFacePosition.LEFT):
        """ execute a Lurr move, defined by the rotation codes lURuLUr """
        
        # figure out relative right position from relative left position
        relRightPosition = CubeFacePosition.rotate(relLeftPosition, CubeRotationDirection.SPIN_LEFTWARD)
        relRightPosition = CubeFacePosition.rotate(relRightPosition, CubeRotationDirection.SPIN_LEFTWARD)
        
        # the 7 rotations that comprise a lURuLUr sequence
        rotations = [
            (relLeftPosition, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (relLeftPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        # add each one to the solution
        for (facePosition, direction) in rotations:
            self._addToSolution(facePosition, direction)
    
    def _executeFfuf(self, relBackPosition: CubeFacePosition = CubeFacePosition.BACK):
        """ execute a Ffuf move, defined by the rotation codes FFUrLFF """
        
        relLeftPosition = CubeFacePosition.rotate(relBackPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        relFrontPosition = CubeFacePosition.rotate(relLeftPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        relRightPosition = CubeFacePosition.rotate(relFrontPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        
        # the 7 rotations that comprise a FFUrLFF sequence
        rotations = [
            (relFrontPosition, FaceRotationDirection.CLOCKWISE),
            (relFrontPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relRightPosition, FaceRotationDirection.COUNTERCLOCKWISE),
            (relLeftPosition, FaceRotationDirection.CLOCKWISE),
            (relFrontPosition, FaceRotationDirection.CLOCKWISE),
            (relFrontPosition, FaceRotationDirection.CLOCKWISE)
        ]
        
        # add each one to the solution
        for (facePosition, direction) in rotations:
            self._addToSolution(facePosition, direction)
    
    def _executeLruf(self, relBackPosition: CubeFacePosition = CubeFacePosition.BACK):
        """ execute a Lruf move, defined by the rotation codes lRUFF """
        
        relLeftPosition = CubeFacePosition.rotate(relBackPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        relFrontPosition = CubeFacePosition.rotate(relLeftPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        relRightPosition = CubeFacePosition.rotate(relFrontPosition, CubeRotationDirection.SPIN_RIGHTWARD)
        
        # the 5 rotations that comprise a lRUFF sequence
        rotations = [
            (relLeftPosition, FaceRotationDirection.COUNTERCLOCKWISE),
            (relRightPosition, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (relFrontPosition, FaceRotationDirection.CLOCKWISE),
            (relFrontPosition, FaceRotationDirection.CLOCKWISE)
        ]
        
        # add each one to the solution
        for (facePosition, direction) in rotations:
            self._addToSolution(facePosition, direction)
    """
    methods dealing with manipulating _solution field
    """
    
    def getSolution(self):
        """ accessor for _solution field """
        
        return self._solution
    
    def _addToSolution(self, facePosition: CubeFacePosition, direction: FaceRotationDirection):
        """ executes cube rotation and adds it to the solve directions """
        
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(direction, FaceRotationDirection))
        
        self._cube.rotateFace(facePosition, direction)
        self._solution.append((facePosition, direction))
    
    def _optimizeSolution(self):
        """ optimizes solution, removing redundancy """
        
        if len(self._solution) < 2:
            return
        
        optimizedSolution = [self._solution[0]]
        
        for (face, direction) in self._solution[1:]:
            
            if len(optimizedSolution) > 0:
                (lastFace, lastDirection) = optimizedSolution[-1]
            
                # determine whether we are just mirroring last step
                if lastFace == face and lastDirection != direction: 
                    # accomplishes nothing, remove these
                    optimizedSolution = optimizedSolution[:-1]
                    continue
            
            if len(optimizedSolution) > 1:
                (lastFace, lastDirection) = optimizedSolution[-1]
                (beforeLastFace, beforeLastDirection) = optimizedSolution[-2]
            
                # check whether this is the 3rd repeat in a row
                if (
                    face == lastFace and face == beforeLastFace
                    and direction == lastDirection and direction == beforeLastDirection
                ):
                    # if so, replace all 3 with other rotation direction
                    replacementDirection = (
                        FaceRotationDirection.CLOCKWISE
                        if direction is FaceRotationDirection.COUNTERCLOCKWISE
                        else FaceRotationDirection.COUNTERCLOCKWISE
                    )
                    
                    optimizedSolution = optimizedSolution[:-2]
                    optimizedSolution.append((face, replacementDirection))
                    continue
            
            # else append solution step to optimized solution
            optimizedSolution.append((face, direction))
            
        self._solution = optimizedSolution
    
    def _clearSolution(self):
        """ resets solution """
        
        self._solution.clear()

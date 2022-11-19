
from unittest import TestCase

from rubik.cubeSolver import CubeSolver
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.solveStage import SolveStage
from rubik.cube import Cube

class CubeSolverTest(TestCase):
    
    ''' CubeSolver.__init__ -- NEGATIVE TESTS '''
    
    def test_cubeSolver_init_10010_ShouldThrowExceptionForNonSuppliedCube(self):
        """ supplying no cube should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver()
    
    def test_cubeSolver_init_10020_ShouldThrowExceptionForCubeOfInvalidType(self):
        """ supplying cube of invalid type should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
    
    ''' CubeSolver.__init__ -- POSITIVE TESTS '''
    
    def test_cubeSolver_init_20010_ShouldInstantiateCubeSolverForValidCubeCode(self):
        """ supplying valid cube should instantiate cube solver """
        
        solver = CubeSolver('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        
        self.assertIsInstance(solver, CubeSolver)
    
    def test_cubeSolver_init_20020_ASolvedCubeShouldYieldNoDirectionsToSolveDownCross(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_CROSS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_20021_ACubeWithDownCrossShouldYieldNoDirectionsToSolveDownCross(self):
        """ a cube with a down cross should give no solve directions """
        
        solver = CubeSolver(
            'bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy',
            SolveStage.DOWN_CROSS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_20030_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_20031_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_20032_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_20040_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_20041_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
    
    def test_cubeSolver_init_20042_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        
        solver = CubeSolver(cube, SolveStage.DOWN_CROSS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down cross
        self.assertTrue(cube.hasDownCross())
        
    def test_cubeSolver_init_20050_ASolvedCubeShouldYieldNoDirectionsToSolveDownLayer(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_LAYER
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
        
    def test_cubeSolver_init_20051_ACubeWithASolvedDownLayerShouldYieldNoDirectionsToSolveDownLayer(self):
        """ a cube with a solved down layer should give no solve directions """
        
        solver = CubeSolver(
            'yryybgbbbgybrryrrrygyogrgggrorbobooogoobygbyowwwwwwwww',
            SolveStage.DOWN_LAYER
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
    
    def test_cubeSolver_init_20060_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_20061_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_20062_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        cube = Cube('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_20070_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_20071_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_cubeSolver_init_20072_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        cube = Cube('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        
        solver = CubeSolver(cube, SolveStage.DOWN_LAYER)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down layer
        self.assertTrue(cube.isDownLayerSolved())
        
    def test_cubeSolver_init_20080_ShouldSolveDownAndMiddleLayersAndUpCrossByDefault(self):
        """ if no cube state supplied, should solve down and middle layers and the up cross """
        
        cube = Cube('rrgoborgorgwyroygobrgwgwwryogybobrbbyboryogwwwwbywybyg')
        
        firstSolver = CubeSolver(cube, SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS)
        secondSolver = CubeSolver(cube)
        
        self.assertEqual(firstSolver.getSolution(), secondSolver.getSolution())
    
    def test_cubeSolver_init_20090_ASolvedCubeShouldYieldNoRotationsToSolveDownAndMiddleLayers(self):
        """ a solved cube should give no rotations to solve down and middle layers """
        
        solver = CubeSolver(
            'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            SolveStage.DOWN_AND_MIDDLE_LAYERS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
        
    def test_cubeSolver_init_20091_ACubeWithSolvedDownAndMiddleLayersShouldYieldNoRotationsToSolveThoseTwoLayers(self):
        """ a cube with solved down, mid layers should give no directions to solve down, mid layers """
        
        solver = CubeSolver(
            'ygrbbbbbbyoyrrrrrrgryggggggrbboooooogyoyyyoybwwwwwwwww',
            SolveStage.DOWN_AND_MIDDLE_LAYERS
        )
        solution = solver.getSolution()
        
        self.assertEqual(len(solution), 0)
        
    def test_cubeSolver_init_20100_ACubeWithSolvedDownLayerShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with solved down layer should yield correct rotations to solve down and middle layers """
        
        cube = Cube('gorybybbbyoybrrrrroggbgygggobrrogoooyrboyyygbwwwwwwwww')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_20101_AnotherCubeWithSolvedDownLayerShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ another cube with solved down layer should yield correct rotations to solve down and middle layers """
        
        cube = Cube('roggbybbboorrrbrrryyorgbgggbgyooroooybbyyyggywwwwwwwww')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_20110_ACubeWithDownCrossShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('rggbbggbyrrbrrygrboygbgyogbwywgooyooorwoybbowywrwwwrwy')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_20120_ACubeWithUpDaisyShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('brogbbbowggryrgbrywoyrgroyorbwbooyorgwgwywowwyyrbwybgg')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_cubeSolver_init_20130_AnUnsolvedCubeWithoutAnyProgressShouldYieldCorrectRotationsToSolveDownAndMiddleLayers(self):
        """ a cube with down cross should yield correct rotations to solve down and middle layers """
        
        cube = Cube('rorwbrrgwwgrbrygwoyogoggbgyoywworbygywbbyobbgyrorwboyw')
        
        solver = CubeSolver(cube, SolveStage.DOWN_AND_MIDDLE_LAYERS)
        solution = solver.getSolution()
        
        # execute all of the solution rotations
        for (facePosition, direction) in solution:
            cube.rotateFace(facePosition, direction)
        
        # check whether it actually solved down and middle layers
        self.assertTrue(cube.isDownLayerSolved())
        self.assertTrue(cube.isMiddleLayerSolved())
        
    def test_cubeSolver_init_20140_ASolvedCubeShouldYieldNoRotationsToSolveDownAndMiddleLayersAndUpCross(self):
        """ a solved cube should give no rotations to solve down and middle layers """
        
        solver = CubeSolver('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS)
        expected = []
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_20141_ACubeWithSolvedDownAndMiddleLayersAndUpCrossShouldYieldNoRotationsToSolveThose(self):
        """ a cube with solved down, mid layers and up cross should give no directions to solve down, mid layers and up cross """
        
        solver = CubeSolver('ygrbbbbbbyoyrrrrrrgryggggggrbboooooogyoyyyoybwwwwwwwww', SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS)
        expected = []
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_20150_ACubeWithSolvedDownAndMiddleLayersShouldYieldCorrectDirectionsToSolveDownMidLayersAndUpCross(self):
        """ a cube with solved down, mid layers should give correct directions to solve down, mid layers and up cross """
        
        solver = CubeSolver(
            'gbgbbbbbbyyyrrrrrrbobggggggyyyoooooooyrrygoyrwwwwwwwww',
            SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS
        )
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getSolution(), expected)
        
    def test_cubeSolver_init_20160_ACubeWithSolvedDownLayerShouldYieldCorrectDirectionsToSolveDownMidLayersAndUpCross(self):
        
        solver = CubeSolver(
            'gyyobgbbbbborryrrrybobgggggbrryogoooyogyyryorwwwwwwwww',
            SolveStage.DOWN_MID_LAYERS_AND_UP_CROSS
        )
        
        expected = [
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getSolution(), expected)
    
    def test_cubeSolver_init_20170_InputCubeShouldNotBeModified(self):
        """ the cube supplied to the cube solver should not be modified """
        
        code = 'rbgobbogbwyboroywwyggwgrbbyroywogogwwyoyyrgyobrrwwbgrr'
        cube = Cube(code)
        
        CubeSolver(cube)
        self.assertEqual(cube.toCode(), code)
    
    ''' CubeSolver.getSolution -- POSITIVE TESTS '''
    
    def test_cubeSolver_getSolution_20010_ShouldReturnValidDirections(self):
        """ should return list of type (CubeFacePosition, FaceRotationDirection) """
        
        solver = CubeSolver('gbogbobwowboyroyrygbrggrrwywwyyoygrwgowbyyorbrgbwwgrob')
        
        rotations = solver.getSolution()
        
        # make sure directions is a list
        self.assertIsInstance(rotations, list)
        
        for rotation in rotations:
            # make sure each direction is a tuple
            self.assertIsInstance(rotation, tuple)
            
            # make sure each direction tuple has 2 items each
            self.assertEqual(len(rotation), 2)
            
            # make sure each direction is of type (CubeFacePosition, FaceRotationDirection)
            (facePosition, rotationDirection) = rotation
            
            self.assertIsInstance(facePosition, CubeFacePosition)
            self.assertIsInstance(rotationDirection, FaceRotationDirection)
    
    
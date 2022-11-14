
from unittest import TestCase

from rubik.cubeSolver import CubeSolver
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cubeState import CubeState

class CubeSolverTest(TestCase):
    
    # CubeSolver.__init__ -- POSITIVE TESTS
    
    def test_cubeSolver_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        """ supplying valid cube should instantiate cube solver """
        
        solver = CubeSolver('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        
        self.assertIsInstance(solver, CubeSolver)
    
    # CubeSolver.__init__ -- NEGATIVE TESTS
    
    def test_cubeSolver_init_20010_ShouldThrowExceptionForNonSuppliedCube(self):
        """ supplying no cube should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver()
    
    def test_cubeSolver_init_20020_ShouldThrowExceptionForCubeOfInvalidType(self):
        """ supplying cube of invalid type should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
    
    # CubeSolver.solve -- POSITIVE TESTS
    
    def test_cubeSolver_solve_10010_ACubeWithUpDaisyAlreadyShouldYieldNoDirectionsToSolveUpDaisy(self):
        """ a cube with an up daisy should yield no solve directions """
        
        solver = CubeSolver('ybrrbggrobgborobyoyrobgbwyyyoryobgorgwowywbwwwgwywgrrg')
        solver.solve(CubeState.UP_DAISY)
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10020_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveUpDaisy(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        solver.solve(CubeState.UP_DAISY)
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10021_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveUpDaisy(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        solver.solve(CubeState.UP_DAISY)
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10022_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveUpDaisy(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        solver.solve(CubeState.UP_DAISY)
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10030_ASolvedCubeShouldYieldNoDirectionsToSolveDownCross(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10031_ACubeWithADownCrossAlreadyShouldYieldNoDirectionsToSolveDownCross(self):
        """ a cube with a down cross should give no solve directions """
        
        solver = CubeSolver('bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10040_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10041_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10042_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10050_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10051_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10052_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownCross(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        solver.solve(CubeState.DOWN_CROSS)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
        
    def test_cubeSolver_solve_10060_ASolvedCubeShouldYieldNoDirectionsToSolveDownLayer(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
        
    def test_cubeSolver_solve_10061_ACubeWithASolvedDownLayerShouldYieldNoDirectionsToSolveDownLayer(self):
        """ a cube with a solved down layer should give no solve directions """
        
        solver = CubeSolver('yryybgbbbgybrryrrrygyogrgggrorbobooogoobygbyowwwwwwwww')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10070_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            # ggyrbyybbborrrbwrwwgorgobgogbybogyorwogyyyoyrgwowwwbwr
            
            # solve down layer
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10071_AnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve down cross
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # wygrbyybwwgwbrorrrrooygrygrbrogoybogybbbyobgoowgwwwywg
            
            # solve down layer
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10072_YetAnotherCubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube with an up daisy should yield correct solve directions """
        
        solver = CubeSolver('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve down cross
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            # wbggbgwbbrygyryorryowogrbgooybgoogobgbrrybrrwowywwwywy
            
            # solve down layer
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10080_ACubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ a cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # solve down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            # bbroborboggygroyrggbrbggogbbyyroywowwroryyryygwbwwwoww
            
            # solve down layer
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10081_AnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # solve down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # gybybowbbrboyrbrrbwrgogooggoyrgoboogygbryrygyrwwwwwwwy
            
            # solve down layer
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10082_YetAnotherCubeWithoutUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ yet another cube without an up daisy should yield correct solve directions """
        
        solver = CubeSolver('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        solver.solve(CubeState.DOWN_LAYER_SOLVED)
        
        expected = [
            # solve up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # solve down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            # ygybbygbogrrrrbbrrbbbrgoggrrobgoyyowyowyygoyoowwwwwgww
            
            # solve down layer
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    # getDirections -- POSITIVE TESTS
    
    def test_cubeSolver_getDirections_10010_ShouldReturnValidDirections(self):
        """ should return list of type (CubeFacePosition, FaceRotationDirection) """
        
        solver = CubeSolver('gbogbobwowboyroyrygbrggrrwywwyyoygrwgowbyyorbrgbwwgrob')
        solver.solve(CubeState.DOWN_CROSS)
        
        directions = solver.getDirections()
        
        # make sure directions is a list
        self.assertIsInstance(directions, list)
        
        for direction in directions:
            # make sure each direction is a tuple
            self.assertIsInstance(direction, tuple)
            
            # make sure each direction tuple has 2 items each
            self.assertEqual(len(direction), 2)
            
            # make sure each direction is of type (CubeFacePosition, FaceRotationDirection)
            (facePosition, rotationDirection) = direction
            
            self.assertIsInstance(facePosition, CubeFacePosition)
            self.assertIsInstance(rotationDirection, FaceRotationDirection)
    
    def test_cubeSolver_getDirections_10020_ShouldBeEmptyIfCubeNeverSolved(self):
        """ should return empty list if Cube.solve() never called """
        
        solver = CubeSolver('grwgbwyrygbbbrwgoywwwoggbgwooyrooorbggrbyyowrryrbwybyo')
        
        directions = solver.getDirections()
        
        self.assertEqual(len(directions), 0)
        
    def test_cubeSolver_getDirections_10030_ShouldNotCarryOverDirectionsFromPreviousSolves(self):
        """ each time solve is executed, the directions should be reset """
        
        solver = CubeSolver('ogrybwryywogorbggbogbygwwgbrrwbooowbyoybybgrgwrrrwwyyo')
        
        # solve a cube fully
        solver.solve()
        # then solve it again (even though it's already solved)
        solver.solve()
        
        # should yield no solve directions
        directions = solver.getDirections()
        
        self.assertEqual(len(directions), 0)
        
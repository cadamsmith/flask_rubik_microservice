
from unittest import TestCase

from rubik.cubeSolver import CubeSolver
from rubik.cube import Cube
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolverTest(TestCase):
    
    # CubeSolver.__init__ -- POSITIVE TESTS
    
    def test_cubeSolver_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        """ supplying valid cube should instantiate cube solver """
        
        cube = Cube('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        solver = CubeSolver(cube)
        
        self.assertIsInstance(solver, CubeSolver)
    
    # CubeSolver.__init__ -- NEGATIVE TESTS
    
    def test_cubeSolver_init_20010_ShouldThrowExceptionForNonSuppliedCube(self):
        """ supplying no cube should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver()
    
    def test_cubeSolver_init_20020_ShouldTHrowExceptionForCubeOfInvalidType(self):
        """ supplying cube of invalid type should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
    
    # CubeSolver.solve -- POSITIVE TESTS
    
    def test_cubeSolver_solve_10010_ASolvedCubeShouldYieldNoSolveDirections(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver(
            Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        )
        solver.solve()
        
        expected = []
        actual = solver._directions
        
        self.assertEqual(actual, expected)
    
    def test_cubeSolver_solve_10020_ACubeWithABottomCrossAlreadyShouldYieldNoSolveDirections(self):
        """ a cube with a bottom cross should give no solve directions """
        
        solver = CubeSolver(
            Cube('bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy')
        )
        solver.solve()
        
        expected = []
        actual = solver._directions
        
        self.assertEqual(actual, expected)
    
    def test_cubeSolver_solve_10030_ACubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        )
        solver.solve()
        
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
        
        self.assertEqual(solver._directions, expected)
    
    def test_cubeSolver_solve_10031_AnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        )
        solver.solve()
        
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
        
        self.assertEqual(solver._directions, expected)
    
    def test_cubeSolver_solve_10032_YetAnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        )
        solver.solve()
        
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
        
        self.assertEqual(solver._directions, expected)
    
    def test_cubeSolver_solve_10040_ACubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        )
        solver.solve()
        
        expected = [
            # make up daisy
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
        
        self.assertEqual(solver._directions, expected)
    
    def test_cubeSolver_solve_10041_AnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        )
        solver.solve()
        
        expected = [
            # make up daisy
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
        
        self.assertEqual(solver._directions, expected)
    
    def test_cubeSolver_solve_10042_YetAnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver(
            Cube('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        )
        solver.solve()
        
        expected = [
            # make up daisy
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
        
        self.assertEqual(solver._directions, expected)

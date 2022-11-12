
from unittest import TestCase
from rubik.cubeSolver import CubeSolver
from rubik.cube import Cube
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolverTest(TestCase):
    
    # init - POSITIVE TESTS
    
    # supplying valid cube should instantiate cube solver
    def test_cubeSolver_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        
        cube = Cube(CubeCode('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg'))
        solver = CubeSolver(cube)
        
        self.assertIsInstance(solver, CubeSolver)
    
    # init - NEGATIVE TESTS
    
    # supplying no cube should throw exception
    def test_cubeSolver_init_20010_ShouldThrowExceptionForNonSuppliedCube(self):
        
        with self.assertRaises(Exception):
            CubeSolver()
            
    # supplying cube of invalid type should throw exception
    def test_cubeSolver_init_20020_ShouldTHrowExceptionForCubeOfInvalidType(self):
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
            
    # solve - POSITIVE TESTS
    
    # an already solved cube should give no solve directions
    def test_cubeSolver_solve_10010_ASolvedCubeShouldYieldNoSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        )
        
        expected = []
        actual = solver.solve()
        
        self.assertEqual(actual, expected)
    
    # a cube with a bottom cross should give no solve directions
    def test_cubeSolver_solve_10020_ACubeWithABottomCrossAlreadyShouldYieldNoSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy'))
        )
        
        expected = []
        actual = solver.solve()
        
        self.assertEqual(actual, expected)
    
    # a cube with a top daisy should yield correct solve directions
    def test_cubeSolver_solve_10030_ACubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg'))
        )
        
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
        
        self.assertEqual(solver.solve(), expected)
        
    def test_cubeSolver_solve_10040_ACubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('ybboboygbyrrborwrwgowygrbyogggbrgbbgowwwywowrryrywgyoo'))
        )
        
        expected = [
            # make up daisy
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # make down cross
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.solve(), expected)
    
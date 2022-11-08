
from unittest import TestCase
from rubik.cubeSolver import CubeSolver
from rubik.cube import Cube
from rubik.cubeCode import CubeCode

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
    def test_cubeSolver_solve_20010_ASolvedCubeShouldYieldNoSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        )
        
        expected = []
        actual = solver.solve()
        
        self.assertEqual(actual, expected)
    
    # a cube with a bottom cross should give no solve directions
    def test_cubeSolver_solve_20020_ACubeWithABottomCrossAlreadyShouldYieldNoSolveDirections(self):
        
        solver = CubeSolver(
            Cube(CubeCode('bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy'))
        )
        
        expected = []
        actual = solver.solve()
        
        self.assertEqual(actual, expected)
    
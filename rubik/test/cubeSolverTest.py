
from unittest import TestCase
from rubik.cubeSolver import CubeSolver

class CubeSolverTest(TestCase):
    
    # init - NEGATIVE TESTS
    
    # supplying no cube should throw exception
    def test_cubeSolver_init_20010_ShouldThrowExceptionForNonSuppliedCube(self):
        
        with self.assertRaises(Exception):
            CubeSolver()
            
    # supplying cube of invalid type should throw exception
    def test_cubeSolver_iinit_20020_ShouldTHrowExceptionForCubeOfInvalidType(self):
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
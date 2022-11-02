
from unittest import TestCase
from rubik.cube import Cube

class CubeTest(TestCase):
    
    ## __init__ - NEGATIVE TESTS
    
    # supplying a param not a dictionary or a string should throw exception
    def test_cube_init_20010_ShouldThrowExceptionForInvalidParamType(self):
        with self.assertRaises(Exception):
            Cube(2.3)

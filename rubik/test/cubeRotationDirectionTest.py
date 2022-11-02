
from unittest import TestCase
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeRotationDirectionTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 4 cube rotation directions (by nature of a cube)
    def test_cubeFace_00010_ShouldHaveExactlySixItems(self):
        expected = 4
        actual = len(list(CubeRotationDirection))
        
        self.assertEqual(expected, actual)
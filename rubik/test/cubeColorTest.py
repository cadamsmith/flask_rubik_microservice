
from unittest import TestCase
from rubik.cubeColor import CubeColor

class CubeColorTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 6 cube colors
    def test_cubeColor_00010_ShouldHaveExactlySixColors(self):
        expected = 6
        actual = len(list(CubeColor))
        
        self.assertEqual(expected, actual)

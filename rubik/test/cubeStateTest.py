
from unittest import TestCase

from rubik.cubeState import CubeState

class CubeStateTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 3 cube states
    def test_cubeState_00010_ShouldHaveExactlyThreeItems(self):
        expected = 3
        actual = len(list(CubeState))
        
        self.assertEqual(expected, actual)

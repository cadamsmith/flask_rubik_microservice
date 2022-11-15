
from unittest import TestCase

from rubik.cubeState import CubeState

class CubeStateTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 4 cube states
    def test_cubeState_00010_ShouldHaveExactlyThreeItems(self):
        expected = 4
        actual = len(list(CubeState))
        
        self.assertEqual(expected, actual)

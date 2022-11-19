
from unittest import TestCase

from rubik.solveStage import SolveStage

class SolveStageTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 5 solve stages
    def test_solveStage_00010_ShouldHaveExactlyFiveItems(self):
        expected = 5
        actual = len(list(SolveStage))
        
        self.assertEqual(expected, actual)


from unittest import TestCase

from rubik.solveStage import SolveStage

class SolveStageTest(TestCase):
    
    ''' SolveStage -- GENERAL TESTS '''
    
    def test_solveStage_00010_ShouldHaveExactlyFiveItems(self):
        """ there should be only 5 solve stages """
        
        expected = 5
        actual = len(list(SolveStage))
        
        self.assertEqual(expected, actual)

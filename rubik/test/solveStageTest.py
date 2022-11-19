
from unittest import TestCase

from rubik.solveStage import SolveStage

class SolveStageTest(TestCase):
    
    ''' SolveStage -- GENERAL TESTS '''
    
    def test_solveStage_00010_ShouldHaveExactlySixItems(self):
        """ there should be only 6 solve stages """
        
        expected = 6
        actual = len(list(SolveStage))
        
        self.assertEqual(expected, actual)

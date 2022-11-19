
from unittest import TestCase

from rubik.cubeRotationDirection import CubeRotationDirection

class CubeRotationDirectionTest(TestCase):
    
    ''' CubeRotationDirection -- GENERAL TESTS '''
    
    def test_cubeRotationDirection_00010_ShouldHaveExactlySixItems(self):
        """ there should be only 6 cube rotation directions (by nature of a cube) """
        
        expected = 6
        actual = len(list(CubeRotationDirection))
        
        self.assertEqual(expected, actual)
    
    ''' CubeRotationDirection -- NEGATIVE TESTS '''
    
    def test_cubeRotationDirection_20010_ShouldThrowExceptionIfNoDirectionCodeSupplied(self):
        """ supplying no face code should result in exception """
        
        with self.assertRaises(Exception):
            CubeRotationDirection()
    
    def test_cubeRotationDirection_20020_ShouldThrowExceptionIfInvalidDirectionCodeSupplied(self):
        """ supplying invalid face code should result in exception """
        
        with self.assertRaises(Exception):
            CubeRotationDirection('T')
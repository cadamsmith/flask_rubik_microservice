
from unittest import TestCase

from rubik.cubeRotationDirection import CubeRotationDirection

class CubeRotationDirectionTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 6 cube rotation directions (by nature of a cube)
    def test_cubeRotationDirection_00010_ShouldHaveExactlySixItems(self):
        expected = 6
        actual = len(list(CubeRotationDirection))
        
        self.assertEqual(expected, actual)
        
    # NEGATIVE TESTS
    
    # supplying no face code should result in exception
    def test_cubeRotationDirection_20010_ShouldThrowExceptionIfNoDirectionCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeRotationDirection()
    
    # supplying invalid face code should result in exception
    def test_cubeRotationDirection_20020_ShouldThrowExceptionIfInvalidDirectionCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeRotationDirection('T')
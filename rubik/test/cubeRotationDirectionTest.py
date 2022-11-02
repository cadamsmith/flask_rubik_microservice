
from unittest import TestCase
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeRotationDirectionTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 4 cube rotation directions (by nature of a cube)
    def test_cubeRotationDirection_00010_ShouldHaveExactlySixItems(self):
        expected = 4
        actual = len(list(CubeRotationDirection))
        
        self.assertEqual(expected, actual)
        
    # POSITIVE TESTS
    
    # 'F' should translate to forward direction
    def test_cubeRotationDirection_10010_ShouldCorrectlyParseForwardDirectionCode(self):
        directionCode = 'F'
        
        expected = CubeRotationDirection.FORWARD
        actual = CubeRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
    # 'B' should translate to backward direction
    def test_cubeRotationDirection_10020_ShouldCorrectlyParseBackwardDirectionCode(self):
        directionCode = 'B'
        
        expected = CubeRotationDirection.BACKWARD
        actual = CubeRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
    # 'L' should translate to leftward direction
    def test_cubeRotationDirection_10030_ShouldCorrectlyParseLeftwardDirectionCode(self):
        directionCode = 'L'
        
        expected = CubeRotationDirection.LEFTWARD
        actual = CubeRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
    # 'R' should translate to rightward direction
    def test_cubeRotationDirection_10040_ShouldCorrectlyParseRightwardDirectionCode(self):
        directionCode = 'R'
        
        expected = CubeRotationDirection.RIGHTWARD
        actual = CubeRotationDirection(directionCode)
        
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
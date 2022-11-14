
from unittest import TestCase

from rubik.faceRotationDirection import FaceRotationDirection

class FaceRotationDirectionTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 2 face rotation directions (by nature of a cube face)
    def test_faceRotationDirection_00010_ShouldHaveExactlyTwoItems(self):
        expected = 2
        actual = len(list(FaceRotationDirection))
        
        self.assertEqual(expected, actual)
        
    # POSITIVE TESTS
    
    # 'CW' should translate to clockwise direction
    def test_faceRotationDirection_10010_ShouldCorrectlyParseClockwiseDirectionCode(self):
        directionCode = 'CW'
        
        expected = FaceRotationDirection.CLOCKWISE
        actual = FaceRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
    # 'CCW' should translate to counterclockwise direction
    def test_faceRotationDirection_10020_ShouldCorrectlyParseCounterClockwiseDirectionCode(self):
        directionCode = 'CCW'
        
        expected = FaceRotationDirection.COUNTERCLOCKWISE
        actual = FaceRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
        
    # NEGATIVE TESTS
    
    # supplying no face code should result in exception
    def test_faceRotationDirection_20010_ShouldThrowExceptionIfNoDirectionCodeSupplied(self):
        with self.assertRaises(Exception):
            FaceRotationDirection()
    
    # supplying invalid face code should result in exception
    def test_faceRotationDirection_20020_ShouldThrowExceptionIfInvalidDirectionCodeSupplied(self):
        with self.assertRaises(Exception):
            FaceRotationDirection('L')
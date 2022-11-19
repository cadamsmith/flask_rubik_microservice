
from unittest import TestCase

from rubik.faceRotationDirection import FaceRotationDirection

class FaceRotationDirectionTest(TestCase):
    
    ''' FaceRotationDirection -- GENERAL TESTS '''
    
    def test_faceRotationDirection_00010_ShouldHaveExactlyTwoItems(self):
        """ there should be only 2 face rotation directions (by nature of a cube face) """
        
        expected = 2
        actual = len(list(FaceRotationDirection))
        
        self.assertEqual(expected, actual)
    
    ''' FaceRotationDirection -- NEGATIVE TESTS '''
    
    def test_faceRotationDirection_10010_ShouldThrowExceptionIfNoDirectionCodeSupplied(self):
        """ supplying no face code should result in exception """
        
        with self.assertRaises(Exception):
            FaceRotationDirection()
    
    def test_faceRotationDirection_10020_ShouldThrowExceptionIfInvalidDirectionCodeSupplied(self):
        """ supplying invalid face code should result in exception """
        
        with self.assertRaises(Exception):
            FaceRotationDirection('L')
    
    ''' FaceRotationDirection -- POSITIVE TESTS '''
    
    def test_faceRotationDirection_20010_ShouldCorrectlyParseClockwiseDirectionCode(self):
        """ 'CW' should translate to clockwise direction """
        
        directionCode = 'CW'
        
        expected = FaceRotationDirection.CLOCKWISE
        actual = FaceRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
    def test_faceRotationDirection_20020_ShouldCorrectlyParseCounterClockwiseDirectionCode(self):
        """ 'CCW' should translate to counterclockwise direction """
        
        directionCode = 'CCW'
        
        expected = FaceRotationDirection.COUNTERCLOCKWISE
        actual = FaceRotationDirection(directionCode)
        
        self.assertEqual(expected, actual)
    
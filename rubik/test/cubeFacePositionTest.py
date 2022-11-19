
from unittest import TestCase

from rubik.cubeFacePosition import CubeFacePosition

class CubeFaceTest(TestCase):
    
    ''' CubeFacePosition -- GENERAL TESTS '''
    
    def test_cubeFacePosition_00010_ShouldHaveExactlySixItems(self):
        """ there should be only 6 cube face positions (by nature of a cube) """
        
        expected = 6
        actual = len(list(CubeFacePosition))
        
        self.assertEqual(expected, actual)
    
    ''' CubeFacePosition -- NEGATIVE TESTS '''
    
    def test_cubeFacePosition_10010_ShouldThrowExceptionIfNoFaceCodeSupplied(self):
        """ supplying no face code should result in exception """
        
        with self.assertRaises(Exception):
            CubeFacePosition()
    
    def test_cubeFacePosition_10020_ShouldThrowExceptionIfInvalidFaceCodeSupplied(self):
        """ supplying invalid face code should result in exception """
        
        with self.assertRaises(Exception):
            CubeFacePosition('H')
    
    ''' CubeFacePosition -- POSITIVE TESTS '''
    
    def test_cubeFacePosition_20010_ShouldCorrectlyParseFrontFaceCode(self):
        """ 'F' should translate to front face """
        
        faceCode = 'F'
        
        expected = CubeFacePosition.FRONT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeFacePosition_20020_ShouldCorrectlyParseBackFaceCode(self):
        """ 'B' should translate to back face """
        
        faceCode = 'B'
        
        expected = CubeFacePosition.BACK
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeFacePosition_20030_ShouldCorrectlyParseLeftFaceCode(self):
        """ 'L' should translate to left face """
        
        faceCode = 'L'
        
        expected = CubeFacePosition.LEFT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeFacePosition_20040_ShouldCorrectlyParseRightFaceCode(self):
        """ 'R' should translate to right face """
        
        faceCode = 'R'
        
        expected = CubeFacePosition.RIGHT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeFacePosition_20050_ShouldCorrectlyParseUpFaceCode(self):
        """ 'U' should translate to up face """
        
        faceCode = 'U'
        
        expected = CubeFacePosition.UP
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeFacePosition_20060_ShouldCorrectlyParseDownFaceCode(self):
        """ 'D' should translate to down face """
        
        faceCode = 'D'
        
        expected = CubeFacePosition.DOWN
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
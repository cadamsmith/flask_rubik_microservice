
from unittest import TestCase
from rubik.cubeFacePosition import CubeFacePosition

class CubeFaceTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 6 cube faces (by nature of a cube)
    def test_cubeFace_00010_ShouldHaveExactlySixItems(self):
        expected = 6
        actual = len(list(CubeFacePosition))
        
        self.assertEqual(expected, actual)
    
    # POSITIVE TESTS
    
    # 'F' should translate to front face
    def test_cubeFace_10010_ShouldCorrectlyParseFrontFaceCode(self):
        faceCode = 'F'
        
        expected = CubeFacePosition.FRONT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    # 'B' should translate to back face
    def test_cubeFace_10020_ShouldCorrectlyParseBackFaceCode(self):
        faceCode = 'B'
        
        expected = CubeFacePosition.BACK
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    # 'L' should translate to left face
    def test_cubeFace_10030_ShouldCorrectlyParseLeftFaceCode(self):
        faceCode = 'L'
        
        expected = CubeFacePosition.LEFT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    # 'R' should translate to right face
    def test_cubeFace_10040_ShouldCorrectlyParseRightFaceCode(self):
        faceCode = 'R'
        
        expected = CubeFacePosition.RIGHT
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    # 'U' should translate to up face
    def test_cubeFace_10050_ShouldCorrectlyParseUpFaceCode(self):
        faceCode = 'U'
        
        expected = CubeFacePosition.UP
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
    
    # 'D' should translate to down face
    def test_cubeFace_10060_ShouldCorrectlyParseDownFaceCode(self):
        faceCode = 'D'
        
        expected = CubeFacePosition.DOWN
        actual = CubeFacePosition(faceCode)
        
        self.assertEqual(expected, actual)
        
    # NEGATIVE TESTS
    
    # supplying no face code should result in exception
    def test_cubeFace_20010_ShouldThrowExceptionIfNoFaceCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeFacePosition()
    
    # supplying invalid face code should result in exception
    def test_cubeFace_20020_ShouldThrowExceptionIfInvalidFaceCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeFacePosition('H')

from unittest import TestCase

from rubik.cubeColor import CubeColor

class CubeColorTest(TestCase):
    
    ''' CubeColor -- GENERAL TESTS '''
    
    def test_cubeColor_00010_ShouldHaveExactlySixColors(self):
        """ there should be only 6 cube colors """
        
        expected = 6
        actual = len(list(CubeColor))
        
        self.assertEqual(expected, actual)
    
    ''' CubeColor -- NEGATIVE TESTS '''
    
    def test_cubeColor_10010_ShouldThrowExceptionIfNoColorCodeSupplied(self):
        """ supplying no color code should result in exception """
        
        with self.assertRaises(Exception):
            CubeColor()
    
    def test_cubeColor_10020_ShouldThrowExceptionIfInvalidColorCodeSupplied(self):
        """ supplying invalid color code should result in exception """
        
        with self.assertRaises(Exception):
            CubeColor('p')
        
    ''' CubeColor -- POSITIVE TESTS '''
    
    def test_cubeColor_20010_ShouldCorrectlyParseBlueCode(self):
        """ 'b' should translate to blue """
        
        colorCode = 'b'
        
        expected = CubeColor.BLUE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeColor_20020_ShouldCorrectlyParseRedCode(self):
        """ 'r' should translate to red """
        
        colorCode = 'r'
        
        expected = CubeColor.RED
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeColor_20030_ShouldCorrectlyParseGreenCode(self):
        """ 'g' should translate to green """
        
        colorCode = 'g'
        
        expected = CubeColor.GREEN
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeColor_20040_ShouldCorrectlyParseOrangeCode(self):
        """ 'o' should translate to orange """
        
        colorCode = 'o'
        
        expected = CubeColor.ORANGE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeColor_20050_ShouldCorrectlyParseYellowCode(self):
        """ 'y' should translate to yellow """
        
        colorCode = 'y'
        
        expected = CubeColor.YELLOW
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    def test_cubeColor_20060_ShouldCorrectlyParseWhiteCode(self):
        """ 'w' should translate to white """
        
        colorCode = 'w'
        
        expected = CubeColor.WHITE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)

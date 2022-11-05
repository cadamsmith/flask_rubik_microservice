
from unittest import TestCase
from rubik.cubeColor import CubeColor

class CubeColorTest(TestCase):
    
    # GENERAL TESTS
    
    # there should be only 7 cube colors
    def test_cubeColor_00010_ShouldHaveExactlySevenColors(self):
        expected = 7
        actual = len(list(CubeColor))
        
        self.assertEqual(expected, actual)
        
    # POSITIVE TESTS
    
    # 'b' should translate to blue
    def test_cubeColor_10010_ShouldCorrectlyParseBlueCode(self):
        colorCode = 'b'
        
        expected = CubeColor.BLUE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    # 'r' should translate to red
    def test_cubeColor_10020_ShouldCorrectlyParseRedCode(self):
        colorCode = 'r'
        
        expected = CubeColor.RED
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    # 'g' should translate to green
    def test_cubeColor_10030_ShouldCorrectlyParseGreenCode(self):
        colorCode = 'g'
        
        expected = CubeColor.GREEN
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    # 'o' should translate to orange
    def test_cubeColor_10040_ShouldCorrectlyParseOrangeCode(self):
        colorCode = 'o'
        
        expected = CubeColor.ORANGE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    # 'y' should translate to yellow
    def test_cubeColor_10050_ShouldCorrectlyParseYellowCode(self):
        colorCode = 'y'
        
        expected = CubeColor.YELLOW
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
    
    # 'w' should translate to white
    def test_cubeColor_10060_ShouldCorrectlyParseWhiteCode(self):
        colorCode = 'w'
        
        expected = CubeColor.WHITE
        actual = CubeColor(colorCode)
        
        self.assertEqual(expected, actual)
        
    # NEGATIVE TESTS
    
    # supplying no color code should result in exception
    def test_cubeColor_20010_ShouldThrowExceptionIfNoColorCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeColor()
    
    # supplying invalid color code should result in exception
    def test_cubeColor_20020_ShouldThrowExceptionIfInvalidColorCodeSupplied(self):
        with self.assertRaises(Exception):
            CubeColor('p')

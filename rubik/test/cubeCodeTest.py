
from unittest import TestCase

from rubik.cubeCode import CubeCode

class CubeCodeTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid code text provided as input, a CubeCode should be instantiated
    def test_cubeCode_init_10010_ShouldInstantiateCubeForValidCodeText(self):
        code = CubeCode('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        self.assertIsInstance(code, CubeCode)
    
    ## __init__ - NEGATIVE TESTS
    
    # supplying a non-string code text should throw exception
    def test_cubeCode_init_20010_ShouldThrowExceptionForNonStringCodeText(self):
        with self.assertRaises(Exception):
            CubeCode(2.3)
    
    # supplying no code text should throw exception
    def test_cubeCode_init_20020_ShouldThrowExceptionForNonSuppliedCodeText(self):
        with self.assertRaises(Exception):
            CubeCode()
            
    # supplying an empty code text should throw exception
    def test_cubeCode_init_20030_ShouldThrowExceptionForEmptyCodeText(self):
        with self.assertRaises(Exception):
            CubeCode('')
            
    # supplying a code text less than 54 chars long should throw exception
    def test_cubeCode_init_20040_ShouldThrowExceptionForCodeTextLessThan54CharsLong(self):
        codeText = 'orgybowrrrrygrywrgggybgrwobywoooybbrwogyggywowbwwbboy'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
            
    # supplying a code text more than 54 chars long should throw exception
    def test_cubeCode_init_20050_ShouldThrowExceptionForCodeTextMoreThan54CharsLong(self):
        codeText = 'wowbbwrybryyrrbyygowwygoobowbgrgorgwgogbryggwbyrrbwoyow'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    # supplying a code text not over the alphabet [brgoyw] should throw exception
    def test_cubeCode_init_20060_ShouldThrowExceptionForCodeTextContainingNonColorChars(self):
        codeText = 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    # supplying a code text not containing every color code should throw exception
    def test_cubeCode_init_20070_ShouldThrowExceptionForCodeTextNotContainingEveryColor(self):
        codeText = 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
            
    # supplying a code text with an uneven distribution of colors should throw exception
    def test_cubeCode_init_20080_ShouldThrowExceptionForCodeTextWithUnevenColorDistribution(self):
        codeText = 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
            
    # supplying a code text with non-unique center cubelet face colors should throw exception
    def test_cubeCode_init_20090_ShouldThrowExceptionForCodeTextWithNonUniqueCenterFaceColors(self):
        codeText = 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
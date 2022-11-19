
from unittest import TestCase

from rubik.cubeCode import CubeCode

class CubeCodeTest(TestCase):
    
    ''' CubeCode.__init__ - NEGATIVE TESTS '''
    
    def test_cubeCode_init_10010_ShouldThrowExceptionForNonStringCodeText(self):
        """ supplying a non-string code text should throw exception """
        
        with self.assertRaises(Exception):
            CubeCode(2.3)
    
    def test_cubeCode_init_10020_ShouldThrowExceptionForNonSuppliedCodeText(self):
        """ supplying no code text should throw exception """
        
        with self.assertRaises(Exception):
            CubeCode()
    
    def test_cubeCode_init_10030_ShouldThrowExceptionForEmptyCodeText(self):
        """ supplying an empty code text should throw exception """
        
        with self.assertRaises(Exception):
            CubeCode('')
    
    def test_cubeCode_init_10040_ShouldThrowExceptionForCodeTextLessThan54CharsLong(self):
        """ supplying a code text less than 54 chars long should throw exception """
        
        codeText = 'orgybowrrrrygrywrgggybgrwobywoooybbrwogyggywowbwwbboy'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    def test_cubeCode_init_10050_ShouldThrowExceptionForCodeTextMoreThan54CharsLong(self):
        """ supplying a code text more than 54 chars long should throw exception """
        
        codeText = 'wowbbwrybryyrrbyygowwygoobowbgrgorgwgogbryggwbyrrbwoyow'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    def test_cubeCode_init_10060_ShouldThrowExceptionForCodeTextContainingNonColorChars(self):
        """ supplying a code text not over the alphabet [brgoyw] should throw exception """
        
        codeText = 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    def test_cubeCode_init_10070_ShouldThrowExceptionForCodeTextNotContainingEveryColor(self):
        """ supplying a code text not containing every color code should throw exception """
        
        codeText = 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    def test_cubeCode_init_10080_ShouldThrowExceptionForCodeTextWithUnevenColorDistribution(self):
        """ supplying a code text with an uneven distribution of colors should throw exception """
        
        codeText = 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    def test_cubeCode_init_10090_ShouldThrowExceptionForCodeTextWithNonUniqueCenterFaceColors(self):
        """ supplying a code text with non-unique center cubelet face colors should throw exception """
        
        codeText = 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        
        with self.assertRaises(Exception):
            CubeCode(codeText)
    
    ''' CubeCode.__init__ -- POSITIVE TESTS '''
    
    def test_cubeCode_init_20010_ShouldInstantiateCubeForValidCodeText(self):
        """ if valid code text provided as input, a CubeCode should be instantiated """
        
        code = CubeCode('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        self.assertIsInstance(code, CubeCode)
    
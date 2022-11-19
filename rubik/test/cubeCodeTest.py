
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
    
    ''' CubeCode.isValid -- POSITIVE TESTS '''
        
    def test_cubeCode_isValid_20010_ShouldReturnFalseForNonStringCodeText(self):
        """ supplying a non-string code text should yield false """
        
        result = CubeCode.isValid(2.3)
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20020_ShouldReturnFalseForEmptyCodeText(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20030_ShouldReturnFalseForCodeTextLessThan54CharsLong(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('orgybowrrrrygrywrgggybgrwobywoooybbrwogyggywowbwwbboy')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20040_ShouldReturnFalseForCodeTextMoreThan54CharsLong(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('wowbbwrybryyrrbyygowwygoobowbgrgorgwgogbryggwbyrrbwoyow')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20050_ShouldReturnFalseForCodeTextContainingNonColorCodes(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20060_ShouldReturnFalseForCodeTextNotContainingEveryColor(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20070_ShouldReturnFalseForCodeTextWithUnevenColorDistribution(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20080_ShouldReturnFalseForCodeTextWithNonUniqueCenterFaceColors(self):
        """ supplying empty code text should yield false """
        
        result = CubeCode.isValid('gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr')
        self.assertFalse(result)
    
    def test_cubeCode_isValid_20090_ShouldReturnTrueForValidCodeText(self):
        """ supplying a valid code text should yield true """
        
        result = CubeCode.isValid('bywrborrbbrrgroygogogwgygworwogoywybwbybygybowbrowwgry')
        self.assertTrue(result)
    

from unittest import TestCase
from rubik.cube import Cube
from rubik.cubeColor import CubeColor

class CubeTest(TestCase):
    
    ## __init__ - NEGATIVE TESTS
    
    # supplying a param not a dictionary or a string should throw exception
    def test_cube_init_20010_ShouldThrowExceptionForInvalidParamType(self):
        with self.assertRaises(Exception):
            Cube(2.3)
    
    # supplying no param should throw exception
    def test_cube_init_20020_ShouldThrowExceptionForNonSuppliedParam(self):
        with self.assertRaises(Exception):
            Cube()
            
    # supplying an empty string param should throw exception
    def test_cube_init_20030_ShouldThrowExceptionForEmptyStringParam(self):
        faces = ''
        
        with self.assertRaises(Exception):
            Cube(faces)
            
    # supplying a string param less than 54 chars long should throw exception
    def test_cube_init_20040_ShouldThrowExceptionForStringParamLessThan54CharsLong(self):
        faces = 'orgybowrrrrygrywrgggybgrwobywoooybbrwogyggywowbwwbboy'
        
        with self.assertRaises(Exception):
            Cube(faces)
            
    # supplying a string param more than 54 chars long should throw exception
    def test_cube_init_20050_ShouldThrowExceptionForStringParamMoreThan54CharsLong(self):
        faces = 'wowbbwrybryyrrbyygowwygoobowbgrgorgwgogbryggwbyrrbwoyow'
        
        with self.assertRaises(Exception):
            Cube(faces)
    
    # supplying a string param not over the alphabet [brgoyw] should throw exception
    def test_cube_init_20060_ShouldThrowExceptionForStringParamContainingNonColorChars(self):
        faces = 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        
        with self.assertRaises(Exception):
            Cube(faces)
    
    # supplying a string param not containing every color code should throw exception
    def test_cube_init_20070_ShouldThrowExceptionForStringParamNotContainingEveryColor(self):
        faces = 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        
        with self.assertRaises(Exception):
            Cube(faces)
            
    # supplying a string param with an uneven distribution of colors should throw exception
    def test_cube_init_20080_ShouldThrowExceptionForStringParamWithUnevenColorDistribution(self):
        faces = 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        
        with self.assertRaises(Exception):
            Cube(faces)
            
    # supplying a string param with non-unique center cubelet face colors should throw exception
    def test_cube_init_20090_ShouldThrowExceptionForStringParamWithNonUniqueCenterFaceColors(self):
        faces = 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        
        with self.assertRaises(Exception):
            Cube(faces)
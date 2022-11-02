
from unittest import TestCase
from rubik.cube import Cube

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
            
    # supplying an string param less than 54 chars long should throw exception
    def test_cube_init_20040_ShouldThrowExceptionForStringParamLessThan54CharsLong(self):
        faces = 'orgybowrrrrygrywrgggybgrwobywoooybbrwogyggywowbwwbboy'
        
        with self.assertRaises(Exception):
            Cube(faces)
            
    # supplying an string param more than 54 chars long should throw exception
    def test_cube_init_20050_ShouldThrowExceptionForStringParamMoreThan54CharsLong(self):
        faces = 'wowbbwrybryyrrbyygowwygoobowbgrgorgwgogbryggwbyrrbwoyow'
        
        with self.assertRaises(Exception):
            Cube(faces)

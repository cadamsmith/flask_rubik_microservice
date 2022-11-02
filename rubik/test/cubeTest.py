
import itertools
from unittest import TestCase
from rubik.cube import Cube
from rubik.cubelet import Cubelet

class CubeTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid cubelet faces are provided as input, a cube should be instantiated
    def test_cube_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        cube = Cube('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        self.assertIsInstance(cube, Cube)
    
    # if valid cubelet faces are provided as input, the NxNxN cube should have all N^3 cubelets present
    def test_cube_init_10020_ShouldHaveAllCubeletsToFillCube(self):
        
        cube = Cube('obwgbrbyorgryrwgrrggwbgygrbbywboooorowyoyrgobygywwbyww')
        
        for i, j, k in itertools.product(*[range(Cube.SIZE)] * 3):
            cubelet = cube.cubelets[i, j, k]
            self.assertIsInstance(cubelet, Cubelet)
    
    ## __init__ - NEGATIVE TESTS
    
    # supplying a non-string param should throw exception
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
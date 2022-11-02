
import itertools
from unittest import TestCase
from rubik.cube import Cube
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode

class CubeTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid cubelet faces are provided as input, a cube should be instantiated
    def test_cube_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        
        code = CubeCode('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        
        cube = Cube(code)
        self.assertIsInstance(cube, Cube)
    
    # if valid cubelet faces are provided as input, the NxNxN cube should have all N^3 cubelets present
    def test_cube_init_10020_ShouldHaveAllCubeletsToFillCube(self):
        
        code = CubeCode('obwgbrbyorgryrwgrrggwbgygrbbywboooorowyoyrgobygywwbyww')
        
        cube = Cube(code)
        for i, j, k in itertools.product(*[range(code.CUBE_WIDTH)] * 3):
            cubelet = cube.cubelets[i, j, k]
            self.assertIsInstance(cubelet, Cubelet)
    
    # solved cube should have all cublets setup correctly
    def test_cube_init_10030_ShouldSetupSolvedCubeCorrectly(self):
        
        code = CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        cube = Cube(code)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, code.text)
        
    # solved cube should have all cublets setup correctly
    def test_cube_init_10040_ShouldSetupUnsolvedCubeCorrectly(self):
        
        code = CubeCode('bwgbbgrgoybwrrbgybbygwggyoowyryooywwoooryrwrrgoygwbbwr')
        cube = Cube(code)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, code.text)
        
    # solved cube should have all cublets setup correctly
    def test_cube_init_10040_ShouldSetupAnotherUnsolvedCubeCorrectly(self):
        
        code = CubeCode('gybwbrwgwrgbbryoyrwbrbgrygbwwygorobogwroyyooygwbowryog')
        cube = Cube(code)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, code.text)
    
    ## __init__ - NEGATIVE TESTS
    
    # supplying invalid cube code should throw exception
    def test_cube_init_20010_ShouldThrowExceptionForInvalidCubeCode(self):
        with self.assertRaises(Exception):
            Cube(2.3)
    
    # supplying no cube code should throw exception
    def test_cube_init_20020_ShouldThrowExceptionForNonSuppliedCubeCode(self):
        with self.assertRaises(Exception):
            Cube()
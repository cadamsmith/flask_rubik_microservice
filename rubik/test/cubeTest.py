
import itertools
from unittest import TestCase
from rubik.cube import Cube
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid cubelet faces are provided as input, a cube should be instantiated
    def test_cube_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        
        cube = Cube(CubeCode('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg'))
        self.assertIsInstance(cube, Cube)
    
    # if valid cubelet faces are provided as input, the NxNxN cube should have all N^3 cubelets present
    def test_cube_init_10020_ShouldHaveAllCubeletsToFillCube(self):
        
        cube = Cube(CubeCode('obwgbrbyorgryrwgrrggwbgygrbbywboooorowyoyrgobygywwbyww'))
        
        for i, j, k in itertools.product(*[range(cube.size)] * 3):
            cubelet = cube.cubelets[i, j, k]
            self.assertIsInstance(cubelet, Cubelet)
    
    # solved cube should have all cubelets setup correctly
    def test_cube_init_10030_ShouldSetupSolvedCubeCorrectly(self):
        
        code = CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        cube = Cube(code)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, code.text)
        
    # solved cube should have all cubelets setup correctly
    def test_cube_init_10040_ShouldSetupUnsolvedCubeCorrectly(self):
        
        code = CubeCode('bwgbbgrgoybwrrbgybbygwggyoowyryooywwoooryrwrrgoygwbbwr')
        cube = Cube(code)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, code.text)
        
    # solved cube should have all cubelets setup correctly
    def test_cube_init_10050_ShouldSetupAnotherUnsolvedCubeCorrectly(self):
        
        code = CubeCode('bbrybggbrbwrrrbgooyyoygwborgborooyrowgbrygyowywwywwggw')
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
            
    ## rotate - NEGATIVE TESTS
    
    # supplying neither cube face position or face rotation direction should throw exception
    def test_cube_rotateFace_20010_ShouldThrowExceptionForNonSuppliedParams(self):
        
        cube = Cube(CubeCode('bbrybggbrbwrrrbgooyyoygwborgborooyrowgbrygyowywwywwggw'))
        
        with self.assertRaises(Exception):
            cube.rotateFace()
    
    # supplying only cube face position should throw exception
    def test_cube_rotateFace_20020_ShouldThrowExceptionForOnlyCubeFacePositionSupplied(self):
        
        cube = Cube(CubeCode('yygrbwowbwrrgrbryoyrgogwgrwyoboowrywrgbgyyobobbwowggby'))
        
        with self.assertRaises(Exception):
            cube.rotateFace(CubeFacePosition.DOWN)
            
    # supplying only face rotation direction should throw exception
    def test_cube_rotateFace_20030_ShouldThrowExceptionForOnlyFaceRotationDirectionSupplied(self):
        
        cube = Cube(CubeCode('yygbbowwyrwbgrroyrwrgbgrbooyobgoybyorwrwygoowgbgrwgwby'))
        
        with self.assertRaises(Exception):
            cube.rotateFace(FaceRotationDirection.CLOCKWISE)
            
    # supplying invalid cube face position should throw exception
    def test_cube_rotateFace_20040_ShouldThrowExceptionForInvalidCubeFacePosition(self):
        
        cube = Cube(CubeCode('gwwwboryrgrygrrybrobwygybybogyooowgbgwbryborrwbgwwoogy'))
        
        with self.assertRaises(Exception):
            cube.rotateFace("DOWN", FaceRotationDirection.COUNTERCLOCKWISE)
            
    # supplying invalid face rotation direction should throw exception
    def test_cube_rotateFace_20050_ShouldThrowExceptionForInvalidFaceRotationDirection(self):
        
        cube = Cube(CubeCode('orywbwwgrgorrrgwoyybyygrbyorbbyobwwggrboyywgorobgwwgbo'))
        
        with self.assertRaises(Exception):
            cube.rotateFace(CubeFacePosition.RIGHT, False)
        
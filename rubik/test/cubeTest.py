
import itertools
from unittest import TestCase

from rubik.cube import Cube
from rubik.cubelet import Cubelet
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeTest(TestCase):
    
    ''' Cube.__init__ - POSITIVE TESTS '''
    
    def test_cube_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        """ if valid cubelet faces are provided as input, a cube should be instantiated """
        
        cube = Cube('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        self.assertIsInstance(cube, Cube)
    
    def test_cube_init_10020_ShouldHaveAllCubeletsToFillCube(self):
        """ if valid cubelet faces are provided as input, the NxNxN cube should have all N^3 cubelets present """
        
        cube = Cube('obwgbrbyorgryrwgrrggwbgygrbbywboooorowyoyrgobygywwbyww')
        
        for i, j, k in itertools.product(*[range(cube.WIDTH)] * cube.DIM):
            cubelet = cube.cubelets[i, j, k]
            self.assertIsInstance(cubelet, Cubelet)
    
    def test_cube_init_10030_ShouldSetupSolvedCubeCorrectly(self):
        """ solved cube should have all cubelets setup correctly """
        
        code = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cube = Cube(code)
        
        self.assertEqual(code, cube.toCode())
    
    def test_cube_init_10040_ShouldSetupUnsolvedCubeCorrectly(self):
        """ unsolved cube should have all cubelets setup correctly """
        
        code = 'bwgbbgrgoybwrrbgybbygwggyoowyryooywwoooryrwrrgoygwbbwr'
        cube = Cube(code)
        
        self.assertEqual(cube.toCode(), code)
    
    def test_cube_init_10050_ShouldSetupAnotherUnsolvedCubeCorrectly(self):
        """ another unsolved cube should have all cubelets setup correctly """
        
        code = 'bbrybggbrbwrrrbgooyyoygwborgborooyrowgbrygyowywwywwggw'
        cube = Cube(code)
        
        self.assertEqual(cube.toCode(), code)
    
    ''' Cube.__init__ - NEGATIVE TESTS '''
    
    def test_cube_init_20010_ShouldThrowExceptionForInvalidCubeCode(self):
        """ supplying invalid cube code should throw exception """
        
        with self.assertRaises(Exception):
            Cube(2.3)
    
    def test_cube_init_20020_ShouldThrowExceptionForNonSuppliedCubeCode(self):
        """ supplying no cube code should throw exception """
        
        with self.assertRaises(Exception):
            Cube()
            
    ''' Cube.rotateFace - POSITIVE TESTS '''
    
    def test_cube_rotateFace_10010_ShouldBeUnchangedAfterTwoRotationsForSameFaceButAlternatingDirections(self):
        """ rotating same face twice, but in alternating directions should result in unchanged cube """
        
        code = 'rybybrygyoyrbrwrrygggogybggwbwrobwogorywyobgwowbbwwroo'
        
        cube = Cube(code)
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        self.assertEqual(cube.toCode(), code)
    
    def test_cube_rotateFace_10020_ShouldBeUnchangedAfterFourIdenticalRotations(self):
        """ rotating same face in same direction 4 times should result in unchanged cube """
        
        code = 'wrbbbwyyrywbbrgwywobrwggggggorooryrbyowwyrgyorbbgwooyo'
        cube = Cube(code)
        
        numRotations = 4
        for _ in range(numRotations):
            cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        
        self.assertEqual(cube.toCode(), code)
    
    def test_cube_rotateFace_10030_ShouldHaveUncoloredCenterCubeletAfterFrontClockwiseRotation(self):
        """ rotating front face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10031_ShouldHaveUncoloredCenterCubeletAfterBackClockwiseRotation(self):
        """ rotating back face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10032_ShouldHaveUncoloredCenterCubeletAfterLeftClockwiseRotation(self):
        """ rotating left face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10033_ShouldHaveUncoloredCenterCubeletAfterRightClockwiseRotation(self):
        """ rotating right face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10034_ShouldHaveUncoloredCenterCubeletAfterUpClockwiseRotation(self):
        """ rotating up face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10035_ShouldHaveUncoloredCenterCubeletAfterDownClockwiseRotation(self):
        """ rotating down face clockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10040_ShouldHaveUncoloredCenterCubeletAfterFrontCounterclockwiseRotation(self):
        """ rotating front face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10041_ShouldHaveUncoloredCenterCubeletAfterBackCounterclockwiseRotation(self):
        """ rotating back face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10042_ShouldHaveUncoloredCenterCubeletAfterLeftCounterclockwiseRotation(self):
        """ rotating left face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10043_ShouldHaveUncoloredCenterCubeletAfterRightCounterclockwiseRotation(self):
        """ rotating right face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10044_ShouldHaveUncoloredCenterCubeletAfterUpClockwiseRotation(self):
        """ rotating up face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10045_ShouldHaveUncoloredCenterCubeletAfterDownClockwiseRotation(self):
        """ rotating down face counterclockwise should result in uncolored center cubelet """
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10050_ShouldHaveUncoloredFaceCenterCubeletsAfterFrontClockwiseRotation(self):
        """ rotating front face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10051_ShouldHaveUncoloredFaceCenterCubeletsAfterBackClockwiseRotation(self):
        """ rotating back face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10052_ShouldHaveUncoloredFaceCenterCubeletsAfterLeftClockwiseRotation(self):
        """ rotating left face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10053_ShouldHaveUncoloredFaceCenterCubeletsAfterRightClockwiseRotation(self):
        """ rotating right face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10054_ShouldHaveUncoloredFaceCenterCubeletsAfterUpClockwiseRotation(self):
        """ rotating up face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10055_ShouldHaveUncoloredFaceCenterCubeletsAfterDownClockwiseRotation(self):
        """ rotating down face clockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10060_ShouldHaveUncoloredFaceCenterCubeletsAfterFrontCounterclockwiseRotation(self):
        """ rotating front face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10061_ShouldHaveUncoloredFaceCenterCubeletsAfterBackCounterclockwiseRotation(self):
        """ rotating back face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10062_ShouldHaveUncoloredFaceCenterCubeletsAfterLeftCounterclockwiseRotation(self):
        """ rotating left face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10063_ShouldHaveUncoloredFaceCenterCubeletsAfterRightCounterclockwiseRotation(self):
        """ rotating right face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10064_ShouldHaveUncoloredFaceCenterCubeletsAfterUpClockwiseRotation(self):
        """ rotating up face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10065_ShouldHaveUncoloredFaceCenterCubeletsAfterDownClockwiseRotation(self):
        """ rotating down face counterclockwise should result in unchanged face center cubelets """
        
        cube = Cube('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw')
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    def test_cube_rotateFace_10070_ShouldFrontClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube front clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10071_ShouldBackClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube back clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10072_ShouldLeftClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube left clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10073_ShouldRightClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube right clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10074_ShouldUpClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube up clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10075_ShouldDownClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube down clockwise should work correctly """
        
        cube = Cube('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expected = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10080_ShouldFrontClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube front clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'wbwgbwggyroobrorbybooggwgywggrroyorowyyrywgybywbbwobrr'
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10081_ShouldBackClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube back clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'wwybbgwggborwrrybbggbygowwoygbyoywrgooyrywrbrryobwogro'
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10082_ShouldLeftClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube left clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'wwyrbgrggboowroybybobggbgyrorgroggybwyywywobrwyobwowrr'
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10083_ShouldRightClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube right clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'wwobbowgrywbbroyooroowgwyywggbroyorgwyyrygrbgrygbwgbrb'
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10084_ShouldUpClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube up clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'boobbgwggboowroybyggbggwgywwwyroyorgrrwbyyrwyryobwobrr'
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
    
    def test_cube_rotateFace_10085_ShouldDownClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube down clockwise should work correctly """
        
        cube = Cube('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr')
        expected = 'wwybbgorgboowrowggbooggwybyggbroygywwyyrywrbrbbrrwyroo'
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        
        self.assertEqual(cube.toCode(), expected)
            
    ''' Cube.rotateFace - NEGATIVE TESTS '''
    
    def test_cube_rotateFace_20010_ShouldThrowExceptionForNonSuppliedParams(self):
        """ supplying neither cube face position or face rotation direction should throw exception """
        
        cube = Cube('bbrybggbrbwrrrbgooyyoygwborgborooyrowgbrygyowywwywwggw')
        
        with self.assertRaises(Exception):
            cube.rotateFace()
    
    def test_cube_rotateFace_20020_ShouldThrowExceptionForOnlyCubeFacePositionSupplied(self):
        """ supplying only cube face position should throw exception """
        
        cube = Cube('yygrbwowbwrrgrbryoyrgogwgrwyoboowrywrgbgyyobobbwowggby')
        
        with self.assertRaises(Exception):
            cube.rotateFace(CubeFacePosition.DOWN)
    
    def test_cube_rotateFace_20030_ShouldThrowExceptionForOnlyFaceRotationDirectionSupplied(self):
        """ supplying only face rotation direction should throw exception """
        
        cube = Cube('yygbbowwyrwbgrroyrwrgbgrbooyobgoybyorwrwygoowgbgrwgwby')
        
        with self.assertRaises(Exception):
            cube.rotateFace(FaceRotationDirection.CLOCKWISE)
    
    def test_cube_rotateFace_20040_ShouldThrowExceptionForInvalidCubeFacePosition(self):
        """ supplying invalid cube face position should throw exception """
        
        cube = Cube('gwwwboryrgrygrrybrobwygybybogyooowgbgwbryborrwbgwwoogy')
        
        with self.assertRaises(Exception):
            cube.rotateFace("DOWN", FaceRotationDirection.COUNTERCLOCKWISE)
    
    def test_cube_rotateFace_20050_ShouldThrowExceptionForInvalidFaceRotationDirection(self):
        """ supplying invalid face rotation direction should throw exception """
        
        cube = Cube('orywbwwgrgorrrgwoyybyygrbyorbbyobwwggrboyywgorobgwwgbo')
        
        with self.assertRaises(Exception):
            cube.rotateFace(CubeFacePosition.RIGHT, False)
    
    ''' Cube.hasUpDaisy - POSITIVE TESTS '''
    
    def test_cube_hasUpDaisy_20010_ShouldReturnFalseForCubeWithoutUpDaisy(self):
        """ a cube without an up daisy should return false for hasUpDaisy query """
        
        cube = Cube('bywobwrrbgboorgwboybwyggybwooywoybgggwggyyrrryworworrb')
        self.assertFalse(cube.hasUpDaisy())
        
    def test_cube_hasUpDaisy_20020_ShouldReturnTrueForCubeWithUpDaisy(self):
        """ a cube with an up daisy should return true for hasUpDaisy query """
        
        cube = Cube('gogobooybrbyyrgyggogwogboygrrrrobygwbwbwywywwbrrrwyobw')
        self.assertTrue(cube.hasUpDaisy())
    
    ''' Cube.hasDownCross - POSITIVE TESTS '''
    
    def test_cube_hasDownCross_20010_ShouldReturnFalseForCubeWithoutDownCross(self):
        """ a cube without a down cross should return false for hasDownCross query """
        
        cube = Cube('rwbybworwrwobrogggbryygbrwrgbgoobwowogyryowgybyogwybry')
        self.assertFalse(cube.hasDownCross())
        
    def test_cube_hasDownCross_20020_ShouldReturnTrueForCubeWithDownCross(self):
        """ a cube with a down cross should return true for hasDownCross query """
        
        cube = Cube('wywobbrbgrggrrbyrgrgyogoogboyoyogyogbrwryybbbywowwwrww')
        self.assertTrue(cube.hasDownCross())
        
    ''' Cube.isDownLayerSolved - POSITIVE TESTS '''
    
    def test_cube_isDownLayerSolved_20010_ShouldReturnFalseForCubeWithUnsolvedDownLayer(self):
        """ a cube with unsolved down layer should return false for isDownLayerSolved query """
        
        cube = Cube('woggbrbygygbbrbywwywbogrbygrwrwoyoroygobyrggrwooywowbr')
        self.assertFalse(cube.isDownLayerSolved())
        
    def test_cube_isDownLayerSolved_20020_ShouldReturnTrueForCubeWithSolvedDownLayer(self):
        """ a cube with solved down layer should return true for isDownLayerSolved query """
        
        cube = Cube('gyogbobbbybrgrgrrryybrgrgggyyrboyooooobbyoyrgwwwwwwwww')
        self.assertTrue(cube.isDownLayerSolved())
        
    ''' Cube.isDownAndMiddleLayersSolved - POSITIVE TESTS '''
    
    def test_cube_isDownAndMiddleLayersSolved_20010_ShouldReturnFalseForCubeWithoutSolvedDownAndMiddleLayers(self):
        """ a cube with unsolved down or middle layers should return false for isDownAndMiddleLayersSolved query """
        
        cube = Cube('ogbbbwgbbwyooryywwbgorgoryywowbowogybyygyogrrrrrwwrgbg')
        self.assertFalse(cube.isDownAndMiddleLayersSolved())
        
    def test_cube_isDownAndMiddleLayersSolved_20020_ShouldReturnTrueForCubeWithSolvedDownAndMiddleLayers(self):
        """ a cube with solved down and middle layers should return true for isDownAndMiddleLayersSolved query """
        
        cube = Cube('ygrbbbbbbgyyrrrrrrbyoggggggbroooooooybryyogyywwwwwwwww')
        self.assertTrue(cube.isDownAndMiddleLayersSolved())
        
    ''' Cube.hasUpCross - POSITIVE TESTS '''
    
    def test_cube_hasUpCross_20010_ShouldReturnFalseForCubeWithoutUpCross(self):
        """ a cube without up cross should return false for hasUpCross query """
        
        cube = Cube('owbobyrbrybygrbbwyrwwoggoygggbooyoobrrgryrwgowyywwbwrg')
        self.assertFalse(cube.hasUpCross())
        
    def test_cube_hasUpCross_20020_ShouldReturnTrueForCubeWithUpCross(self):
        """ a cube with up cross should return true for hasUpCross query """
        
        cube = Cube('ybrbbbbbbgrorrrrrryobggggggygroooooooygyyybyywwwwwwwww')
        self.assertTrue(cube.hasUpCross())
        
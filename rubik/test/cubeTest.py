
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
            
    ## rotateFace - POSITIVE TESTS
    
    # rotating same face twice, but in alternating directions should result in unchanged cube
    def test_cube_rotateFace_10010_ShouldBeUnchangedAfterTwoRotationsForSameFaceButAlternatingDirections(self):
        
        initCode = CubeCode('rybybrygyoyrbrwrrygggogybggwbwrobwogorywyobgwowbbwwroo')
        cube = Cube(initCode)
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, initCode.text)
    
    # rotating same face in same direction 4 times should result in unchanged cube
    def test_cube_rotateFace_10020_ShouldBeUnchangedAfterFourIdenticalRotations(self):
        
        initCode = CubeCode('wrbbbwyyrywbbrgwywobrwggggggorooryrbyowwyrgyorbbgwooyo')
        cube = Cube(initCode)
        
        numRotations = 4
        for _ in range(numRotations):
            cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        
        newCode = cube.toCode()
        self.assertEqual(newCode.text, initCode.text)
    
    # rotating front face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10030_ShouldHaveUncoloredCenterCubeletAfterFrontClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating back face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10031_ShouldHaveUncoloredCenterCubeletAfterBackClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating left face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10032_ShouldHaveUncoloredCenterCubeletAfterLeftClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating right face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10033_ShouldHaveUncoloredCenterCubeletAfterRightClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating up face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10034_ShouldHaveUncoloredCenterCubeletAfterUpClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating down face clockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10035_ShouldHaveUncoloredCenterCubeletAfterDownClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating front face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10040_ShouldHaveUncoloredCenterCubeletAfterFrontCounterclockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating back face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10041_ShouldHaveUncoloredCenterCubeletAfterBackCounterclockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating left face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10042_ShouldHaveUncoloredCenterCubeletAfterLeftCounterclockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating right face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10043_ShouldHaveUncoloredCenterCubeletAfterRightCounterclockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating up face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10044_ShouldHaveUncoloredCenterCubeletAfterUpClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating down face counterclockwise should result in uncolored center cubelet
    def test_cube_rotateFace_10045_ShouldHaveUncoloredCenterCubeletAfterDownClockwiseRotation(self):
        
        expected = {cf: None for cf in CubeFacePosition}
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE)
        
        centerCoords = (1, 1, 1)
        actual = cube.cubelets[centerCoords].faces
        
        self.assertEqual(actual, expected)
        
    # rotating front face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10050_ShouldHaveUncoloredFaceCenterCubeletsAfterFrontClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating back face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10051_ShouldHaveUncoloredFaceCenterCubeletsAfterBackClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating left face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10052_ShouldHaveUncoloredFaceCenterCubeletsAfterLeftClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating right face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10053_ShouldHaveUncoloredFaceCenterCubeletsAfterRightClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating up face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10054_ShouldHaveUncoloredFaceCenterCubeletsAfterUpClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating down face clockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10055_ShouldHaveUncoloredFaceCenterCubeletsAfterDownClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating front face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10060_ShouldHaveUncoloredFaceCenterCubeletsAfterFrontCounterclockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating back face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10061_ShouldHaveUncoloredFaceCenterCubeletsAfterBackCounterclockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating left face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10062_ShouldHaveUncoloredFaceCenterCubeletsAfterLeftCounterclockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating right face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10063_ShouldHaveUncoloredFaceCenterCubeletsAfterRightCounterclockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating up face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10064_ShouldHaveUncoloredFaceCenterCubeletsAfterUpClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
        
    # rotating down face counterclockwise should result in unchanged face center cubelets
    def test_cube_rotateFace_10065_ShouldHaveUncoloredFaceCenterCubeletsAfterDownClockwiseRotation(self):
        
        cube = Cube(CubeCode('obbwbrwoworygrogyrgyyggygyrrwyoobbgrggooywbrwbbowwrybw'))
        expected = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.COUNTERCLOCKWISE)
        actual = list(map(lambda coord : cube.cubelets[coord], cube.FACE_CENTER_CUBELET_COORDS.values()))
        
        self.assertEqual(actual, expected)
    
    # rotating a solved cube front clockwise should work correctly
    def test_cube_rotateFace_10070_ShouldFrontClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
    
    # rotating a solved cube back clockwise should work correctly
    def test_cube_rotateFace_10071_ShouldBackClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a solved cube left clockwise should work correctly
    def test_cube_rotateFace_10072_ShouldLeftClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a solved cube right clockwise should work correctly
    def test_cube_rotateFace_10073_ShouldRightClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a solved cube up clockwise should work correctly
    def test_cube_rotateFace_10074_ShouldUpClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a solved cube down clockwise should work correctly
    def test_cube_rotateFace_10075_ShouldDownClockwiseRotateSolvedCubeCorrectly(self):
        
        cube = Cube(CubeCode('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'))
        expected = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a random cube front clockwise should work correctly
    def test_cube_rotateFace_10080_ShouldFrontClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'wbwgbwggyroobrorbybooggwgywggrroyorowyyrywgybywbbwobrr'
        
        cube.rotateFace(CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
    
    # rotating a random cube back clockwise should work correctly
    def test_cube_rotateFace_10081_ShouldBackClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'wwybbgwggborwrrybbggbygowwoygbyoywrgooyrywrbrryobwogro'
        
        cube.rotateFace(CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a random cube left clockwise should work correctly
    def test_cube_rotateFace_10082_ShouldLeftClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'wwyrbgrggboowroybybobggbgyrorgroggybwyywywobrwyobwowrr'
        
        cube.rotateFace(CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a random cube right clockwise should work correctly
    def test_cube_rotateFace_10083_ShouldRightClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'wwobbowgrywbbroyooroowgwyywggbroyorgwyyrygrbgrygbwgbrb'
        
        cube.rotateFace(CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a random cube up clockwise should work correctly
    def test_cube_rotateFace_10084_ShouldUpClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'boobbgwggboowroybyggbggwgywwwyroyorgrrwbyyrwyryobwobrr'
        
        cube.rotateFace(CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
        
    # rotating a random cube down clockwise should work correctly
    def test_cube_rotateFace_10085_ShouldDownClockwiseRotateRandomCubeCorrectly(self):
        
        cube = Cube(CubeCode('wwybbgwggboowroybybooggwgywggbroyorgwyyrywrbrryobwobrr'))
        expected = 'wwybbgorgboowrowggbooggwybyggbroygywwyyrywrbrbbrrwyroo'
        
        cube.rotateFace(CubeFacePosition.DOWN, FaceRotationDirection.CLOCKWISE)
        actual = cube.toCode().text
        
        self.assertEqual(actual, expected)
            
    ## rotateFace - NEGATIVE TESTS
    
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
        
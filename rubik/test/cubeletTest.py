
from unittest import TestCase
from rubik.cubelet import Cubelet
from rubik.cubeColor import CubeColor
from rubik.cubeFace import CubeFace
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeletTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid cube faces are provided as input, a cube should be instantiated
    def test_cubelet_init_10010_ShouldInstantiateCubeForValidInput(self):
    
        faces = {
            CubeFace.UP: CubeColor.RED,
            CubeFace.FRONT: CubeColor.BLUE,
            CubeFace.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        self.assertIsInstance(cubelet, Cubelet)
    
    # instantiating with no supplied param faces should create uncolored cubelet
    def test_cubelet_init_10020_ShouldCreateUncoloredCubeletForUnsuppliedParam(self):
        
        cubelet = Cubelet()
        
        # see if all faces are non-colored
        for face in list(CubeFace):
            expected = None
            actual = cubelet.faces[face]
            
            self.assertEqual(actual, expected)
    
    # instantiating with empty param faces should create uncolored cubelet
    def test_cubelet_init_10030_ShouldCreateUncoloredCubeletForEmptyDictParam(self):
        
        cubelet = Cubelet({})
        
        # see if all faces are non-colored
        for face in list(CubeFace):
            expected = None
            actual = cubelet.faces[face]
            
            self.assertEqual(actual, expected)
    
    # front face should be colored correctly if supplied in param faces
    def test_cubelet_init_10040_ShouldColorFrontFaceIfSupplied(self):
        
        faces = {
            CubeFace.FRONT : CubeColor.GREEN
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.GREEN
        actual = cubelet.faces[CubeFace.FRONT]
        
        self.assertEqual(actual, expected)
    
    # back face should be colored correctly if supplied in param faces
    def test_cubelet_init_10050_ShouldColorBackFaceIfSupplied(self):
        
        faces = {
            CubeFace.BACK : CubeColor.RED
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.RED
        actual = cubelet.faces[CubeFace.BACK]
        
        self.assertEqual(actual, expected)
    
    # left face should be colored correctly if supplied in param faces
    def test_cubelet_init_10060_ShouldColorLeftFaceIfSupplied(self):
        
        faces = {
            CubeFace.LEFT : CubeColor.YELLOW
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.YELLOW
        actual = cubelet.faces[CubeFace.LEFT]
        
        self.assertEqual(actual, expected)
    
    # right face should be colored correctly if supplied in param faces
    def test_cubelet_init_10070_ShouldColorRightFaceIfSupplied(self):
        
        faces = {
            CubeFace.RIGHT : CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.WHITE
        actual = cubelet.faces[CubeFace.RIGHT]
        
        self.assertEqual(actual, expected)
    
    # up face should be colored correctly if supplied in param faces
    def test_cubelet_init_10080_ShouldColorUpFaceIfSupplied(self):
        
        faces = {
            CubeFace.UP : CubeColor.BLUE
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.BLUE
        actual = cubelet.faces[CubeFace.UP]
        
        self.assertEqual(actual, expected)
    
    # down face should be colored correctly if supplied in param faces
    def test_cubelet_init_10090_ShouldColorDownFaceIfSupplied(self):
        
        faces = {
            CubeFace.DOWN : CubeColor.ORANGE
        }
        
        cubelet = Cubelet(faces)
        
        expected = CubeColor.ORANGE
        actual = cubelet.faces[CubeFace.DOWN]
        
        self.assertEqual(actual, expected)
        
    # front face should not be colored if not supplied in param faces
    def test_cubelet_init_10100_ShouldNotColorFrontFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.UP : CubeColor.BLUE,
            CubeFace.LEFT : CubeColor.YELLOW
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.FRONT]
        
        self.assertEqual(actual, expected)
    
    # back face should not be colored if not supplied in param faces
    def test_cubelet_init_10110_ShouldNotColorBackFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.UP : CubeColor.BLUE,
            CubeFace.LEFT : CubeColor.YELLOW
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.BACK]
        
        self.assertEqual(actual, expected)
    
    # left face should not be colored if not supplied in param faces
    def test_cubelet_init_10120_ShouldNotColorLeftFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.RIGHT : CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.LEFT]
        
        self.assertEqual(actual, expected)
    
    # right face should not be colored if not supplied in param faces
    def test_cubelet_init_10130_ShouldNotColorRightFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.LEFT : CubeColor.ORANGE
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.RIGHT]
        
        self.assertEqual(actual, expected)
    
    # up face should not be colored if not supplied in param faces
    def test_cubelet_init_10140_ShouldNotColorUpFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.RIGHT : CubeColor.GREEN
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.UP]
        
        self.assertEqual(actual, expected)
    
    # down face should not be colored if not supplied in param faces
    def test_cubelet_init_10150_ShouldNotColorDownFaceIfNotSupplied(self):
        
        faces = {
            CubeFace.UP: CubeColor.RED,
            CubeFace.FRONT: CubeColor.BLUE,
            CubeFace.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        
        expected = None
        actual = cubelet.faces[CubeFace.DOWN]
        
        self.assertEqual(actual, expected)
    
    # more than one face should be able to be colored
    def test_cubelet_init_10160_ShouldSetColorFacesCorrectly(self):
        
        faces = {
            CubeFace.DOWN: CubeColor.WHITE,
            CubeFace.RIGHT: CubeColor.BLUE,
            CubeFace.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        
        # see if all 3 faces were colored correctly
        for face, color in faces.items():
            actual = cubelet.faces[face]
            self.assertEqual(actual, color)
        
    ## __init__ - NEGATIVE TESTS
    
    # supplying a dictionary with non-CubeFace keys should throw exception
    def test_cubelet_init_20010_ShouldThrowExceptionForInvalidParamKeys(self):
        
        faces = {
            1: CubeColor.GREEN,
            True: CubeColor.WHITE
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
            
    # supplying a dictionary with non-CubeColor values should throw exception
    def test_cubelet_init_20020_ShouldThrowExceptionForInvalidParamValues(self):
        
        faces = {
            CubeFace.BACK: 2.01,
            CubeFace.RIGHT: 'value'
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)

    # supplying more than 3 colored faces should throw exception
    def test_cubelet_init_20030_ShouldThrowExceptionForMoreThanThreeColoredFaces(self):
        
        faces = {
            CubeFace.UP: CubeColor.RED,
            CubeFace.DOWN: CubeColor.RED,
            CubeFace.LEFT: CubeColor.RED,
            CubeFace.RIGHT: CubeColor.RED
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
            
    ## rotate - POSITIVE TESTS
    
    # a normal cubelet should rotate forward correctly
    def test_cubelet_rotate_10010_ShouldRotateForwardCorrectly(self):
        
        faces = {
            CubeFace.UP: CubeColor.BLUE,
            CubeFace.FRONT: CubeColor.ORANGE,
            CubeFace.RIGHT: CubeColor.YELLOW
        }
        
        cubelet = Cubelet(faces)
        cubelet.rotate(CubeRotationDirection.FORWARD)
        
        for face in list(CubeFace):
            expectedColor = None
            
            if face is CubeFace.FRONT:
                expectedColor = CubeColor.BLUE
            elif face is CubeFace.DOWN:
                expectedColor = CubeColor.ORANGE
            elif face is CubeFace.RIGHT:
                expectedColor = CubeColor.YELLOW
                
            actualColor = cubelet.faces[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should rotate backward correctly
    def test_cubelet_rotate_10020_ShouldRotateBackwardCorrectly(self):
        
        faces = {
            CubeFace.UP: CubeColor.ORANGE
        }
        
        cubelet = Cubelet(faces)
        cubelet.rotate(CubeRotationDirection.BACKWARD)
        
        for face in list(CubeFace):
            expectedColor = None
            
            if face is CubeFace.BACK:
                expectedColor = CubeColor.ORANGE
                
            actualColor = cubelet.faces[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should rotate leftward correctly
    def test_cubelet_rotate_10030_ShouldRotateLeftwardCorrectly(self):
        
        faces = {
            CubeFace.LEFT: CubeColor.ORANGE,
            CubeFace.FRONT: CubeColor.GREEN,
            CubeFace.DOWN: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        cubelet.rotate(CubeRotationDirection.LEFTWARD)
        
        for face in list(CubeFace):
            expectedColor = None
            
            if face is CubeFace.FRONT:
                expectedColor = CubeColor.GREEN
            elif face is CubeFace.DOWN:
                expectedColor = CubeColor.ORANGE
            elif face is CubeFace.RIGHT:
                expectedColor = CubeColor.WHITE
                
            actualColor = cubelet.faces[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should rotate rightward correctly
    def test_cubelet_rotate_10040_ShouldRotateRightwardCorrectly(self):
        
        faces = {
            CubeFace.FRONT: CubeColor.RED,
            CubeFace.DOWN: CubeColor.BLUE
        }
        
        cubelet = Cubelet(faces)
        cubelet.rotate(CubeRotationDirection.RIGHTWARD)
        
        for face in list(CubeFace):
            expectedColor = None
            
            if face is CubeFace.FRONT:
                expectedColor = CubeColor.RED
            elif face is CubeFace.LEFT:
                expectedColor = CubeColor.BLUE
                
            actualColor = cubelet.faces[face]
            self.assertEqual(actualColor, expectedColor)
    
    # a cubelet with only left face colored should not be affected by forward rotation
    def test_cubelet_rotate_10050_ShouldNotChangeCubeletWithOnlyLeftColoredOnForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.LEFT: CubeColor.WHITE
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.FORWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only left face colored should not be affected by backward rotation
    def test_cubelet_rotate_10060_ShouldNotChangeCubeletWithOnlyLeftColoredOnBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.LEFT: CubeColor.GREEN
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.BACKWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only right face colored should not be affected by forward rotation
    def test_cubelet_rotate_10070_ShouldNotChangeCubeletWithOnlyRightColoredOnForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.RIGHT: CubeColor.RED
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.FORWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only right face colored should not be affected by backward rotation
    def test_cubelet_rotate_10080_ShouldNotChangeCubeletWithOnlyRightColoredOnBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.RIGHT: CubeColor.ORANGE
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.BACKWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only up face colored should not be affected by leftward rotation
    def test_cubelet_rotate_10090_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnLeftwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.UP: CubeColor.RED
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.LEFTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only up face colored should not be affected by rightward rotation
    def test_cubelet_rotate_10100_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.UP: CubeColor.BLUE
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.RIGHTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only down face colored should not be affected by leftward rotation
    def test_cubelet_rotate_10110_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnLeftwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.DOWN: CubeColor.YELLOW
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.LEFTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only down face colored should not be affected by rightward rotation
    def test_cubelet_rotate_10120_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.DOWN: CubeColor.GREEN
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.RIGHTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a forward rotation followed by a backward rotation
    def test_cubelet_rotate_10130_ShouldNotChangeCubeletOnForwardThenBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.UP: CubeColor.YELLOW,
            CubeFace.FRONT: CubeColor.GREEN,
            CubeFace.RIGHT: CubeColor.RED
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.FORWARD)
        cubelet.rotate(CubeRotationDirection.BACKWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    # a cubelet should end up unchanged by a backward rotation followed by a forward rotation
    def test_cubelet_rotate_10140_ShouldNotChangeCubeletOnBackwardThenForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.LEFT: CubeColor.WHITE,
            CubeFace.FRONT: CubeColor.ORANGE
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.BACKWARD)
        cubelet.rotate(CubeRotationDirection.FORWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a leftward rotation followed by a rightward rotation
    def test_cubelet_rotate_10150_ShouldNotChangeCubeletOnLeftwardThenRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFace.RIGHT: CubeColor.RED,
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.LEFTWARD)
        cubelet.rotate(CubeRotationDirection.RIGHTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a rightward rotation followed by a leftward rotation
    def test_cubelet_rotate_10160_ShouldNotChangeCubeletOnRightwardThenLeftawrdRotation(self):
        
        cubelet = Cubelet({
            CubeFace.LEFT: CubeColor.BLUE,
            CubeFace.FRONT: CubeColor.RED,
            CubeFace.DOWN: CubeColor.YELLOW
        })
        
        oldFaces = cubelet.faces
        cubelet.rotate(CubeRotationDirection.RIGHTWARD)
        cubelet.rotate(CubeRotationDirection.LEFTWARD)
        
        for face in list(CubeFace):
            expectedColor = oldFaces[face]
            actualColor = cubelet.faces[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    ## rotate - NEGATIVE TESTS
    
    # supplying no direction param should throw exception
    def test_cubelet_rotate_20010_ShouldThrowExceptionForNonSuppliedDirectionParam(self):
        
        faces = {
            CubeFace.UP : CubeColor.BLUE
        }
        
        cubelet = Cubelet(faces)
        
        with self.assertRaises(Exception):
            cubelet.rotate()
    
    # supplying non-CubeRotationDirection param should throw exception
    def test_cubelet_rotate_20020_ShouldThrowExceptionForInvalidDirectionParam(self):
        
        faces = {
            CubeFace.UP : CubeColor.BLUE
        }
        
        cubelet = Cubelet(faces)
        
        with self.assertRaises(Exception):
            cubelet.rotate(2.46)

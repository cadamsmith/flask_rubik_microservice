
from unittest import TestCase

from rubik.cubelet import Cubelet
from rubik.cubeColor import CubeColor
from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeletTest(TestCase):
    
    ## __init__ - POSITIVE TESTS
    
    # if valid cube faces are provided as input, a cube should be instantiated
    def test_cubelet_init_10010_ShouldInstantiateCubeletForValidInput(self):
    
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.FRONT: CubeColor.BLUE,
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        self.assertIsInstance(cubelet, Cubelet)
    
    # instantiating with no supplied param faces should create uncolored cubelet
    def test_cubelet_init_10020_ShouldCreateUncoloredCubeletForUnsuppliedParam(self):
        
        cubelet = Cubelet()
        
        # see if all faces are non-colored
        for face in list(CubeFacePosition):
            expected = None
            actual = cubelet[face]
            
            self.assertEqual(actual, expected)
    
    # instantiating with empty param faces should create uncolored cubelet
    def test_cubelet_init_10030_ShouldCreateUncoloredCubeletForEmptyDictParam(self):
        
        cubelet = Cubelet({})
        
        # see if all faces are non-colored
        for face in list(CubeFacePosition):
            expected = None
            actual = cubelet[face]
            
            self.assertEqual(actual, expected)
    
    # front face should be colored correctly if supplied in param faces
    def test_cubelet_init_10040_ShouldColorFrontFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.FRONT : CubeColor.GREEN
        })
        
        expected = CubeColor.GREEN
        actual = cubelet[CubeFacePosition.FRONT]
        
        self.assertEqual(actual, expected)
    
    # back face should be colored correctly if supplied in param faces
    def test_cubelet_init_10050_ShouldColorBackFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.BACK : CubeColor.RED
        })
        
        expected = CubeColor.RED
        actual = cubelet[CubeFacePosition.BACK]
        
        self.assertEqual(actual, expected)
    
    # left face should be colored correctly if supplied in param faces
    def test_cubelet_init_10060_ShouldColorLeftFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = CubeColor.YELLOW
        actual = cubelet[CubeFacePosition.LEFT]
        
        self.assertEqual(actual, expected)
    
    # right face should be colored correctly if supplied in param faces
    def test_cubelet_init_10070_ShouldColorRightFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.WHITE
        })
        
        expected = CubeColor.WHITE
        actual = cubelet[CubeFacePosition.RIGHT]
        
        self.assertEqual(actual, expected)
    
    # up face should be colored correctly if supplied in param faces
    def test_cubelet_init_10080_ShouldColorUpFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        expected = CubeColor.BLUE
        actual = cubelet[CubeFacePosition.UP]
        
        self.assertEqual(actual, expected)
    
    # down face should be colored correctly if supplied in param faces
    def test_cubelet_init_10090_ShouldColorDownFaceIfSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN : CubeColor.ORANGE
        })
        
        expected = CubeColor.ORANGE
        actual = cubelet[CubeFacePosition.DOWN]
        
        self.assertEqual(actual, expected)
        
    # front face should not be colored if not supplied in param faces
    def test_cubelet_init_10100_ShouldNotColorFrontFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE,
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.FRONT]
        
        self.assertEqual(actual, expected)
    
    # back face should not be colored if not supplied in param faces
    def test_cubelet_init_10110_ShouldNotColorBackFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE,
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.BACK]
        
        self.assertEqual(actual, expected)
    
    # left face should not be colored if not supplied in param faces
    def test_cubelet_init_10120_ShouldNotColorLeftFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.WHITE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.LEFT]
        
        self.assertEqual(actual, expected)
    
    # right face should not be colored if not supplied in param faces
    def test_cubelet_init_10130_ShouldNotColorRightFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT : CubeColor.ORANGE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.RIGHT]
        
        self.assertEqual(actual, expected)
    
    # up face should not be colored if not supplied in param faces
    def test_cubelet_init_10140_ShouldNotColorUpFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.GREEN
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.UP]
        
        self.assertEqual(actual, expected)
    
    # down face should not be colored if not supplied in param faces
    def test_cubelet_init_10150_ShouldNotColorDownFaceIfNotSupplied(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.FRONT: CubeColor.BLUE,
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.DOWN]
        
        self.assertEqual(actual, expected)
    
    # more than one face should be able to be colored
    def test_cubelet_init_10160_ShouldSetColorFacesCorrectly(self):
        
        faces = {
            CubeFacePosition.DOWN: CubeColor.WHITE,
            CubeFacePosition.RIGHT: CubeColor.BLUE,
            CubeFacePosition.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        
        # see if all 3 faces were colored correctly
        for face, color in faces.items():
            actual = cubelet[face]
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
            CubeFacePosition.BACK: 2.01,
            CubeFacePosition.RIGHT: 'value'
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)

    # supplying more than 3 colored faces should throw exception
    def test_cubelet_init_20030_ShouldThrowExceptionForMoreThanThreeColoredFaces(self):
        
        faces = {
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.DOWN: CubeColor.RED,
            CubeFacePosition.LEFT: CubeColor.RED,
            CubeFacePosition.RIGHT: CubeColor.RED
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
            
    ## rotate - POSITIVE TESTS
    
    # a normal cubelet should flip forward correctly
    def test_cubelet_rotate_10010_ShouldFlipForwardCorrectly(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.BLUE,
            CubeFacePosition.FRONT: CubeColor.ORANGE,
            CubeFacePosition.RIGHT: CubeColor.YELLOW
        })
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = None
            
            if face is CubeFacePosition.FRONT:
                expectedColor = CubeColor.BLUE
            elif face is CubeFacePosition.DOWN:
                expectedColor = CubeColor.ORANGE
            elif face is CubeFacePosition.RIGHT:
                expectedColor = CubeColor.YELLOW
                
            actualColor = cubelet[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should flip backward correctly
    def test_cubelet_rotate_10020_ShouldFlipBackwardCorrectly(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.ORANGE
        })
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = None
            
            if face is CubeFacePosition.BACK:
                expectedColor = CubeColor.ORANGE
                
            actualColor = cubelet[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should flip leftward correctly
    def test_cubelet_rotate_10030_ShouldFlipLeftwardCorrectly(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.ORANGE,
            CubeFacePosition.FRONT: CubeColor.GREEN,
            CubeFacePosition.DOWN: CubeColor.WHITE
        })
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = None
            
            if face is CubeFacePosition.FRONT:
                expectedColor = CubeColor.GREEN
            elif face is CubeFacePosition.DOWN:
                expectedColor = CubeColor.ORANGE
            elif face is CubeFacePosition.RIGHT:
                expectedColor = CubeColor.WHITE
                
            actualColor = cubelet[face]
            self.assertEqual(actualColor, expectedColor)
            
    # a normal cubelet should flip rightward correctly
    def test_cubelet_rotate_10040_ShouldFlipRightwardCorrectly(self):
        
        cubelet = Cubelet({
            CubeFacePosition.FRONT: CubeColor.RED,
            CubeFacePosition.DOWN: CubeColor.BLUE
        })
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = None
            
            if face is CubeFacePosition.FRONT:
                expectedColor = CubeColor.RED
            elif face is CubeFacePosition.LEFT:
                expectedColor = CubeColor.BLUE
                
            actualColor = cubelet[face]
            self.assertEqual(actualColor, expectedColor)
    
    # a cubelet with only left face colored should not be affected by flip forward
    def test_cubelet_rotate_10050_ShouldNotChangeCubeletWithOnlyLeftColoredOnForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only left face colored should not be affected by flip backward
    def test_cubelet_rotate_10060_ShouldNotChangeCubeletWithOnlyLeftColoredOnBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.GREEN
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only right face colored should not be affected by flip forward
    def test_cubelet_rotate_10070_ShouldNotChangeCubeletWithOnlyRightColoredOnForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT: CubeColor.RED
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only right face colored should not be affected by flip backward
    def test_cubelet_rotate_10080_ShouldNotChangeCubeletWithOnlyRightColoredOnBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT: CubeColor.ORANGE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only up face colored should not be affected by flip leftward
    def test_cubelet_rotate_10090_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnLeftwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only up face colored should not be affected by flip rightward
    def test_cubelet_rotate_10100_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.BLUE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only down face colored should not be affected by flip leftward
    def test_cubelet_rotate_10110_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnLeftwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN: CubeColor.YELLOW
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet with only down face colored should not be affected by flip rightward
    def test_cubelet_rotate_10120_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN: CubeColor.GREEN
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a flip forward followed by a flip backward
    def test_cubelet_rotate_10130_ShouldNotChangeCubeletOnForwardThenBackwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.YELLOW,
            CubeFacePosition.FRONT: CubeColor.GREEN,
            CubeFacePosition.RIGHT: CubeColor.RED
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    # a cubelet should end up unchanged by a flip backward followed by a flip forward
    def test_cubelet_rotate_10140_ShouldNotChangeCubeletOnBackwardThenForwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.WHITE,
            CubeFacePosition.FRONT: CubeColor.ORANGE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a flip leftward followed by a flip rightward
    def test_cubelet_rotate_10150_ShouldNotChangeCubeletOnLeftwardThenRightwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT: CubeColor.RED,
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    # a cubelet should end up unchanged by a flip rightward followed by a flip leftward
    def test_cubelet_rotate_10160_ShouldNotChangeCubeletOnRightwardThenLeftwardRotation(self):
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.BLUE,
            CubeFacePosition.FRONT: CubeColor.RED,
            CubeFacePosition.DOWN: CubeColor.YELLOW
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
            
    ## rotate - NEGATIVE TESTS
    
    # supplying no direction param should throw exception
    def test_cubelet_rotate_20010_ShouldThrowExceptionForNonSuppliedDirectionParam(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        with self.assertRaises(Exception):
            cubelet.rotate()
    
    # supplying non-CubeRotationDirection param should throw exception
    def test_cubelet_rotate_20020_ShouldThrowExceptionForInvalidDirectionParam(self):
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        with self.assertRaises(Exception):
            cubelet.rotate(2.46)

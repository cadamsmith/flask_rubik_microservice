
from unittest import TestCase

from rubik.cubelet import Cubelet
from rubik.cubeColor import CubeColor
from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeRotationDirection import CubeRotationDirection

class CubeletTest(TestCase):
        
    ''' Cubelet.__init__ -- NEGATIVE TESTS '''
    
    def test_cubelet_init_10010_ShouldThrowExceptionForInvalidParamKeys(self):
        """ supplying a dictionary with non-CubeFace keys should throw exception """
        
        faces = {
            1: CubeColor.GREEN,
            True: CubeColor.WHITE
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
    
    def test_cubelet_init_10020_ShouldThrowExceptionForInvalidParamValues(self):
        """ supplying a dictionary with non-CubeColor values should throw exception """
        
        faces = {
            CubeFacePosition.BACK: 2.01,
            CubeFacePosition.RIGHT: 'value'
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
    
    def test_cubelet_init_10030_ShouldThrowExceptionForMoreThanThreeColoredFaces(self):
        """ supplying more than 3 colored faces should throw exception """
        
        faces = {
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.DOWN: CubeColor.RED,
            CubeFacePosition.LEFT: CubeColor.RED,
            CubeFacePosition.RIGHT: CubeColor.RED
        }
        
        with self.assertRaises(Exception):
            Cubelet(faces)
    
    ''' Cubelet.__init__ -- POSITIVE TESTS '''
    
    def test_cubelet_init_20010_ShouldInstantiateCubeletForValidInput(self):
        """ if valid cube faces are provided as input, a cube should be instantiated """
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.FRONT: CubeColor.BLUE,
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        self.assertIsInstance(cubelet, Cubelet)
    
    def test_cubelet_init_20020_ShouldCreateUncoloredCubeletForUnsuppliedParam(self):
        """ instantiating with no supplied param faces should create uncolored cubelet """
        
        cubelet = Cubelet()
        
        # see if all faces are non-colored
        for face in list(CubeFacePosition):
            expected = None
            actual = cubelet[face]
            
            self.assertEqual(actual, expected)
    
    def test_cubelet_init_20030_ShouldCreateUncoloredCubeletForEmptyDictParam(self):
        """ instantiating with empty param faces should create uncolored cubelet """
        
        cubelet = Cubelet({})
        
        # see if all faces are non-colored
        for face in list(CubeFacePosition):
            expected = None
            actual = cubelet[face]
            
            self.assertEqual(actual, expected)
    
    def test_cubelet_init_20040_ShouldColorFrontFaceIfSupplied(self):
        """ front face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.FRONT : CubeColor.GREEN
        })
        
        expected = CubeColor.GREEN
        actual = cubelet[CubeFacePosition.FRONT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20050_ShouldColorBackFaceIfSupplied(self):
        """ back face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.BACK : CubeColor.RED
        })
        
        expected = CubeColor.RED
        actual = cubelet[CubeFacePosition.BACK]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20060_ShouldColorLeftFaceIfSupplied(self):
        """ left face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = CubeColor.YELLOW
        actual = cubelet[CubeFacePosition.LEFT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20070_ShouldColorRightFaceIfSupplied(self):
        """ right face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.WHITE
        })
        
        expected = CubeColor.WHITE
        actual = cubelet[CubeFacePosition.RIGHT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20080_ShouldColorUpFaceIfSupplied(self):
        """ up face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        expected = CubeColor.BLUE
        actual = cubelet[CubeFacePosition.UP]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20090_ShouldColorDownFaceIfSupplied(self):
        """ down face should be colored correctly if supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN : CubeColor.ORANGE
        })
        
        expected = CubeColor.ORANGE
        actual = cubelet[CubeFacePosition.DOWN]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20100_ShouldNotColorFrontFaceIfNotSupplied(self):
        """ front face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE,
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.FRONT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20110_ShouldNotColorBackFaceIfNotSupplied(self):
        """ back face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE,
            CubeFacePosition.LEFT : CubeColor.YELLOW
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.BACK]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20120_ShouldNotColorLeftFaceIfNotSupplied(self):
        """ left face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.WHITE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.LEFT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20130_ShouldNotColorRightFaceIfNotSupplied(self):
        """ right face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT : CubeColor.ORANGE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.RIGHT]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20140_ShouldNotColorUpFaceIfNotSupplied(self):
        """ up face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT : CubeColor.GREEN
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.UP]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20150_ShouldNotColorDownFaceIfNotSupplied(self):
        """ down face should not be colored if not supplied in param faces """
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED,
            CubeFacePosition.FRONT: CubeColor.BLUE,
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        expected = None
        actual = cubelet[CubeFacePosition.DOWN]
        
        self.assertEqual(actual, expected)
    
    def test_cubelet_init_20160_ShouldSetColorFacesCorrectly(self):
        """ more than one face should be able to be colored """
        
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
      
    ''' Cubelet.rotate -- NEGATIVE TESTS '''
    
    def test_cubelet_rotate_10010_ShouldThrowExceptionForNonSuppliedDirectionParam(self):
        """ supplying no direction param should throw exception """
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        with self.assertRaises(Exception):
            cubelet.rotate()
    
    def test_cubelet_rotate_10020_ShouldThrowExceptionForInvalidDirectionParam(self):
        """ supplying non-CubeRotationDirection param should throw exception """
        
        cubelet = Cubelet({
            CubeFacePosition.UP : CubeColor.BLUE
        })
        
        with self.assertRaises(Exception):
            cubelet.rotate(2.46)

    ''' Cubelet.rotate -- POSITIVE TESTS '''
    
    def test_cubelet_rotate_20010_ShouldFlipForwardCorrectly(self):
        """ a normal cubelet should flip forward correctly """
        
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
    
    def test_cubelet_rotate_20020_ShouldFlipBackwardCorrectly(self):
        """ a normal cubelet should flip backward correctly """
        
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
    
    def test_cubelet_rotate_20030_ShouldFlipLeftwardCorrectly(self):
        """ a normal cubelet should flip leftward correctly """
        
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
    
    def test_cubelet_rotate_20040_ShouldFlipRightwardCorrectly(self):
        """ a normal cubelet should flip rightward correctly """
        
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
    
    def test_cubelet_rotate_20050_ShouldNotChangeCubeletWithOnlyLeftColoredOnForwardRotation(self):
        """ a cubelet with only left face colored should not be affected by flip forward """
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.WHITE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20060_ShouldNotChangeCubeletWithOnlyLeftColoredOnBackwardRotation(self):
        """ a cubelet with only left face colored should not be affected by flip backward """
        
        cubelet = Cubelet({
            CubeFacePosition.LEFT: CubeColor.GREEN
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20070_ShouldNotChangeCubeletWithOnlyRightColoredOnForwardRotation(self):
        """ a cubelet with only right face colored should not be affected by flip forward """
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT: CubeColor.RED
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_FORWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20080_ShouldNotChangeCubeletWithOnlyRightColoredOnBackwardRotation(self):
        """ a cubelet with only right face colored should not be affected by flip backward """
        
        cubelet = Cubelet({
            CubeFacePosition.RIGHT: CubeColor.ORANGE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_BACKWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20090_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnLeftwardRotation(self):
        """ a cubelet with only up face colored should not be affected by flip leftward """
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.RED
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20100_ShouldNotChangeCubeletWithOnlyUpFaceColoredOnRightwardRotation(self):
        """ a cubelet with only up face colored should not be affected by flip rightward """
        
        cubelet = Cubelet({
            CubeFacePosition.UP: CubeColor.BLUE
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20110_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnLeftwardRotation(self):
        """ a cubelet with only down face colored should not be affected by flip leftward """
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN: CubeColor.YELLOW
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_LEFTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20120_ShouldNotChangeCubeletWithOnlyDownFaceColoredOnRightwardRotation(self):
        """ a cubelet with only down face colored should not be affected by flip rightward """
        
        cubelet = Cubelet({
            CubeFacePosition.DOWN: CubeColor.GREEN
        })
        
        oldFaces = cubelet
        cubelet.rotate(CubeRotationDirection.FLIP_RIGHTWARD)
        
        for face in list(CubeFacePosition):
            expectedColor = oldFaces[face]
            actualColor = cubelet[face]
            
            self.assertEqual(actualColor, expectedColor)
    
    def test_cubelet_rotate_20130_ShouldNotChangeCubeletOnForwardThenBackwardRotation(self):
        """ a cubelet should end up unchanged by a flip forward followed by a flip backward """
        
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
    
    def test_cubelet_rotate_20140_ShouldNotChangeCubeletOnBackwardThenForwardRotation(self):
        """ a cubelet should end up unchanged by a flip backward followed by a flip forward """
        
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
    
    def test_cubelet_rotate_20150_ShouldNotChangeCubeletOnLeftwardThenRightwardRotation(self):
        """ a cubelet should end up unchanged by a flip leftward followed by a flip rightward """
        
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
    
    def test_cubelet_rotate_20160_ShouldNotChangeCubeletOnRightwardThenLeftwardRotation(self):
        """ a cubelet should end up unchanged by a flip rightward followed by a flip leftward """
        
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
    
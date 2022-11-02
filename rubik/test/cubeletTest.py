
from unittest import TestCase
from rubik.cubelet import Cubelet
from rubik.cubeColor import CubeColor
from rubik.cubeFace import CubeFace

class CubeletTest(TestCase):
    
    # __init__ - POSITIVE TESTS
    
    # there should be only 6 cube faces (by nature of a cube)
    def test_cubelet_init_10010_ShouldInstantiateCubeForValidInput(self):
    
        faces = {
            CubeFace.UP: CubeColor.RED,
            CubeFace.FRONT: CubeColor.BLUE,
            CubeFace.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(faces)
        self.assertIsInstance(cubelet, Cubelet)
        
    # __init__ - NEGATIVE TESTS
    
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


from unittest import TestCase
from rubik.cubelet import Cubelet
from rubik.cubeColor import CubeColor
from rubik.cubeFace import CubeFace

class CubeletTest(TestCase):
    
    # __init__ - POSITIVE TESTS
    
    # there should be only 6 cube faces (by nature of a cube)
    def test_cublet_init_10010_ShouldInstantiateCubeForValidInput(self):
    
        sides = {
            CubeFace.UP: CubeColor.RED,
            CubeFace.FRONT: CubeColor.BLUE,
            CubeFace.LEFT: CubeColor.WHITE
        }
        
        cubelet = Cubelet(sides)
        self.assertIsInstance(cubelet, Cubelet)

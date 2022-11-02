
import re
import itertools
from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet
from rubik.cubeCode import CubeCode

class Cube:
    '''
    Rubik's cube
    '''

    SIZE = 3
    CODE_LENGTH = 54
    
    cubelets = {}

    def __init__(self, cubeCode):
        # make sure supplied param is a valid CubeCode
        assert (isinstance(cubeCode, CubeCode))
        
        for i, j, k in itertools.product(*[range(Cube.SIZE)] * 3):
            self.cubelets[i, j, k] = Cubelet()

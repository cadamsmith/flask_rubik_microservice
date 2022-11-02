
import re
import itertools
from rubik.cubeColor import CubeColor
from rubik.cubelet import Cubelet

class Cube:
    '''
    Rubik's cube
    '''

    SIZE = 3
    CODE_LENGTH = 54
    
    cubelets = {}

    def __init__(self, cubeCode):
        # make sure supplied param is a string
        assert (isinstance(cubeCode, str))
        
        # make sure "cube code" is 54 chars long
        assert (len(cubeCode) == Cube.CODE_LENGTH)
        
        # make sure is over alphabet [brgoyw]
        assert (not bool(re.search('[^brgoyw]', cubeCode)))
        
        # make sure contains every color
        for color in list(CubeColor):
            assert (cubeCode.__contains__(color.value))
            
        # make sure contains even distribution of colors
        colorDistributions = {c: 0 for c in CubeColor}
        
        for letter in cubeCode:
            color = CubeColor(letter)
            colorDistributions[color] += 1
        
        assert (len(set(colorDistributions.values())) == 1)
        
        # make sure there are no 2 center cubelet faces with same color
        centerColors = set(map(lambda letter: CubeColor(letter), [
            cubeCode[4], cubeCode[13], cubeCode[22], cubeCode[31], cubeCode[40], cubeCode[49]
        ]))
        
        assert (len(centerColors) == len(CubeColor))
        
        for i, j, k in itertools.product(*[range(Cube.SIZE)] * 3):
            self.cubelets[i, j, k] = Cubelet()

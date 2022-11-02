
import re
from rubik.cubeColor import CubeColor

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, faces):
        # make sure supplied param is either a string or dictionary
        assert (isinstance(faces, str) or isinstance(faces, dict))
        
        if isinstance(faces, str):
            self.__initFromCubeCode__(faces)
        elif isinstance(faces, dict):
            pass
        
    def __initFromCubeCode__(self, facesCode):
        # make sure supplied param is a string
        assert (isinstance(facesCode, str))
        
        # make sure "cube code" is 54 chars long
        assert (len(facesCode) == 54)
        
        # make sure is over alphabet [brgoyw]
        assert (not bool(re.search('[^brgoyw]', facesCode)))
        
        # make sure contains every color
        for color in list(CubeColor):
            assert (facesCode.__contains__(color.value))
            
        # make sure contains even distribution of colors
        colorDistributions = {c: 0 for c in CubeColor}
        
        for letter in facesCode:
            color = CubeColor(letter)
            colorDistributions[color] += 1
        
        assert (len(set(colorDistributions.values())) == 1)
        
        # make sure there are no 2 center cubelet faces with same colo
        centerColors = set(map(lambda letter: CubeColor(letter), [
            facesCode[5], facesCode[14], facesCode[23], facesCode[32], facesCode[41], facesCode[50]
        ]))
        
        assert (len(centerColors) == len(CubeColor))


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
        
    def __initFromCubeCode__(self, faces):
        # make sure supplied param is a string
        assert (isinstance(faces, str))
        
        # make sure "cube code" is 54 chars long
        assert (len(str) is 54)
        
        # make sure contains every color
        for color in list(CubeColor):
            assert (faces.__contains__(color.value))

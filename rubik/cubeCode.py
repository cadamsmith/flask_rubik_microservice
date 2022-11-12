
import re
from rubik.cubeColor import CubeColor
from rubik.cubeFacePosition import CubeFacePosition

class CubeCode:
    '''represents a code supplied to create a 3x3x3 Cube instance'''
    
    CODE_LENGTH = 54
    
    FACE_POSITION_ORDER = [
        CubeFacePosition.FRONT,
        CubeFacePosition.RIGHT,
        CubeFacePosition.BACK,
        CubeFacePosition.LEFT,
        CubeFacePosition.UP,
        CubeFacePosition.DOWN,
    ]
    
    FACE_CENTER_INDICES = [4, 13, 22, 31, 40, 49]
    
    def __init__(self, codeText):
        # make sure supplied param is a valid cube code text
        assert self.isValid(codeText)
        
        self.text = codeText
    
    @classmethod
    def isValid(cls, codeText):
        
        # check if supplied code text is a string
        if not isinstance(codeText, str):
            return False
        
        # check if code text is 54 chars long
        if len(codeText) != cls.CODE_LENGTH:
            return False
        
        # check if it's over alphabet [brgoyw]
        if bool(re.search('[^brgoyw]', codeText)):
            return False
        
        # check if it contains every color
        for color in CubeColor.getFaceColors():
            if not codeText.__contains__(color.value):
                return False
        
        # check if it contains even distribution of colors
        colorDistributions = {c: 0 for c in CubeColor.getFaceColors()}
        
        for letter in codeText:
            color = CubeColor(letter)
            colorDistributions[color] += 1
        
        if not len(set(colorDistributions.values())) == 1:
            return False
        
        # check if the center cubelet faces have unique colors
        centerColors = set(map(lambda index: CubeColor(codeText[index]), cls.FACE_CENTER_INDICES))
        
        if not len(centerColors) == len(CubeColor.getFaceColors()):
            return False
        
        # congrats, its a valid cube code
        return True
    
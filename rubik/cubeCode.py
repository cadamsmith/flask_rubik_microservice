
from rubik.cubeColor import CubeColor
from rubik.cubeFacePosition import CubeFacePosition

class CubeCode:
    """ represents a code supplied to create a 3x3x3 Cube instance """
    
    """ length of the cube code """
    CODE_LENGTH = 54
    
    """ ordering that shows how the cube faces are encoded in the cube code """
    FACE_POSITION_ORDER = [
        CubeFacePosition.FRONT,
        CubeFacePosition.RIGHT,
        CubeFacePosition.BACK,
        CubeFacePosition.LEFT,
        CubeFacePosition.UP,
        CubeFacePosition.DOWN,
    ]
    
    """ the center tile index in each cube face """
    FACE_CENTER_INDICES = [4, 13, 22, 31, 40, 49]
    
    def __init__(self, codeText: str):
        """ instantiates CubeCode from supplied code string """
        
        # make sure supplied param is a valid cube code text
        assert self.isValid(codeText)
        
        self.text = codeText
    
    @classmethod
    def isValid(cls, codeText: str):
        """ determines whether a string is a valid cube code """
        
        # check if supplied code text is a string
        if not isinstance(codeText, str):
            return False
        
        # check if code text is 54 chars long
        if len(codeText) != cls.CODE_LENGTH:
            return False
        
        # check if it's made up of valid cube color codes
        for letter in codeText:
            if not CubeColor.hasValue(letter):
                return False
        
        # tally up color distributions
        colorDistributions = {c: 0 for c in list(CubeColor)}
        
        for letter in codeText:
            color = CubeColor(letter)
            colorDistributions[color] += 1
        
        # check whether any colors are missing
        if any(count == 0 for count in colorDistributions.values()):
            return False
        
        # check if colors are unevenly distributed
        if not len(set(colorDistributions.values())) == 1:
            return False
        
        # check if the center cubelet faces have unique colors
        centerColors = set(map(
            lambda index: CubeColor(codeText[index]),
            cls.FACE_CENTER_INDICES
        ))
        
        if not len(centerColors) == len(list(CubeColor)):
            return False
        
        # congrats, its a valid cube code
        return True
    
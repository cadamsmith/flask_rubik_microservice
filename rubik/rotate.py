
from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeCode import CubeCode
from rubik.faceRotationDirection import FaceRotationDirection
from rubik.cube import Cube

ERROR_MISSING_CUBE = 'error: missing cube'
ERROR_INVALID_CUBE = 'error: invalid cube'
ERROR_INVALID_DIR = 'error: invalid rotation'

def _rotate(params):
    """ Return rotated cube """
    
    # validate that 'cube' param exists
    if 'cube' not in params:
        return __missingCubeError__()
    
    cubeCode = params['cube']
    
    # validate that 'cube' param
    if not CubeCode.isValid(cubeCode):
        return __invalidCubeError__()
    
    # by default, rotation taken to be front clockwise
    rotationCodes = 'F'
    
    # if 'dir' param exists, validate it
    if 'dir' in params:
        dirValue = params['dir']
        
        # validate that it is a string
        if not isinstance(dirValue, str):
            return __invalidDirError__()
        
        # validate it is over alphabet [FfRrBbLlUuDd]
        for letter in dirValue:
            if not CubeFacePosition.hasValue(letter.upper()):
                return __invalidDirError__()
        
        if len(dirValue) > 0:
            rotationCodes = dirValue
            
    # build initial cube
    cube = Cube(cubeCode)
    
    # loop thru each rotation code
    for rotationCode in rotationCodes:
        
        # determine which way to rotate the cube face
        direction = (
            FaceRotationDirection.CLOCKWISE 
            if rotationCode.isupper()
            else FaceRotationDirection.COUNTERCLOCKWISE
        )
        
        # determine which cube face to rotate
        facePosition = CubeFacePosition(rotationCode.upper())
        
        cube.rotateFace(facePosition, direction)
    
    # return final cube code
    result = {
        'cube': cube.toCode(),
        'status': 'ok'
    }
    
    return result

def __missingCubeError__():
    """ returns error for missing cube param """
    
    return {'status': ERROR_MISSING_CUBE}

def __invalidCubeError__():
    """ returns error for invalid cube param """
    
    return {'status': ERROR_INVALID_CUBE}

def __invalidDirError__():
    """ returns error for invalid direction param """
    
    return {'status': ERROR_INVALID_DIR}

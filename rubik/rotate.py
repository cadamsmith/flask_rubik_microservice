
from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeCode import CubeCode

ERROR_MISSING_CUBE = 'error: missing cube'
ERROR_INVALID_CUBE = 'error: invalid cube'
ERROR_INVALID_DIR = 'error: invalid rotation'

def _rotate(params):
    """Return rotated cube"""
    
    # validate that 'cube' param exists
    if 'cube' not in params:
        return __missingCubeError__()
    
    cube = params['cube']
    
    # validate that 'cube' param
    if not CubeCode.isValid(cube):
        return __invalidCubeError__()
    
    # by default, rotation taken to be front clockwise
    dir = 'F'
    
    # if 'dir' param exists, validate it
    if 'dir' in params:
        dir = params['dir']
        
        # validate that it is a string
        if not isinstance(dir, str):
            return __invalidDirError__()
        
        # validate that it has at least one character
        if len(dir) < 1:
            return __invalidDirError__()
        
        # validate it is over alphabet [FfRrBbLlUuDd]
        for char in dir:
            if not CubeFacePosition.hasValue(char.upper()):
                return __invalidDirError__()
    
    result = {}
    encodedCube = params.get('cube',None)       #STUB:  get "cube" parameter if present
    rotatedCube = encodedCube                  #STUB:  rotate the cube
    result['cube'] = rotatedCube               
    result['status'] = 'ok'                     
    return result

def __missingCubeError__():
    return {'status': ERROR_MISSING_CUBE}

def __invalidCubeError__():
    return {'status': ERROR_INVALID_CUBE}

def __invalidDirError__():
    return {'status': ERROR_INVALID_DIR}

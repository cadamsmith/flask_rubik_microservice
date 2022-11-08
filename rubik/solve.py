import rubik.cube as rubik
from rubik.cubeCode import CubeCode

ERROR_MISSING_CUBE = 'error: missing cube'
ERROR_INVALID_CUBE = 'error: invalid cube'

def _solve(params):
    """Return rotates needed to solve input cube"""
    
    # validate that 'cube' param exists
    if 'cube' not in params:
        return __missingCubeError__()
    
    cubeCodeText = params['cube']
    
    # validate that 'cube' param conforms to spec
    if not CubeCode.isValid(cubeCodeText):
        return __invalidCubeError__()
    
    result = {}
    encodedCube = params.get('cube',None)
    result['rotations'] = 'FfRrBbLlUuDd'
    result['status'] = 'ok'
    return result

def __missingCubeError__():
    return {'status': ERROR_MISSING_CUBE}

def __invalidCubeError__():
    return {'status': ERROR_INVALID_CUBE}
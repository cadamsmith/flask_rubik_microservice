
from rubik.cube import Cube
from rubik.cubeSolver import CubeSolver
from rubik.cubeCode import CubeCode
from rubik.faceRotationDirection import FaceRotationDirection

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
    
    # solve the cube, i.e. obtain rotations to solve it
    solver = CubeSolver(
        Cube(CubeCode(cubeCodeText))
    )
    
    solver.solve()
    rotations = solver.directions
    
    # loop thru rotations and convert them to rotation codes
    rotationCodes = ''
    for (facePosition, direction) in rotations:
        rotationCode = facePosition.value
        
        if direction is FaceRotationDirection.COUNTERCLOCKWISE:
            rotationCode = rotationCode.lower()
        
        rotationCodes += rotationCode
    
    result = {
        'status': 'ok',
        'rotations': rotationCodes
    }
    
    return result

def __missingCubeError__():
    """ returns error for missing cube param """
    
    return {'status': ERROR_MISSING_CUBE}

def __invalidCubeError__():
    """ returns error for invalid cube param """
    
    return {'status': ERROR_INVALID_CUBE}
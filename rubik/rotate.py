
ERROR_MISSING_CUBE = 'error: missing cube'
ERROR_INVALID_CUBE = 'error: invalid cube'
ERROR_INVALID_DIR = 'error: invalid rotation'

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube',None)       #STUB:  get "cube" parameter if present
    rotatedCube = encodedCube                  #STUB:  rotate the cube
    result['cube'] = rotatedCube               
    result['status'] = 'ok'                     
    return result
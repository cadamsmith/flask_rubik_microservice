class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, faces):
        assert (isinstance(faces, str) or isinstance(faces, dict))
        
        if isinstance(faces, str):
            pass
        elif isinstance(faces, dict):
            pass
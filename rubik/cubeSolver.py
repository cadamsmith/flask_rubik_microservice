
from rubik.cube import Cube

class CubeSolver():
    
    def __init__(self, cube: Cube):
        assert (isinstance(cube, Cube))
        
        self.cube = cube
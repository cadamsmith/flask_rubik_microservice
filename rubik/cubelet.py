
from rubik.cubeFace import CubeFace
from rubik.cubeColor import CubeColor

class Cubelet:

    def __init__(self, faces = {}):
        
        # initialize all faces to no color
        self.faces = list(map(
            {s: None for s in CubeFace}
        ))
        
        # make sure that the param faces is a dictionary with CubeFace keys and CubeColor values
        assert (all(isinstance(face, CubeFace) for face in faces.keys()))
        assert (all(isinstance(color, CubeColor) for color in faces.values()))
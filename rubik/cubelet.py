
from rubik.cubeFacePosition import CubeFacePosition
from rubik.cubeColor import CubeColor
from rubik.cubeRotationDirection import CubeRotationDirection

class Cubelet:
    """ Represents one of the smaller cubes that make up a Rubik's Cube """

    def __init__(self, coloredFaces = {}):
        """ instantiate Cubelet from info about its face colors """
        
        # make sure coloredFaces is dict<CubeFacePosition, CubeColor>
        assert (isinstance(coloredFaces, dict))
        
        assert (all(isinstance(face, CubeFacePosition) for face in coloredFaces.keys()))
        assert (all(isinstance(color, CubeColor) for color in coloredFaces.values()))
        
        # make sure that no more than 3 cubelet faces are colored
        assert (len(coloredFaces) <= 3)
        
        # initialize all cubeData to no color
        self._faces = {cf: None for cf in CubeFacePosition}
        
        self._faces.update(coloredFaces)
    
    def __getitem__(self, facePosition: CubeFacePosition) -> CubeColor | None:
        """ accessor for the faces that make up cubelet """
        
        # ensure param is valid type
        assert isinstance(facePosition, CubeFacePosition)
        
        return self._faces[facePosition]
    
    def setFaceColor(self, facePosition: CubeFacePosition, color: CubeColor):
        """ colors one of the cubelet's faces """
        
        # ensure params are valid types
        assert (isinstance(facePosition, CubeFacePosition))
        assert (isinstance(color, CubeColor))
        
        self._faces[facePosition] = color
    
    def getFaceColors(self):
        """ returns the face colors of the cubelet """
        
        return {
            facePosition: self[facePosition]
            for facePosition in CubeFacePosition
        }
    
    def rotate(self, direction: CubeRotationDirection):
        """ rotates the cubelet in some direction """
        
        # make sure direction is a CubeRotationDirection
        assert (isinstance(direction, CubeRotationDirection))
        
        # go thru each face position, and calculate its new color based on the rotation
        alteredFaces = {}
        for facePosition in list(CubeFacePosition):
            newFacePosition = CubeFacePosition.rotate(facePosition, direction)
            
            alteredFaces[newFacePosition] = self[facePosition]
        
        # apply the transform
        self._faces.update(alteredFaces)
    
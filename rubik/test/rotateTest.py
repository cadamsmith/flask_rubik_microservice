from unittest import TestCase
import rubik.rotate as rotate

class RotateTest(TestCase):
    
    # rotate - NEGATIVE TESTS
    
    # supplying no cube param should result in error status
    def test_rotate_20010_ShouldErrorOnMissingCube(self):
        result = rotate._rotate({'op': 'rotate', 'dir': 'R'})
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_MISSING_CUBE)
    
    # supplying non-string dir param should result in error status
    def test_rotate_20020_ShouldErrorOnNonStringDir(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': {
                'a': 'b' 
            }
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying empty string dir param should result in error status
    def test_rotate_20030_ShouldErrorOnEmptyStringDir(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': ''
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying string dir param with one character should result in error status if the character
    # is an invalid rotational code
    def test_rotate_20040_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'P'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying string dir param with multiple characters should result in error status
    # if any of the characters are invalid rotational codes
    def test_rotate_20050_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'FfRrBbELlUuDd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying non-string cube should result in error status
    def test_rotate_20630_ShouldErrorOnNonStringCube(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': False,
            'dir': 'l'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    # supplying string cube not 54 chars long should result in error status
    def test_rotate_20070_ShouldErrorOnCubeWithInvalidLength(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'ooyyyyyyyyyw',
            'dir': 'l'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
        
    # supplying a string cube not over the alphabet [brgoyw] should throw exception
    def test_rotate_20080_ShouldErrorOnCubeContainingNonColorChars(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor',
            'dir': 'b'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    # supplying a string cube not containing every color code should throw exception
    def test_rotate_20090_ShouldErrorOnCubeNotContainingEveryColor(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg',
            'dir': 'R'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
            
    # supplying a string cube with an uneven distribution of colors should throw exception
    def test_rotate_init_20100_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy',
            'dir': 'd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
            
    # supplying a string cube with non-unique center cubelet face colors should throw exception
    def test_rotate_init_20110_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr',
            'dir': 'U'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
        
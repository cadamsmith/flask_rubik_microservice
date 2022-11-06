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
    def test_rotate_20021_ShouldErrorOnEmptyStringDir(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': ''
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying string dir param with one character should result in error status if the character
    # is an invalid rotational code
    def test_rotate_20022_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'P'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
    # supplying string dir param with multiple characters should result in error status
    # if any of the characters are invalid rotational codes
    def test_rotate_20023_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'FfRrBbELlUuDd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
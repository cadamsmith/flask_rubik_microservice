from unittest import TestCase
import rubik.rotate as rotate

class RotateTest(TestCase):
    
    # rotate - NEGATIVE TESTS
    
    # supplying no cube param should result in error status
    def test_rotate_20010_ShouldErrorOnMissingCube(self):
        result = rotate._rotate({'op': 'rotate', 'dir': 'R'})
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_MISSING_CUBE)
    
    # supplying invalid dir param should result in error status
    def test_rotate_20020_ShouldErrorOnInvalidDirection(self):
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'p'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
        
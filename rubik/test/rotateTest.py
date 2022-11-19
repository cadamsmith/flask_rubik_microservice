
from unittest import TestCase

import rubik.rotate as rotate

class RotateTest(TestCase):
    
    ''' rotate - NEGATIVE TESTS '''
    
    def test_rotate_10010_ShouldErrorOnMissingCube(self):
        """ supplying no cube param should result in error status """
        
        result = rotate._rotate({
            'op': 'rotate',
            'dir': 'R'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_MISSING_CUBE)
    
    def test_rotate_10020_ShouldErrorOnNonStringDir(self):
        """ supplying non-string dir param should result in error status """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': {
                'a': 'b' 
            }
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
    
    def test_rotate_10040_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        """ 
        supplying string dir param with one character should result in error status if the 
        character is an invalid rotational code
        """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'P'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
    
    def test_rotate_10050_ShouldErrorOnMultipleCharDirWithAnyInvalidRotationalCodes(self):
        """
        supplying string dir param with multiple characters should result in error status
        if any of the characters are invalid rotational codes
        """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg',
            'dir': 'FfRrBbELlUuDd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_DIR)
    
    def test_rotate_10060_ShouldErrorOnNonStringCube(self):
        """ supplying non-string cube should result in error status """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': False,
            'dir': 'l'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    def test_rotate_10070_ShouldErrorOnCubeWithInvalidLength(self):
        """ supplying string cube not 54 chars long should result in error status """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'ooyyyyyyyyyw',
            'dir': 'l'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    def test_rotate_10080_ShouldErrorOnCubeContainingNonColorChars(self):
        """ supplying a string cube not over the alphabet [brgoyw] should throw exception """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor',
            'dir': 'b'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    def test_rotate_10090_ShouldErrorOnCubeNotContainingEveryColor(self):
        """ supplying a string cube not containing every color code should throw exception """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg',
            'dir': 'R'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    def test_rotate_10100_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        """ supplying a string cube with an uneven distribution of colors should throw exception """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy',
            'dir': 'd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    def test_rotate_10110_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        """ supplying a string cube with non-unique center cubelet face colors should throw exception """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr',
            'dir': 'U'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
    
    ''' rotate - POSITIVE TESTS '''
    
    def test_rotate_20010_ShouldReturnStatusOKForValidParams(self):
        """ supplying valid params should return a result with status of ok """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'wrobbobgygwrwrwgoybgorgwbggyboboywyrgywoygbbwyorrwyrro',
            'dir': 'FlDlDU'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
    
    def test_rotate_20020_ShouldFrontClockwiseRotateWhenDirectionNotSupplied(self):
        """ supplying no direction should rotate front clockwise by default """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'orgwbrwbgobwbrwwobrgrogworgyowrogrobbybbyygyyowrgwyygy'
        })
        
        frontClockwiseResult = rotate._rotate({
            'op': 'rotate',
            'cube': 'orgwbrwbgobwbrwwobrgrogworgyowrogrobbybbyygyyowrgwyygy',
            'dir': 'F'
        })
        
        self.assertIn('cube', result)
        self.assertIn('cube', frontClockwiseResult)
        self.assertEqual(result['cube'], frontClockwiseResult['cube'])
    
    def test_rotate_20030_ShouldFrontClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube front clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'F'
        })
        
        expected = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20031_ShouldBackClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube back clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'B'
        })
        
        expected = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20032_ShouldLeftClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube left clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'L'
        })
        
        expected = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20033_ShouldRightClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube right clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'R'
        })
        
        expected = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20034_ShouldUpClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube up clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'U'
        })
        
        expected = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20035_ShouldDownClockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube down clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'D'
        })
        
        expected = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20040_ShouldFrontCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube front counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'f'
        })
        
        expected = 'bbbbbbbbbwrrwrrwrrgggggggggooyooyooyyyyyyyrrrooowwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20041_ShouldBackCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube back counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'b'
        })
        
        expected = 'bbbbbbbbbrryrryrrygggggggggwoowoowoooooyyyyyywwwwwwrrr'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20042_ShouldLeftCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube left counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'l'
        })
        
        expected = 'wbbwbbwbbrrrrrrrrrggyggyggyooooooooobyybyybyygwwgwwgww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20043_ShouldRightCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube right counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'r'
        })
        
        expected = 'bbybbybbyrrrrrrrrrwggwggwggoooooooooyygyygyygwwbwwbwwb'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20044_ShouldUpCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube up counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'u'
        })
        
        expected = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20045_ShouldDownCounterclockwiseRotateSolvedCubeCorrectly(self):
        """ rotating a solved cube down counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'd'
        })
        
        expected = 'bbbbbbrrrrrrrrrgggggggggooooooooobbbyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20050_ShouldFrontClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube front clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'F'
        })
        
        expected = 'ywgbbbbgorooyrobwbyrwygbooorrgoorwwrbggyywrgwyywrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20051_ShouldBackClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube back clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'B'
        })
        
        expected = 'gbowbgybbwoyyrgywgoyyogrobwgrwgogbwroobyywrybgrrrwbrow'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20052_ShouldLeftClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube left clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'L'
        })
        
        expected = 'bboybgrbbwooyroywbyrgygroogworworrgwoggbywwybgrrwwbygy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20053_ShouldRightClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube right clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'R'
        })
        
        expected = 'gbrwbbybyyywwroboobrwwgbgoorrwoogwwrbgoyygrybgrorwyggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20054_ShouldUpClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube up clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'U'
        })
        
        expected = 'woowbgybbyrwyroywbrrwygbooogbooogwwrrybyygbwggrrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20055_ShouldDownClockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube down clockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'D'
        })
        
        expected = 'gbowbgwwrwooyroybbyrwygbywbrrwoogooobggyywrybgrggwrybr'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20060_ShouldFrontCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube front counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'f'
        })
        
        expected = 'ogbbbbgwyroorrogwbyrwygbooorrbooywwrbggyywwyywgrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20061_ShouldBackCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube back counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'b'
        })
        
        expected = 'gbowbgybbwobyrgywgwborgoyyogrwgogywrworyywrybgrrrwbboo'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20062_ShouldLeftCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube left counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'l'
        })
        
        expected = 'gborbggbbwooyroywbyrrygyoobwgrrowrowgggwywyyborrbwbwgy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20063_ShouldRightCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube right counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'r'
        })
        
        expected = 'gbgwbwybbooborwwyyyrwbgbroorrwoogwwrbgoyyyryygrorwgggb'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20064_ShouldUpCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube up counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'u'
        })
        
        expected = 'rrwwbgybbgboyroywbwooygboooyrwoogwwrgwbgyybyrgrrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20065_ShouldDownCounterclockwiseRotateRandomCubeCorrectly(self):
        """ rotating a random cube down counterclockwise should work correctly """
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'd'
        })
        
        expected = 'gbowbgywbwooyrooooyrwygbwwrrrwoogybbbggyywrybrbyrwggrg'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    def test_rotate_20070_ShouldBeUnchangedAfterTwoRotationsForSameFaceButAlternatingDirections(self):
        """ rotating same face twice, but in alternating directions should result in unchanged cube """
        
        cubeCodeText = 'orbbbgrogwybwrywoyyoorgrobygybgoyrrgwwogyowbrybrwwgbwg'
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': cubeCodeText,
            'dir': 'Rr'
        })
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], cubeCodeText)
    
    def test_rotate_20080_ShouldBeUnchangedAfterFourIdenticalRotations(self):
        """ rotating same face in same direction 4 times should result in unchanged cube """
        
        cubeCodeText = 'orbbbgrogwybwrywoyyoorgrobygybgoyrrgwwogyowbrybrwwgbwg'
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': cubeCodeText,
            'dir': 'UUUU'
        })
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], cubeCodeText)
    
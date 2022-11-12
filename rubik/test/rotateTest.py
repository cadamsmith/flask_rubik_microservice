from unittest import TestCase
import rubik.rotate as rotate

class RotateTest(TestCase):
    
    # rotate - POSITIVE TESTS
    
    # supplying valid params should return a result with status of ok
    def test_rotate_10010_ShouldReturnStatusOKForValidParams(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'wrobbobgygwrwrwgoybgorgwbggyboboywyrgywoygbbwyorrwyrro',
            'dir': 'FlDlDU'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
    
    # supplying no direction should rotate front clockwise by default
    def test_rotate_10020_ShouldFrontClockwiseRotateWhenDirectionNotSupplied(self):
        
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
    
    # rotating a solved cube front clockwise should work correctly
    def test_rotate_10030_ShouldFrontClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'F'
        })
        
        expected = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    # rotating a solved cube back clockwise should work correctly
    def test_rotate_10031_ShouldBackClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'B'
        })
        
        expected = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube left clockwise should work correctly
    def test_rotate_10032_ShouldLeftClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'L'
        })
        
        expected = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube right clockwise should work correctly
    def test_rotate_10033_ShouldRightClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'R'
        })
        
        expected = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube up clockwise should work correctly
    def test_rotate_10034_ShouldUpClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'U'
        })
        
        expected = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube down clockwise should work correctly
    def test_rotate_10035_ShouldDownClockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'D'
        })
        
        expected = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube front counterclockwise should work correctly
    def test_rotate_10040_ShouldFrontCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'f'
        })
        
        expected = 'bbbbbbbbbwrrwrrwrrgggggggggooyooyooyyyyyyyrrrooowwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    # rotating a solved cube back counterclockwise should work correctly
    def test_rotate_10041_ShouldBackCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'b'
        })
        
        expected = 'bbbbbbbbbrryrryrrygggggggggwoowoowoooooyyyyyywwwwwwrrr'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube left counterclockwise should work correctly
    def test_rotate_10042_ShouldLeftCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'l'
        })
        
        expected = 'wbbwbbwbbrrrrrrrrrggyggyggyooooooooobyybyybyygwwgwwgww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube right counterclockwise should work correctly
    def test_rotate_10043_ShouldRightCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'r'
        })
        
        expected = 'bbybbybbyrrrrrrrrrwggwggwggoooooooooyygyygyygwwbwwbwwb'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube up counterclockwise should work correctly
    def test_rotate_10044_ShouldUpCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'u'
        })
        
        expected = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a solved cube down counterclockwise should work correctly
    def test_rotate_10045_ShouldDownCounterclockwiseRotateSolvedCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
            'dir': 'd'
        })
        
        expected = 'bbbbbbrrrrrrrrrgggggggggooooooooobbbyyyyyyyyywwwwwwwww'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube front clockwise should work correctly
    def test_rotate_10050_ShouldFrontClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'F'
        })
        
        expected = 'ywgbbbbgorooyrobwbyrwygbooorrgoorwwrbggyywrgwyywrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    # rotating a random cube back clockwise should work correctly
    def test_rotate_10051_ShouldBackClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'B'
        })
        
        expected = 'gbowbgybbwoyyrgywgoyyogrobwgrwgogbwroobyywrybgrrrwbrow'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube left clockwise should work correctly
    def test_rotate_10052_ShouldLeftClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'L'
        })
        
        expected = 'bboybgrbbwooyroywbyrgygroogworworrgwoggbywwybgrrwwbygy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube right clockwise should work correctly
    def test_rotate_10053_ShouldRightClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'R'
        })
        
        expected = 'gbrwbbybyyywwroboobrwwgbgoorrwoogwwrbgoyygrybgrorwyggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube up clockwise should work correctly
    def test_rotate_10054_ShouldUpClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'U'
        })
        
        expected = 'woowbgybbyrwyroywbrrwygbooogbooogwwrrybyygbwggrrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube down clockwise should work correctly
    def test_rotate_10055_ShouldDownClockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'D'
        })
        
        expected = 'gbowbgwwrwooyroybbyrwygbywbrrwoogooobggyywrybgrggwrybr'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube front counterclockwise should work correctly
    def test_rotate_10060_ShouldFrontCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'f'
        })
        
        expected = 'ogbbbbgwyroorrogwbyrwygbooorrbooywwrbggyywwyywgrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
    
    # rotating a random cube back counterclockwise should work correctly
    def test_rotate_10061_ShouldBackCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'b'
        })
        
        expected = 'gbowbgybbwobyrgywgwborgoyyogrwgogywrworyywrybgrrrwbboo'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube left counterclockwise should work correctly
    def test_rotate_10062_ShouldLeftCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'l'
        })
        
        expected = 'gborbggbbwooyroywbyrrygyoobwgrrowrowgggwywyyborrbwbwgy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube right counterclockwise should work correctly
    def test_rotate_10063_ShouldRightCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'r'
        })
        
        expected = 'gbgwbwybbooborwwyyyrwbgbroorrwoogwwrbgoyyyryygrorwgggb'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube up counterclockwise should work correctly
    def test_rotate_10064_ShouldUpCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'u'
        })
        
        expected = 'rrwwbgybbgboyroywbwooygboooyrwoogwwrgwbgyybyrgrrrwbggy'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating a random cube down counterclockwise should work correctly
    def test_rotate_10065_ShouldDownCounterclockwiseRotateRandomCubeCorrectly(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gbowbgybbwooyroywbyrwygbooorrwoogwwrbggyywrybgrrrwbggy',
            'dir': 'd'
        })
        
        expected = 'gbowbgywbwooyrooooyrwygbwwrrrwoogybbbggyywrybrbyrwggrg'
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], expected)
        
    # rotating same face twice, but in alternating directions should result in unchanged cube
    def test_rotate_10070_ShouldBeUnchangedAfterTwoRotationsForSameFaceButAlternatingDirections(self):
        
        cubeCodeText = 'orbbbgrogwybwrywoyyoorgrobygybgoyrrgwwogyowbrybrwwgbwg'
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': cubeCodeText,
            'dir': 'Rr'
        })
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], cubeCodeText)
    
    # rotating same face in same direction 4 times should result in unchanged cube
    def test_rotate_10080_ShouldBeUnchangedAfterFourIdenticalRotations(self):
        
        cubeCodeText = 'orbbbgrogwybwrywoyyoorgrobygybgoyrrgwwogyowbrybrwwgbwg'
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': cubeCodeText,
            'dir': 'UUUU'
        })
        
        self.assertIn('cube', result)
        self.assertEqual(result['cube'], cubeCodeText)
    
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
    def test_rotate_20060_ShouldErrorOnNonStringCube(self):
        
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
    def test_rotate_20100_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy',
            'dir': 'd'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
            
    # supplying a string cube with non-unique center cubelet face colors should throw exception
    def test_rotate_20110_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        
        result = rotate._rotate({
            'op': 'rotate',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr',
            'dir': 'U'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], rotate.ERROR_INVALID_CUBE)
        

import re
from unittest import TestCase

import rubik.solve as solve

class SolveTest(TestCase):
    
    # solve - POSITIVE TESTS
    
    # supplying valid params should return a result with status of ok
    def test_solve_10010_ShouldReturnStatusOKForValidParams(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
        
    # supplying valid params should return a result with valid rotation codes
    def test_solve_10020_ShouldReturnValidRotationCodesForValidParams(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'boyybbowrrywrrowrgbgyygwwbgbgogoryggrooyybybgwobrwwowr'
        })
        
        # make sure rotation codes are present
        self.assertIn('rotations', result)
        
        # make sure rotation codes are valid
        isInvalid = bool(re.search('[^FfBbLlRrUuDd]', result['rotations']))
        self.assertFalse(isInvalid)
        
    # an already solved cube should yield no rotations to solve down cross
    def test_solve_10030_ASolvedCubeShouldYieldNoSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        })
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], '')
    
    # a cube with a down cross should yield no rotations to solve down cross
    def test_solve_10031_ACubeWithSolveDownLayerShouldYieldNoSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'brrrbrbbbgbogrorrrbgoygggggyyyooyooogyybyorbywwwwwwwww'
        })
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], '')
        
    # a cube with a top daisy should yield correct solve directions
    def test_solve_10040_ACubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg'
        })
        
        expected = 'uRRULLBBUFFBUbbuuBUbuBluuLfuFUUluuLUluL'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
        
    # another cube with a top daisy should yield correct solve directions
    def test_solve_10041_AnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb'
        })
        
        expected = 'FFUURRULLBBFUfuRUruLUlUruR'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
        
    # yet another cube with a top daisy should yield correct solve directions
    def test_solve_10042_YetAnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg'
        })
        
        expected = 'FFLLBBRRuRUrbuBruuRUruRluLUluuLUluL'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    # a cube without a top daisy should yield correct solve directions
    def test_solve_10050_ACubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo'
        })
        
        expected = 'FFlRuuFUluRRULLBBUFFbuuBufuFbuuBluLuruRLUl'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
        
    # another cube without a top daisy should yield correct solve directions
    def test_solve_10051_AnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb'
        })
        
        expected = 'FLLuLLBBUBuRRFFLLBBUUFUfUBUb'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
        
    # yet another cube without a top daisy should yield correct solve directions
    def test_solve_100512_YetAnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        expected = 'FlbRuRRUfuRRUUBBUULLUUFFUUluuLfuFUUFUfuubuB'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    # solve - NEGATIVE TESTS
    
    # supplying no cube param should result in error status
    def test_solve_20010_ShouldErrorOnMissingCube(self):
        result = solve._solve({'op': 'solve', 'dir': 'R'})
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_MISSING_CUBE)
    
    # supplying non-string cube should result in error status
    def test_solve_20020_ShouldErrorOnNonStringCube(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': [1, 2, 3]
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    # supplying string cube not 54 chars long should result in error status
    def test_solve_20030_ShouldErrorOnCubeWithInvalidLength(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bryogw'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
        
    # supplying a string cube not over the alphabet [brgoyw] should throw exception
    def test_solve_20040_ShouldErrorOnCubeContainingNonColorChars(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    # supplying a string cube not containing every color code should throw exception
    def test_solve_20050_ShouldErrorOnCubeNotContainingEveryColor(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
            
    # supplying a string cube with an uneven distribution of colors should throw exception
    def test_solve_20060_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
            
    # supplying a string cube with non-unique center cubelet face colors should throw exception
    def test_solve_20070_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
        
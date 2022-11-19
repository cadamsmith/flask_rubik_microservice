
import re
from unittest import TestCase

import rubik.solve as solve
from rubik.cubeFacePosition import CubeFacePosition

class SolveTest(TestCase):
    
    ''' solve -- NEGATIVE TESTS '''
    
    def test_solve_10010_ShouldErrorOnMissingCube(self):
        """ supplying no cube param should result in error status """
        
        result = solve._solve({'op': 'solve', 'dir': 'R'})
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_MISSING_CUBE)
    
    def test_solve_10020_ShouldErrorOnNonStringCube(self):
        """ supplying non-string cube should result in error status """
        
        result = solve._solve({
            'op': 'solve',
            'cube': [1, 2, 3]
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    def test_solve_10030_ShouldErrorOnCubeWithInvalidLength(self):
        """ supplying string cube not 54 chars long should result in error status """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bryogw'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    def test_solve_10040_ShouldErrorOnCubeContainingNonColorChars(self):
        """ supplying a string cube not over the alphabet [brgoyw] should throw exception """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gorbbgobbwgowrrwrbgwwygyyggr!rgowyybbrwwyrybgyyoowboor'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    def test_solve_10050_ShouldErrorOnCubeNotContainingEveryColor(self):
        """ supplying a string cube not containing every color code should throw exception """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'ggwobgrrbrwgorrwggwwoggbrgggbrwobbrwggorgobobggowwbogg'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    def test_solve_10060_ShouldErrorOnCubeWithUnevenColorDistribution(self):
        """ supplying a string cube with an uneven distribution of colors should throw exception """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wobrbrrryyoowrwrggggyggwrrwgyroobobborwbyyggowwbowybyy'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    def test_solve_10070_ShouldErrorOnCubeWithNonUniqueCenterFaceColors(self):
        """ supplying a string cube with non-unique center cubelet face colors should throw exception """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'gyyogroywgrygrorbwryyggbbwwbwowoboybrbgoywwooyggrwrbbr'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], solve.ERROR_INVALID_CUBE)
    
    ''' solve -- POSITIVE TESTS '''
    
    def test_solve_20010_ShouldReturnStatusOKForValidParams(self):
        """ supplying valid params should return a result with status of ok """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        })
        
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'ok')
    
    def test_solve_20020_ShouldReturnValidRotationCodesForValidParams(self):
        """ supplying valid params should return a result with valid rotation codes """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'boyybbowrrywrrowrgbgyygwwbgbgogoryggrooyybybgwobrwwowr'
        })
        
        # make sure rotation codes are present
        self.assertIn('rotations', result)
        
        # make sure rotation codes are valid
        for letter in result['rotations']:
            self.assertTrue(CubeFacePosition.hasValue(letter.upper()))
    
    def test_solve_20030_ASolvedCubeShouldYieldNoSolveDirections(self):
        """ an already solved cube should yield no rotations to solve down cross """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        })
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], '')
    
    def test_solve_20031_ACubeWithSolvedDownLayerShouldYieldNoSolveDirections(self):
        """ a cube with a down cross should yield no rotations to solve down cross """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'brrrbrbbbgbogrorrrbgoygggggyyyooyooogyybyorbywwwwwwwww'
        })
        
        expected = 'uufuFURUrUUFUfuluLUruRUBUbUFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20040_ACubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube with a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg'
        })
        
        expected = 'uRRULLBBUFFBUbbuuBUbuBluuLfuFUUluuLUluLUUFUfuluLURUrufuFruRUBUbFURurURurfUUFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20041_AnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube with a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb'
        })
        
        expected = 'FFUURRULLBBFUfuRUruLUlUruRUfuFURUruuluLUFUfUruRUBUbubuBULUlFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20042_YetAnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube with a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg'
        })
        
        expected = 'FFLLBBRRuRUrbuBruuRUruRluLUluuLUluLFUfuluLUruRUBUbUbuBULUlUURUrufuFUUFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20050_ACubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube without a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo'
        })
        
        expected = 'FFlRuuFUluRRULLBBUFFbuuBufuFbuuBluLuruRLUluFUfuluLUBUburuRUULUlubuBUFURurfUUFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20051_AnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube without a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb'
        })
        
        expected = 'FLLuLLBBUBuRRFFLLBBUUFUfUBUbURUrufuFUUFUfuluLLUlubuBuLUlubuBBUburuRuBUburuRuFURurf'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
    
    def test_solve_20052_YetAnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube without a top daisy should yield correct solve directions """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        expected = 'FlbRuRRUfuRRUUBBUULLUUFFUUluuLfuFUUFUfuubuBubuBULUlBUburuRUfuFURUruBUburuR'
        
        self.assertIn('rotations', result)
        self.assertEqual(result['rotations'], expected)
        
    def test_solve_20060_ShouldYieldHashToken(self):
        """ solve result should yield hash token """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        self.assertIn('token', result)
        
    def test_solve_20061_ShouldYield8CharacterHashToken(self):
        """ yielded hash token should be 8 chars long """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        expectedTokenLength = 8
        actualTokenLength = len(result['token'])
        
        self.assertEqual(actualTokenLength, expectedTokenLength)
    
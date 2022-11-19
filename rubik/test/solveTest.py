
from unittest import TestCase

import rubik.solve as solve
import rubik.rotate as rotate
from rubik.cube import Cube
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
    
    
    def test_solve_20040_ShouldYieldHashToken(self):
        """ solve result should yield hash token """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        self.assertIn('token', result)
        
    def test_solve_20041_ShouldYield8CharacterHashToken(self):
        """ yielded hash token should be 8 chars long """
        
        result = solve._solve({
            'op': 'solve',
            'cube': 'owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby'
        })
        
        expectedTokenLength = 8
        actualTokenLength = len(result['token'])
        
        self.assertEqual(actualTokenLength, expectedTokenLength)
    
    def test_solve_30010_ACubeWithNoProgressShouldYieldCorrectRotationsToSolveDownCross(self):
        """ supplying a cube with no milestones reached should yield correct rotations to solve down cross """
        
        cubeCode = 'rorobgggbyrbyrywboyyorgowobywygoyrwrgborybgwbwrogwwwbg'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.hasDownCross())
        
    def test_solve_30020_ACubeWithUpDaisyShouldYieldCorrectRotationsToSolveDownCross(self):
        """ supplying a cube with up daisy should yield correct rotations to solve down cross """
        
        cubeCode = 'rowgbggbyrgyyrorrborgggywbwobgoorgryywbwywwwbrybywbooo'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.hasDownCross())
    
    def test_solve_30030_ACubeWithDownCrossShouldYieldCorrectRotationsToSolveDownCross(self):
        """ supplying a cube with down cross should yield correct rotations to solve down cross """
        
        cubeCode = 'ggorbowbrgbyyrbbryrywoggbgrrryyoggobbrgbyyoowowywwwwwo'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.hasDownCross())
    
    def test_solve_40010_ACubeWithNoProgressShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ supplying a cube with no reached milestones should yield correct rotations to solve down layer """
        
        cubeCode = 'bgoobybboyyorrwbrwggrggorrryoowoyybwbrwbygyogrywwwbgwg'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_solve_40020_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ supplying a cube with up daisy should yield correct rotations to solve down layer """
        
        cubeCode = 'bggrbowbgwrwgrbryobbyygyggboorgoyybgbwowywwworoyrworry'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_solve_40030_ACubeWithDownCrossShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ supplying a cube with down cross should yield correct rotations to solve down layer """
        
        cubeCode = 'ooyrbyobrgobrrbyrwrybrgyrggwybbogoobroygygwboywgwwwwwg'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isDownLayerSolved())
    
    def test_solve_40030_ACubeWithSolvedDownLayerShouldYieldCorrectDirectionsToSolveDownLayer(self):
        """ supplying a cube with solved down layer should yield correct rotations to solve down layer """
        
        cubeCode = 'yoobbbbbbyyrrrgrrryyorgogggbygboyoooygbryorggwwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isDownLayerSolved())
        
    def test_solve_50010_ACubeWithNoProgressShouldYieldCorrectDirectionsToSolveMiddleLayer(self):
        """ supplying a cube with no milestones reached should yield correct rotations to solve middle layer """
        
        cubeCode = 'wwygbgbgyowwyrborwbryogwbrrrogboogbrgboyyroobywgywywgr'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isMiddleLayerSolved())
        
    def test_solve_50020_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveMiddleLayer(self):
        """ supplying a cube with up daisy should yield correct rotations to solve middle layer """
        
        cubeCode = 'yoyobgwyyogrrrogrbwbgbgywygwrrgogyyrowgwywbwbbbrrwbooo'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isMiddleLayerSolved())
        
    def test_solve_50030_ACubeWithDownCrossShouldYieldCorrectDirectionsToSolveMiddleLayer(self):
        """ supplying a cube with down cross should yield correct rotations to solve middle layer """
        
        cubeCode = 'gobrbrbbgroggryorbygobggrgwybwyoyooygorryyrbyowwwwwbww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_solve_50040_ACubeWithSolvedDownLayerShouldYieldCorrectDirectionsToSolveMiddleLayer(self):
        """ supplying a cube with solved down layer should yield correct rotations to solve middle layer """
        
        cubeCode = 'ygrbbgbbbyyyyrbrrroyyrgogggrroyooooogrbgybgobwwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isMiddleLayerSolved())
        
    def test_solve_50050_ACubeWithSolvedDownAndMiddleLayersShouldYieldCorrectDirectionsToSolveMiddleLayer(self):
        """ supplying a cube with solved down, middle layers should yield correct rotations to solve middle layer """
        
        cubeCode = 'yyybbbbbbrbyrrrrrroooggggggyyroooooogybgyybrgwwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isMiddleLayerSolved())
    
    def test_solve_60010_ACubeWithNoProgressShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with no milestones reached should yield correct rotations to solve up face """
        
        cubeCode = 'wwobbywyryobgrrybgrrbggyoggywooorwrroyygybbogbbgwwwrow'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60020_ACubeWithUpDaisyShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with no milestones reached should yield correct rotations to solve up face """
        
        cubeCode = 'rbyobybyrggoorgyyrgobygbgooyrbrogbgwowwwywyworbgrwrwbw'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60030_ACubeWithDownCrossShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with down cross should yield correct rotations to solve up face """
        
        cubeCode = 'gbgybrobwygoyrgorybbwygorgrgoygoowogrrybyroyrwwbwwwbwb'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60040_ACubeWithSolvedDownLayerShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with solved down layer should yield correct rotations to solve up face """
        
        cubeCode = 'oyrbbybbbgybgryrrrroorgrgggyoygorooogbygyobbywwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60050_ACubeWithSolvedDownAndMiddleLayersShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with solved down and middle layers should yield correct rotations to solve up face """
        
        cubeCode = 'yyybbbbbbbgyrrrrrrrbbggggggyyooooooooygryygorwwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60060_ACubeWithSolvedDownMidLayersAndUpCrossShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with solved down, mid layers and up cross should yield correct rotations to solve up face """
        
        cubeCode = 'bbgbbbbbbyrgrrrrrroooggggggbgyooooooyyyyyyryrwwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    def test_solve_60070_ACubeWithSolvedDownMidLayersAndUpFaceShouldYieldCorrectDirectionsToSolveUpFace(self):
        """ supplying a cube with solved down, mid layers and up face should yield correct rotations to solve up face """
        
        cubeCode = 'borbbbbbbggbrrrrrrrbgggggggoroooooooyyyyyyyyywwwwwwwww'
        
        solveResult = solve._solve({
            'op': 'solve',
            'cube': cubeCode
        })
        solution = solveResult['rotations']
        
        cube = Cube(cubeCode)
        if len(solution) > 1:
            rotateResult = rotate._rotate({
                'cube': cubeCode,
                'dir': solution
            })
            
            cube = Cube(rotateResult['cube'])
        
        self.assertTrue(cube.isUpFaceSolved())
    
    

from unittest import TestCase

from rubik.cubeSolver import CubeSolver
from rubik.cubeFacePosition import CubeFacePosition
from rubik.faceRotationDirection import FaceRotationDirection

class CubeSolverTest(TestCase):
    
    # CubeSolver.__init__ -- POSITIVE TESTS
    
    def test_cubeSolver_init_10010_ShouldInstantiateCubeForValidCubeCode(self):
        """ supplying valid cube should instantiate cube solver """
        
        solver = CubeSolver('oboybbrrggrborywwroogggbygrooyyorbobygwwygbrwwwrywbywg')
        
        self.assertIsInstance(solver, CubeSolver)
    
    # CubeSolver.__init__ -- NEGATIVE TESTS
    
    def test_cubeSolver_init_20010_ShouldThrowExceptionForNonSuppliedCube(self):
        """ supplying no cube should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver()
    
    def test_cubeSolver_init_20020_ShouldTHrowExceptionForCubeOfInvalidType(self):
        """ supplying cube of invalid type should throw exception """
        
        with self.assertRaises(Exception):
            CubeSolver('not a cube')
    
    # CubeSolver.solve -- POSITIVE TESTS
    
    def test_cubeSolver_solve_10010_ASolvedCubeShouldYieldNoSolveDirections(self):
        """ an already solved cube should give no solve directions """
        
        solver = CubeSolver('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        solver.solve()
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10020_ACubeWithABottomCrossAlreadyShouldYieldNoSolveDirections(self):
        """ a cube with a bottom cross should give no solve directions """
        
        solver = CubeSolver('bowybbybrrgwrrgbrooywygbggwbrooorrorobggyoyybgwywwwgwy')
        solver.solve()
        
        expected = []
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10030_ACubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver('wryrbobgbgbybrgwbrogyrgyyogborrobogwrwbwywgworyoowywyg')
        solver.solve()
        
        expected = [
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10031_AnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver('wbyrbybgwrgyorbryrgooygrwowbrgyogorrywowywowgyogbwgbbb')
        solver.solve()
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10032_YetAnotherCubeWithTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube with a top daisy should yield correct solve directions """
        
        solver = CubeSolver('ybgobgbbbrrgyrgoyoogwrggwowbogooybyrowywywrwwyryrwbrbg')
        solver.solve()
        
        expected = [
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10040_ACubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ a cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver('owrwbwybyyywrrybygggorgbygwgbboogborwrrryowobgwogwbryo')
        solver.solve()
        
        expected = [
            # make up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10041_AnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ another cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver('yogrbyyoowobgrgbbrrygrgowgorybwowgbrwrybybogogywwwrywb')
        solver.solve()
        
        expected = [
            # make up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    def test_cubeSolver_solve_10042_YetAnotherCubeWithoutTopDaisyShouldYieldCorrectSolveDirections(self):
        """ yet another cube without a top daisy should yield correct solve directions """
        
        solver = CubeSolver('owyobygwwowyrrorygbgbbggrrbwwgroywywroroyrybbogggwboby')
        solver.solve()
        
        expected = [
            # make up daisy
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.LEFT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.BACK, FaceRotationDirection.COUNTERCLOCKWISE),
            
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.COUNTERCLOCKWISE),
            
            # make down cross
            (CubeFacePosition.UP, FaceRotationDirection.COUNTERCLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.RIGHT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.BACK, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.LEFT, FaceRotationDirection.CLOCKWISE),
            
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.UP, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE),
            (CubeFacePosition.FRONT, FaceRotationDirection.CLOCKWISE)
        ]
        
        self.assertEqual(solver.getDirections(), expected)
    
    # getDirections -- POSITIVE TESTS
    
    def test_cubeSolver_getDirections_10010_ShouldReturnValidDirections(self):
        """ should return list of type (CubeFacePosition, FaceRotationDirection) """
        
        solver = CubeSolver('gbogbobwowboyroyrygbrggrrwywwyyoygrwgowbyyorbrgbwwgrob')
        solver.solve()
        
        directions = solver.getDirections()
        
        # make sure directions is a list
        self.assertIsInstance(directions, list)
        
        for direction in directions:
            # make sure each direction is a tuple
            self.assertIsInstance(direction, tuple)
            
            # make sure each direction tuple has 2 items each
            self.assertEqual(len(direction), 2)
            
            # make sure each direction is of type (CubeFacePosition, FaceRotationDirection)
            (facePosition, rotationDirection) = direction
            
            self.assertIsInstance(facePosition, CubeFacePosition)
            self.assertIsInstance(rotationDirection, FaceRotationDirection)
    
    def test_cubeSolver_getDirections_10020_ShouldBeEmptyIfCubeNeverSolved(self):
        """ should return empty list if Cube.solve() never called """
        
        solver = CubeSolver('grwgbwyrygbbbrwgoywwwoggbgwooyrooorbggrbyyowrryrbwybyo')
        
        directions = solver.getDirections()
        
        self.assertEqual(len(directions), 0)
        
    def test_cubeSolver_getDirections_10030_ShouldNotCarryOverDirectionsFromPreviousSolves(self):
        """ each time solve is executed, the directions should be reset """
        
        solver = CubeSolver('ogrybwryywogorbggbogbygwwgbrrwbooowbyoybybgrgwrrrwwyyo')
        
        # solve a cube fully
        solver.solve()
        # then solve it again (even though it's already solved)
        solver.solve()
        
        # should yield no solve directions
        directions = solver.getDirections()
        
        self.assertEqual(len(directions), 0)
        
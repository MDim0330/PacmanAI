import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import search

import eightpuzzle

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.expected_actions=[
                ['left'],
                ['left', 'up', 'up', 'right', 'down', 'left', 'left', 
                 'down', 'right', 'right', 'up', 'left', 'up', 'right',
                 'down', 'left', 'left', 'down', 'right', 'right', 'up',
                 'left', 'up', 'left'],
                ['left', 'down', 'right', 'up', 'up', 'left', 'down', 
                 'right', 'up', 'left'],
                ['up', 'left', 'down', 'right', 'up', 'right', 'down', 
                 'left', 'up', 'left', 'down', 'right', 'up', 'left'],
                ['up', 'right', 'down', 'right', 'up', 'up', 'left', 'down', 
                'down', 'left', 'up', 'right', 'up', 'left'],
                ['right', 'right', 'down', 'down', 'left', 'up', 'right', 'down', 'left', 'left', 'up', 'up'],
            ]
        
        self.expected_actions_astar_manhatten=[
                ['left'],
                ['left', 'up', 'up', 'right', 'down', 'left', 'left', 
                 'down', 'right', 'right', 'up', 'left', 'up', 'right',
                 'down', 'left', 'left', 'down', 'right', 'right', 'up',
                 'left', 'up', 'left'],
                ['left', 'down', 'right', 'up', 'up', 'left', 'down', 
                 'right', 'up', 'left'],
                ['up', 'left', 'down', 'right', 'up', 'right', 'down', 
                 'left', 'up', 'left', 'down', 'right', 'up', 'left'],
                ['up', 'right', 'down', 'right', 'up', 'up', 'left', 'down', 
                'down', 'left', 'up', 'right', 'up', 'left'],
                ['right', 'right', 'down', 'left', 'down', 'right', 'up', 'left', 'down', 'left', 'up', 'up'],
            ]

    @weight(2)
    @number("1.1")
    def test_11_ucs(self):
        """UCS EightPuzzle"""
        expected_expands = [6, 152459, 1240, 6264, 5661, 2749]
        ee_tol = [20, 5000, 100, 500, 500, 200]
        for i in range(6):
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            #print(problem.getStartState())
            path, expands = search.uniformCostSearch(problem)
            self.assertEqual(self.expected_actions[i], path,'UCS path incorrect for puzzle' + 
                str(i) + "\n" + str(puzzle))
            self.assertTrue(
                expected_expands[i] - ee_tol[i] <= expands <= expected_expands[i] + ee_tol[i],
                'UCS tiles expected expands not within tolerance.  Expected:' +
                str(expected_expands[i]) + ' actual:' + str(expands))

    @weight(1)
    @number("1.2")
    def test_12_astar_tiles_heuristic(self):
        """A* Tile heuristic test"""
        # test heuristic function
        tiles_heuristic=[2, 9, 6, 5, 9, 8]
        for i in range(6):
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            hx = search.tilesEightPuzzleHeuristic(puzzle,problem)
            self.assertEqual(tiles_heuristic[i], hx, 
                "tiles heuristic error on puzzle\n" + str(puzzle) + "\n")

    @weight(1)
    @number("1.3")
    def test_13_astar_manhatten_heuristic(self):
        """A* manhatten heuristic test"""
        # test heuristic function
        manhatten_heuristic=[2, 18, 12, 10, 14, 12]
        for i in range(6):
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            hx = search.manhattenEightPuzzleHeuristic(puzzle,problem)
            self.assertEqual(manhatten_heuristic[i], hx, 
                "manhatten heuristic error on puzzle\n" + str(puzzle) + "\n")


    @weight(1)
    @number("1.4")
    def test_14_astar_tiles(self):
            """A* EightPuzzle w/tiles"""
            expected_expands = [3, 27070, 102, 500, 434, 121]
            ee_tol = [10, 10, 10, 10, 10, 10 ]
            for i in range(6):
                puzzle = eightpuzzle.loadEightPuzzle(i)
                problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
                path, expands = search.aStarSearch(problem, search.tilesEightPuzzleHeuristic)

                self.assertEqual(self.expected_actions[i], path, 'A* tiles path incorrect for puzzle' + 
                    str(i) + "\n" + str(puzzle))
                self.assertTrue(
                    expected_expands[i] - ee_tol[i] <= expands <= expected_expands[i] + ee_tol[i],
                    'A* tiles expected expands not within tolerance.  Expected:' +
                    str(expected_expands[i]) + ' actual:' + str(expands))

    @weight(1)
    @number("1.5")
    def test_15_astar_manhatten(self):
            """A* EightPuzzle w/manhatten"""

            expected_expands = [4, 4427, 36, 171, 85, 61]
            ee_tol = [10, 10, 10, 10, 10, 10 ]
            for i in range(6):
                puzzle = eightpuzzle.loadEightPuzzle(i)
                problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
                path, expands = search.aStarSearch(problem, search.manhattenEightPuzzleHeuristic)

                self.assertEqual(self.expected_actions_astar_manhatten[i], path, 
                  'A* manhatten path incorrect for puzzle' + str(i) + "\n" + str(puzzle))
                self.assertTrue(
                    expected_expands[i] - ee_tol[i] <= expands <= expected_expands[i] + ee_tol[i],
                    'A* manhatten expected expands not within tolerance.  Expected:' +
                    str(expected_expands[i]) + ' actual:' + str(expands))

if __name__ == "__main__":
    unittest.main()
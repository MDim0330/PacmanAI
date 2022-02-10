import unittest
import search
import eightpuzzle


class SearchTests(unittest.TestCase):
    def test_bfs(self):
        expected_actions = [
            ['left'],
            ['left', 'up', 'left', 'down', 'right', 'right', 'up',
             'left', 'down', 'left', 'up'],
            ['left', 'down', 'right', 'up', 'up', 'left', 'down',
             'right', 'up', 'left'],
            ['up', 'left', 'down', 'right', 'up', 'right', 'down',
             'left', 'up', 'left', 'down', 'right', 'up', 'left']
        ]

        for i in [0, 2, 3]:
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            print(problem.getStartState())
            path = search.breadthFirstSearch(problem)
            self.assertEqual(expected_actions[i], path)

    def d_test_dfs(self):
        expected_actions=[
            ['left'],
            ['up', 'left', 'left', 'up', 'right', 'down', 'right',
             'down', 'left', 'left', 'up', 'right', 'up'],
            ['left', 'down', 'right', 'up', 'up', 'left', 'down',
              'right', 'up', 'left']
        ]

        for i in [0,3]:
            puzzle = eightpuzzle.loadEightPuzzle(i)
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            print(problem.getStartState())
            path = search.depthFirstSearch(problem,14)
            path = search.breadthFirstSearch(problem)

            print(i, path)
            self.assertEqual(expected_actions[i], path)

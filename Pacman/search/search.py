# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from collections import namedtuple
from itertools import count
import util
import queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = queue.Queue()
    return whatever_first_search(problem, frontier)
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    return aStarSearch(problem, nullHeuristic)
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

Node = namedtuple('Node', ['state', 'action', 'cost', 'futurecost'])
def aStarSearch(problem, heuristic=nullHeuristic):
    start = Node(problem.getStartState(), [], 0, 0)
    
    frontier = queue.PriorityQueue()
    unique = count()
    reached = {}
    
    if problem.isGoalState(start.state): 
        return start.action, 0
    
    frontier.put((start.cost + heuristic(start.state, problem), next(unique), start))
    c = 1
    
    while frontier.not_empty:
        node = frontier.get()[2]
        if problem.isGoalState(node.state):
            return node.action, c
        for state, action, cost in problem.getSuccessors(node.state): 
            if state not in reached or node.cost + cost < reached[state]:
                reached[state] = node.cost + cost
                t_node = Node(state, node.action + [action], node.cost + cost, heuristic(state, problem))
                frontier.put((t_node.cost + heuristic(t_node.state, problem), next(unique), t_node))
                c = c + 1           
    return problem
    #util.raiseNotDefined()


def whatever_first_search(problem, frontier):

    # Create a tuple for ease-of-use
    Node = namedtuple('Node', ['state', 'path', 'cost', 'futurecost'])

    # Get the starting state of problem
    node = Node(problem.getStartState(), [], 0)

    # Check for the frontier already being in the goal state
    if problem.isGoalState(node.state):
        return []

    # Reached/Initial actions of the node
    reached = {}

    # Add the starting node to the queue
    frontier.put(node)

    curr_cost = 0

    # Iterator through the children and find the optimal pathing for solving
    while not frontier.empty():
        # Pop of queue
        node = frontier.get()
        # Split successors into a tuple and assign to vars to prevent overwrite
        for state, action, cost in problem.getSuccessors(node.state):
            s = state
            if problem.isGoalState(s):
                return node.action + [action]
            if s not in reached:
                # reached.append(state)
                reached[state] = True
                temp_node = Node(state, node.action+[action], node.cost + cost)
                frontier.put(temp_node)
    return problem

correct = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]
def tilesEightPuzzleHeuristic (state, problem):
    cells = state.cells
    c = 0
    for x in range(3):
        for y in range(3):
            if (cells[x][y] != correct[x][y]):
                c = c + 1
    return c
# HNode = namedtuple('HNode', ['fx', 'steps', 'node'])
# # Used for uniform and A-Star
# def best_first_search(problem, frontier, hueristic):   
#     node = Node(problem.getStartState(), 0, )

def findCoords (value):
    for x in range(3):
        for y in range(3):
            if (correct[x][y] == value):
                return x, y
    return 0, 0

def manhattenEightPuzzleHeuristic (state, problem):
    cells = state.cells
    c = 0
    for x in range(3):
        for y in range(3):
            if cells[x][y] != correct[x][y]:
                tx, ty = findCoords(cells[x][y])
                c += abs(x - tx) + abs(y - ty)
    return c     

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch



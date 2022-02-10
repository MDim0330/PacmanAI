"""
    Purpose: example code for plotting results w/Matplotlib
    Author: Kevin Molloy (molloykp@jmu.edu)
"""

import numpy as np
import matplotlib.pyplot as plt
import eightpuzzle
import search

x = [0, 1, 2, 3, 4, 5]

# plt.plot(x,y1,label="Method 1", color="red",lw=3)
# plt.plot(x,y2,label="Method 2", color="blue",lw=3)
plt.xlabel("8-Puzzle Number", fontsize=16)
plt.ylabel("Expand Count", fontsize=16)
plt.xticks(x)
plt.legend(fontsize=16)
usc = []
man = []
tiles = []
for i in range (6):
    puzzle = eightpuzzle.loadEightPuzzle(i)
    problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
    path, expanded = search.uniformCostSearch(problem)
    usc.append(expanded)
for i in range (6):
    puzzle = eightpuzzle.loadEightPuzzle(i)
    problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
    path, expanded = search.aStarSearch(problem, search.tilesEightPuzzleHeuristic)
    tiles.append(expanded)
for i in range (6):
    puzzle = eightpuzzle.loadEightPuzzle(i)
    problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
    path, expanded = search.aStarSearch(problem, search.manhattenEightPuzzleHeuristic)
    man.append(expanded)
plt.plot(x,usc,label="UCS", color="blue",lw=3)
plt.plot(x,tiles,label="AStar Tiles", color="red",lw=3)
plt.plot(x,man,label="AStar Manhatten", color="green",lw=3)
plt.legend()
plt.show()  # you can use to display while modifying this script
plt.savefig(fname='searchAnalysis.pdf', dpi=300,
            bbox_inches='tight',pad_inches=0.05)
plt.close()




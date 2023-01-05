import time
import sys

from function import type

board = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]

def functionMove(board, moving): #the board is the board. moving is an array where moving[0]][moving][1] is the index for the 2d board array to point to a speciic square.
    movingColor = board[moving[0]][moving][1] #hopefully either 1 or 2. if someone asked for nothing to move then it would be 0.
    for 
    
import time
import sys

from function import type

class piece:
    def __init__ (self,player,type):
        self.player = player
        self.type = type

class move:
    def __init__(self,target,position,victim):
        self.target = target #the piece you are moving
        self.position = position
        self.victim = victim

board = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]
realBoard = []
for q in range(len(board)):
    realBoard.append([])
    for j in range(len(board[q])):
        if board[q][j] == 1:
            realBoard.append(tile(1, 'pawn'))
        if board[q][j] == 2:
            realBoard.append(tile(2, 'pawn'))
        if board[q][j] == 0:
            realBoard.append(None)
def findAllMoves(board)
def findMove(board, moving): #the board is the board. moving is an array where moving[0]][moving][1] is the index for the 2d board array to point to a speciic square.
    movingPiece = board[moving[0]][moving][1] #hopefully either 1 or 2. if someone asked for nothing to move then it would be 0.
    if movingPiece.player == 1:
        checkingFor = 2
        direction = 1
    if movingPiece.player == 2:
        checkingFor = 1
        direction = -1
    if movingPiece.type == 'king':
        for i in range(4):

    if movingPiece.type == 'pawn':
        if board[moving[0]+direction][moving][1]]:
    
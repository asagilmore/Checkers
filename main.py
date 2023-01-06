import time
import sys

from function import type

class piece:
    def __init__ (self,player,type):
        self.player = player
        self.type = type

class move:
    def __init__(self,target,position,victim):
        self.target = target # [x,y] of target
        self.position = position # [x,y] of position that target moves too
        self.victim = victim # [x,y] of victim if true, else None

    
#board as [y][x]
board = [[None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn')],
         [piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None], 
         [None, None, None, None, None, None, None, None],
         [None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn')], 
         [piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None]]

def findMoves(board,player):
    moves = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != None: #if tile not empty
                if board[y][x].player == player: #if piece is players 
                    #do top left
                    if (x-1 >= 0) and (y-1 >= 0): #check tile exists
                        if board[y-1][x-1] == None:
                            moves.append(move([x,y],[x-1,y-1],None))
                        if board[y-1][x-1].player != player: #piece is not players
                            if board[y-2][x-2] == None: #if piece has open spot to jump too
                                moves.append(move([x,y],[x-2,y-2],[x-1,y-1])) 
                        



                        



# def findAllMoves(board):
#     return

# def findMove(board, moving): #the board is the board. moving is an array where moving[0]][moving][1] is the index for the 2d board array to point to a speciic square.
#     movingPiece = board[moving[0]][moving][1] #hopefully either 1 or 2. if someone asked for nothing to move then it would be 0.
#     if movingPiece.player == 1:
#         checkingFor = 2
#         direction = 1
#     if movingPiece.player == 2:
#         checkingFor = 1
#         direction = -1
#     if movingPiece.type == 'king':
#         for i in range(4):

#     if movingPiece.type == 'pawn':
#         if board[moving[0]+direction][moving][1]]:
    
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
         [None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn')],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None], 
         [piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None],
         [None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn')], 
         [piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None]]

def findMoves(board,player):
    moves = []

    #Get all moves
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != None: #if tile not empty
                if board[y][x].player == player: #if piece is players 
                    moves.extend(checkPiece(board,player,x,y))

    #check for jump and remove 
    for i in moves:
        if i.victim != None: #if jump move exists
            for j in moves:
                if j.victim == None:
                    moves.remove(j)

    return moves
                                
def checkPiece(board,player,x,y): #returns all possible moves for a piece on board, 

    moves = []


    #check for error
    if board[y][x] == None:
        print(f'error passed empty tile to checkPiece @ x:{x} y:{y}')
        return moves
    if board[y][x].player != player:
        print(f'error passed tile of wrong player to checkPiece  @ x:{x} y:{y}')
        return moves

    #do top left
    if inRange(x-1,y-1): #check tile exists
        if board[y-1][x-1] == None: #if spot empty
            if player == 2 or board[x][y].type == 'king': #if able to move in direction
                moves.append(move([x,y],[x-1,y-1],None))
        if board[y-1][x-1].player != player: #piece is not players
            if inRange(x-2,y-2):
                if board[y-2][x-2] == None: #if piece has open spot to jump too
                    moves.append(move([x,y],[x-2,y-2],[x-1,y-1])) 
    #do top right
    if inRange(x+1,y-1): #check tile exists
        if board[y-1][x+1] == None: #if spot empty
            if player == 2 or board[x][y].type == 'king': #if able to move in direction
                moves.append(move([x,y],[x+1,y-1],None))
        if board[y-1][x+1].player != player: #piece is not players
            if inRange(x+2,y-2):
                if board[y-2][x+2] == None: #if piece has open spot to jump too
                    moves.append(move([x,y],[x+2,y-2],[x+1,y-1])) 
    #do bottom left
    if inRange(x-1,y+1): #check tile exists
        if board[y+1][x-1] == None: #if spot empty
            if player == 1 or board[x][y].type == 'king': #if able to move in direction
                moves.append(move([x,y],[x-1,y+1],None))
        if board[y+1][x-1].player != player: #piece is not players
            if inRange(x-2,y+2):
                if board[y+2][x-2] == None: #if piece has open spot to jump too
                    moves.append(move([x,y],[x-2,y+2],[x-1,y+1])) 
    #do bottom right
    if inRange(x+1,y+1): #check tile exists
        if board[y+1][x+1] == None: #if spot empty
            if player == 1 or board[x][y].type == 'king': #if able to move in direction
                moves.append(move([x,y],[x+1,y+1],None))
        if board[y+1][x+1].player != player: #piece is not players
            if inRange(x+2,y+2):
                if board[y+2][x+2] == None: #if piece has open spot to jump too
                    moves.append(move([x,y],[x+2,y+2],[x+1,y+1])) 

    return moves
                        
def inRange(x,y):
    if (8 >= x >= 0) and (8 >= y >= 0):
        return True
    else: 
        return False

def flipBoard(board):

    #flip x
    for i in board:
        i.reverse()

    #flip y
    board.reverse()

    #switch players
    for i in board:
        for j in i:
            if piece.player == 1:
                piece.player = 2
            if piece.player == 2:
                piece.player =1
    
    return board

def doMove(move,board): #returns 2d board array

    board[move.position[1]][move.position[0]] = board[move.target[1]][move.target[0]]

    board[move.target[1]][move.target[0]] = None

    if move.victim != None:
        board[move.victim[1]][move.victim[0]] = None

    return board

def checkScore(board): #returns #piecesP1 - #piecesP2
    scoreP1 = 0
    scoreP2 = 0
    for i in board:
        for x in board:
            if x != None:
                if x.player == 1:
                    scoreP1 += 1
                if x.player == 2:
                    scoreP2 += 1
    return (scoreP1 - scoreP2)
 

                        



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
    
import time
import sys
import random

class piece:
    def __init__ (self,player,type):
        self.player = player
        self.type = type

class move:
    def __init__(self,target,position,victim,becomeKing):
        self.target = target # [x,y] of target
        self.position = position # [x,y] of position that target moves too
        self.victim = victim # [x,y] of victim if true, else None
        self.becomeKing = becomeKing #bool


    
#board as [y][x]
board = [[None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn')],
         [piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None],
         [None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn'), None, piece(1,'pawn')],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None], 
         [piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None],
         [None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn')], 
         [piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None, piece(2,'pawn'), None]]

def inRange(x,y):
    if (7 >= x >= 0) and (7 >= y >= 0):
        return True
    else: 
        return False

def findMoves(board,player):
    moves = [] 

    #Get all moves
    for y in range(8):
        for x in range(8):
            if board[y][x] != None: #if tile not empty
                if board[y][x].player == player: #if piece is players 
                    moves.extend(checkPiece(board,player,[x,y]))

    #check for jump and remove 
    for i in moves:
        if i.victim != None: #if jump move exists 
            for j in moves:
                if j.victim == None:
                    moves.remove(j)

    return moves
                                
def checkPiece(board,player,target): #returns all possible moves for a piece on board, 


    moves = []
    x = target[0]
    y = target[1]

    # #check for error
    if board[y][x] == None:
        print(f'error passed empty tile to checkPiece @ x:{x} y:{y}')
        return moves
    if board[y][x].player != player:
        print(f'error passed tile of wrong player to checkPiece  @ x:{x} y:{y}')
        return moves

    #do top left
    topLeft = checkTile(board,player,[x,y],[-1,-1])
    if topLeft != None:
        moves.append(topLeft) 
    #do top right
    topRight = checkTile(board,player,[x,y],[1,-1])
    if topRight != None:
        moves.append(topRight) 
    #do bottom left
    bottomLeft = checkTile(board,player,[x,y],[-1,1])
    if bottomLeft != None:
        moves.append(bottomLeft) 
    #do bottom right
    bottomRight = checkTile(board,player,[x,y],[1,1])
    if bottomRight != None:
        moves.append(bottomRight)   

    return moves

def checkTile(board,player,target,direction): #target as [x,y], direction as [+/-1,+/-1]
    x = target[0]
    y = target[1]

    if inRange(x+direction[0],y+direction[1]): #check tile exists
        if board[y+direction[1]][x+direction[0]] == None: #if spot empty


            if ( (y-(y+direction[1])) > 0 and player == 2) or ( (y-(y+direction[1])) < 0 and player == 1) or board[y][x].type == 'king': 


                if player == 2 and y+direction[1] == 0:
                    return move([x,y],[x+direction[0],y+direction[1]],None,True)
                if player == 1 and y+direction[1] == 7:
                    return move([x,y],[x+direction[0],y+direction[1]],None,True)
                else:
                    return move([x,y],[x+direction[0],y+direction[1]],None,False)
        elif board[y+direction[1]][x+direction[0]].player != player: #piece is not players
            if inRange(x+(direction[0]*2),y+(direction[1]*2)):
                if board[y+(direction[1]*2)][x+(direction[0]*2)] == None: #if piece has open spot to jump too 
                    if player == 2 and (y+(direction[1]*2)) == 0:
                        return move([x,y],[x+(direction[0]*2),y+(direction[1]*2)],[x+direction[0],y+direction[1]],True)
                    if player == 1 and (y+direction[1]*2) == 7:
                        return move([x,y],[x+(direction[0]*2),y+(direction[1]*2)],[x+direction[0],y+direction[1]],True)
                    else:
                        return move([x,y],[x+(direction[0]*2),y+(direction[1]*2)],[x+direction[0],y+direction[1]],False)
    
    return None

def flipBoard(board):

    #flip x
    for i in board:
        i.reverse()

    #flip y
    board.reverse()

    #switch players
    for i in board:
        for j in i:
            if j != None:
                if j.player == 2:
                    j.player = 1
                elif j.player == 1:
                    j.player = 2

    return board

def doMove(move,board): #returns 2d board array

    board[move.position[1]][move.position[0]] = board[move.target[1]][move.target[0]]

    if move.becomeKing:
        board[move.position[1]][move.position[0]].type = 'king'

    board[move.target[1]][move.target[0]] = None

    if move.victim != None:
        board[move.victim[1]][move.victim[0]] = None

    return board

def checkScore(board): #returns #piecesP1 - #piecesP2
    scoreP1 = 0
    scoreP2 = 0
    for i in board:
        for x in i:
            if x != None:
                if x.player == 1:
                    scoreP1 += 1
                if x.player == 2:
                    scoreP2 += 1
    return[scoreP1,scoreP2]

def draw(board):
    sys.stdout.write("\x1b[2J\x1b[H")
    num = 1
    for i in board:
        sys.stdout.write("\033[0;37;39m" + str(num) + " ")
        for j in i:
            if j == None:
                sys.stdout.write("\033[0;37;39m" + "▢")
            else:
                if j.player == 1:
                    if j.type == 'pawn':
                        sys.stdout.write("\033[0;31;40m" + "▣")
                    else:
                        sys.stdout.write("\033[0;31;40m" + "◩")   
                if j.player == 2:
                    if j.type == 'pawn':
                        sys.stdout.write("\033[0;36;40m" + "▣")
                    else:
                        sys.stdout.write("\033[0;36;40m" + "◩")
            sys.stdout.write(" ")
        num = num + 1
        sys.stdout.write("\n")
    sys.stdout.write("  1 2 3 4 5 6 7 8\n")

def doTurn(board):
    p1Moves = findMoves(board,1)
    board = doMove(p1Moves[ random.randrange(0,len(p1Moves)) ], board)
    draw(board)
    time.sleep(0.5)
    p2Moves = findMoves(board,2)
    board = doMove(p2Moves[ random.randrange(0,len(p2Moves)) ], board)    
    draw(board)
    time.sleep(0.5)
    return(board)

if __name__ == '__main__':
    while True:
        board = doTurn(board)
        draw(board)


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
    
# def checkPiece(board,player,target): #returns all possible moves for a piece on board, 


#     moves = []
#     x = target[0]
#     y = target[1]

#     # #check for error
#     if board[y][x] == None:
#         print(f'error passed empty tile to checkPiece @ x:{x} y:{y}')
#         return moves
#     if board[y][x].player != player:
#         print(f'error passed tile of wrong player to checkPiece  @ x:{x} y:{y}')
#         return moves

#     #do top left
#     if inRange(x-1,y-1): #check tile exists
#         if board[y-1][x-1] == None: #if spot empty
#             if player == 2 or board[y][x].type == 'king': #if able to move in direction
#                 moves.append(move([x,y],[x-1,y-1],None))
#         elif board[y-1][x-1].player != player: #piece is not players
#             if inRange(x-2,y-2):
#                 if board[y-2][x-2] == None: #if piece has open spot to jump too
#                     moves.append(move([x,y],[x-2,y-2],[x-1,y-1])) 
#     #do top right
#     if inRange(x+1,y-1): #check tile exists
#         if board[y-1][x+1] == None: #if spot empty 
#             if player == 2 or board[y][x].type == 'king': #if able to move in direction
#                 moves.append(move([x,y],[x+1,y-1],None))
#         elif board[y-1][x+1].player != player: #piece is not players
#             if inRange(x+2,y-2):
#                 if board[y-2][x+2] == None: #if piece has open spot to jump too
#                     moves.append(move([x,y],[x+2,y-2],[x+1,y-1])) 
#     #do bottom left
#     if inRange(x-1,y+1): #check tile exists
#         if board[y+1][x-1] == None: #if spot empty
#             if player == 1 or board[y][x].type == 'king': #if able to move in direction
#                 moves.append(move([x,y],[x-1,y+1],None))
#         elif board[y+1][x-1].player != player: #piece is not players
#             if inRange(x-2,y+2):
#                 if board[y+2][x-2] == None: #if piece has open spot to jump too
#                     moves.append(move([x,y],[x-2,y+2],[x-1,y+1])) 
#     #do bottom right
#     if inRange(x+1,y+1): #check tile exists
#         if board[y+1][x+1] == None: #if spot empty
#             if player == 1 or board[y][x].type == 'king': #if able to move in direction
#                 moves.append(move([x,y],[x+1,y+1],None))
#         elif board[y+1][x+1].player != player: #piece is not players
#             if inRange(x+2,y+2):
#                 if board[y+2][x+2] == None: #if piece has open spot to jump too
#                     moves.append(move([x,y],[x+2,y+2],[x+1,y+1])) 
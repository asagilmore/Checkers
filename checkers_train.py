import checkers
from network import Network
from layers import Layer,Activation_Layer,Connected_Layer
import cost
import activation

from save import save,load

import numpy as np

def translateBoard(board): #converts to 1d array [empty,player1,player2,isKing] (note: stored as 1d string of numbers, not nested arrays)
    output = []

    for row in board:
        for tile in row:
            if tile == None:
                output +=  [1,0,0,0]
            else:
                output.append(0) #not empty
                if tile.player == 1:
                    output += [1,0]
                else:
                    output += [0,1]
                if tile.type == 'king':
                    output.append(1)
                else:
                    output.append(0)

    return np.array(output)

def playCycle(games,net):
    data_train = []
    data_answer = []
    for i in range(games):
        boardsP1 = []
        boardsP2 = []
        board = checkers.board 
        
        while True:
            score = checkers.checkScore(board)
            if score[0] == 0 or score[1] == 0:
                return
            doTurn(board,net)

def doTurn(board,net): #does turn for p1 only
    moveBoards = []
    netConfidence = []
    moves = checkers.findMoves(board)

    for move in moves:
        moveBoards.append(checkers.doMove(move,board))
    
    for i in moveBoards:
        net.




net = Network()

net.add(Connected_Layer(256,256))
net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
net.add(Connected_Layer(256,256))
net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
net.add(Connected_Layer(256,256))
net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
net.add(Connected_Layer(256,128))
net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
net.add(Connected_Layer(128,1))
net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))



#def playCycle(games,net):

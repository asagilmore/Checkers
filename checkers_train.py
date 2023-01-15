import checkers
from network import Network
from layers import Layer,Activation_Layer,Connected_Layer
import cost
import activation
import random

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
        winner = 0
        
        while score[0] != 0 and score[1] != -0: #do game
            score = checkers.checkScore(board)

            if score[0] == 0:
                winner = 1
                return
            if score[1] == 0:
                winner = 2
                return 

            board = doTurn(board,net)
            checkers.flipBoard(board)
            boardsP1.append(board)  

            if score[0] == 0:
                winner = 2
                return
            if score[1] == 0:
                winner = 1
                return 

            board = doTurn(board,net)
            checkers.flipBoard(board) 
            boardsP2.append(board)
        
        #append data_train and data_awnser
        if winner == 0:
            return ValueError
        elif winner == 1:

            data_train.extend(boardsP1)
            for i in range(len(data_train)):
                data_answer.append(1)

            data_train.extend(boardsP2)
            for i in range(len(data_train)):
                data_answer.append(0)
        elif winner == 2:

            data_train.extend(boardsP2)
            for i in range(len(data_train)):
                data_answer.append(1)

            data_train.extend(boardsP1)
            for i in range(len(data_train)):
                data_answer.append(0)

    return [data_train,data_answer]



        
        
    
def doTurn(board,net): #does turn for p1 only
    moveBoards = []
    netConfidence = []
    moves = checkers.findMoves(board)

    for move in moves:
        moveBoards.append(checkers.doMove(move,board))
    
    for i in moveBoards:
        netConfidence.append(net.predict(translateBoard(i)))
    
    return np.random.choice(a=moveBoards,size=1,p=netConfidence)

    






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

data = playCycle(10,net)

training_set = data[0]

answer_set = data[1]

print(training_set)
print(answer_set)


#def playCycle(games,net):

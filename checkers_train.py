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
        score = [1,1]
        while score[0] != 0 and score[1] != 0: #do game
            turn = 1
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
            print(f'playing game turn:{turn}, score:{score}')
        
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
    moves = checkers.findMoves(board,1)

    for move in moves:
        moveBoards.append(checkers.doMove(move,board))
    
    for i in moveBoards:
        prediction = net.predict([translateBoard(i)])
        print(prediction)
        netConfidence.append(prediction[0][0][0]) #this is pretty ugly, but idk why net.predict is returns a ton of nested arrays, anyway just bandaid solution here but it works
    print(netConfidence)
    choice = np.random.choice(a=moveBoards,size=1,p=netConfidence) #this is currently the problem, idk how we should randomly choose the move
    return choice

    
def weightedChoice(confidences):
    denom = 1/sum(confidences)
    weighted = np.dot(confidences,denom)
    sumSoFar = 0
    for i in range(len(weighted)):
        newWeight = weighted[i]+sumSoFar
        sumSoFar+=weighted[i]
        weighted[i] = newWeight
    newFloat = random.random()
    found = False
    for i in range(len(weighted)):
      if found == False and newFloat < weighted[i]:
        found = True
        move = i
    return(move)

print(weightedChoice([0.2, 0.4, 0.4]))


net = Network()

net.add(Connected_Layer(256,256))
net.add(Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))
net.add(Connected_Layer(256,1))
net.add(Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))

if __name__ == "__main__":
    translated = translateBoard(checkers.board)
    print(translated)
    print(net.predict([translated]))
    
#def playCycle(games,net):

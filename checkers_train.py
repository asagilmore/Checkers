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
def reverseTranslateBoard(translateBoard):
    output = []
    for i in translateBoard/4:
        if translateBoard[i*4] == 0:
            output.append(None)
        else:
            if translateBoard[i*4+1] == 1:
                player = 1
            else:
                player = 2
            if translateBoard[i*4+3] == 1:
                type = 'king'
            else:
                type = 'pawn'
            output.append(checkers.piece(player, type))
def playCycle(games,net):
    data_train = []
    data_answer = []
    for i in range(games):
        boardsP1 = []
        boardsP2 = []
        board = checkers.board 
        winner = 0
        score = checkers.checkScore(board)
        turn = 1

        while score[0] != 0 and score[1] != 0: #do game
            
            score = checkers.checkScore(board)

            board = doTurn(board,net)
            boardsP1.append(board)  
            checkers.flipBoard(board)

            board = doTurn(board,net)
            boardsP2.append(board)
            checkers.flipBoard(board) 
            print(f'playing game turn:{turn}, score:{score}')
            turn += 1

        if score[0] == 0:
            winner = 2
            return
        if score[1] == 0:
            winner = 1
            return 

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
        boardToChange = []
        for i in range(len(board)):
            boardToChange.append(board[i])
        moveBoards.append(checkers.doMove(move,boardToChange))
    
    for i in moveBoards:
        netConfidence.append(net.predict(translateBoard(i)))
    
    return moveBoards[weightedChoice(netConfidence)]

    
def weightedChoice(confidences):
    #print(confidences)
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
    save(net,"network_0")
    for i in range(1,2):
        net = load("network_" + str(i-1))
        trainingData = playCycle(100,net)
        net.train(trainingData[0],trainingData[1],1000,0.01)
        save(net,"network_"+str(i))
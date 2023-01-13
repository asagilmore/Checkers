def turnBoardToNeuralNetInput(board):
  newBoard = []
  for i in range(8):
    for l in range(8):
      if (l%2 == 1 and i%2 == 0) or (l%2 == 0 and i%2 == 1):
        if board[i][l] == None:
          newBoard.append(0)
        else:
          if board[i][l].player == 1:
            mult = 0
          else:
            mult = 1
          if board[i][l].type == 'king':
            num = 1
          else:
            num = 0
          newBoard.append(1+2*mult+num)
          #if it is 0 then it is empty. if it is 4 then it is an opponent king. if it is a 3 then it is an opponent pawn. if it is a 2 then it is a computer king. if it is a 1 then it is a computer pawn.

layer1 = Layer(32, 32)
layer2 = Layer(32, 1)
input = np.random.rand(32)
output = layer1.forward_prop(input)
print(output)
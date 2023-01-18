import network 
import activation
import cost
import layers
import numpy as np
import checkers
from checkers_train import translateBoard
if __name__ == '__main__':
  net = network.Network()
  net.setCost(cost.MSE,cost.MSE_derivative)

  net.add(layers.Connected_Layer(256,256))
  net.add(layers.Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))
  net.add(layers.Connected_Layer(256,1))
  net.add(layers.Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))

  board = checkers.board
  print(translateBoard(board))
  prediction = net.predict(translateBoard(board))
  print(prediction)
import numpy as np
import main
import numpy as np

#we will have the network imputs as the board state, and the output be a single confidence value for the given move
#then we basiaclly have it play against itself, and if it looses it will assume all moves it made were bad and should have been a 0 and vice versa for a win
#we then train the weights for each move given the output and expected value


def ReLU(x):
    return max(0,x)

def sigmoid(x):
    return 1 /(1 + np.exp(-x))


class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    # computes the output Y of a layer for a given input X
    def forward_propagation(self, input):
        raise NotImplementedError

    # computes dE/dX for a given dE/dY (and update parameters if any)
    def backward_propagation(self, output_error, learning_rate):
        raise NotImplementedError
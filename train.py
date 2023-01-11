import numpy as np
import main

#we will have the network imputs as the board state, and the output be a single confidence value for the given move
#then we basiaclly have it play against itself, and if it looses it will assume all moves it made were bad and should have been a 0 and vice versa for a win
#we then train the weights for each move given the output and expected value


def ReLU(x):
    return max(0,x)

def sigmoid(x):
    return 1 /(1 + np.exp(-x))


class Layer:
    def __init__(self,num_inputs,num_outputs):
        self.weight = np.random.rand(num_inputs,num_outputs)
        self.bias = np.random.rand(1,num_outputs)
    def forward_prop(self,input_data):
        self.input = input_data
        self.output = np.dot(self.input,self.weight) + self.bias
        return self.output
    
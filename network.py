import numpy as np
import layers

#we will have the network imputs as the board state, and the output be a single confidence value for the given move
#then we basiaclly have it play against itself, and if it looses it will assume all moves it made were bad and should have been a 0 and vice versa for a win
#we then train the weights for each move given the output and expected value


def cost_function(prediction,expected):
    return np.mean(np.power(expected-prediction,2)) # average of (expected-predicted)^2

def cost_function_derivative(prediction,expected):
    return 2*(prediction-expected)/expected.size

class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_derivative = None
    
    def add(self,layer):
        self.layers.append(layer)
    
    def lossFunction(self,loss,loss_derivative):
        self.loss = loss
        self.loss_derivative = loss_derivative
    
 

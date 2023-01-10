import numpy as np
import main
import numpy as np

#we will have the network imputs as the board state, and the output be a confidence value for the given move

def ReLU(x):
    return max(0,x)

def sigmoid(x):
    return 1 /(1 + np.exp(-x))
    


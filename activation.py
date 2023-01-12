import numpy as np

def ReLU(x):
    return max(0,x)

def ReLU_Derivative(x):
    if x <= 0:
        return 0
    else:
        return 1

def sigmoid(x):
    return 1 /(1 + np.exp(-x))

def sigmoid_derivative(x):
    return np.exp(-x)/ (1+np.exp(-x))^2 

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1-np.tanh(x)**2

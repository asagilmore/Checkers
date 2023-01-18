import numpy as np

def ReLU(x):
    return np.maximum(0,x)

def ReLU_derivative(x):
    return np.where(x>0,1,0) #sets range of array to 0,1, rounds any non 0 to 1 

leakySlope = 0.05

def LeakyReLU(x):
    return np.where(x>0,x,x*leakySlope)

def LeakyReLU_derivative(x):
    return np.where(x>0,1,leakySlope)

def sigmoid(x):
    return 1 /(1 + np.exp(-x))

def sigmoid_derivative(x):
    return np.exp(-x)/ (1+np.exp(-x))**2 

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1-np.tanh(x)**2


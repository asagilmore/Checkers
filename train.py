import numpy as np
import main

#we will have the network imputs as the board state, and the output be a single confidence value for the given move
#then we basiaclly have it play against itself, and if it looses it will assume all moves it made were bad and should have been a 0 and vice versa for a win
#we then train the weights for each move given the output and expected value

##Activation functions and their derivatives


def ReLU(x):
    return max(0,x)

def ReLU_Derivative(x):
    if x < 0:
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

def cost_function(prediction,expected):
    return np.mean(np.power(expected-prediction,2)) # average of (expected-predicted)^2

def cost_function_derivative(prediction,expected):
    return 2*(prediction-expected)/expected.size

#Gloabals

learning_rate = 0.001

class Layer:
    def __init__(self,num_inputs,num_outputs):
        self.weight = np.random.rand(num_inputs,num_outputs)
        self.bias = np.random.rand(1,num_outputs)
    def forward_prop(self,input_data):
        self.input = input_data
        self.output = np.dot(self.input,self.weight) + self.bias
        return self.output
    def backward_prop(self,output_error,learning_rate):
        return NotImplementedError

class Activation_Layer:
    def __init__(self,activation,activation_derivative):
        self.activation = activation
        self.activation_derivative = activation_derivative
    def forward_prop(self,input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output
    def backward_prop(self,output_error,learning_rate):
        return self.activation_derivative(self.input) * output_error

class Network:

 

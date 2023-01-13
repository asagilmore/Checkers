import numpy as np

class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    def forward_propagation(self,input):
        return NotImplementedError
    def backward_propagation(self,input):
        return NotImplementedError


class Connected_Layer(Layer):
    def __init__(self,num_inputs,num_outputs):
        self.weights = np.random.rand(num_inputs,num_outputs)
        self.bias = np.random.rand(1,num_outputs)
    def forward_propagation(self,input_data):
        self.input = input_data
        self.output = np.dot(self.input,self.weights) + self.bias
        return self.output
    def backward_propagation(self,output_error,learning_rate):
        #calculate errors
        input_error = np.dot(output_error,self.weights.T)
        weight_error = np.dot(self.input.T,output_error)

        #apply and return
        self.weights -= learning_rate * weight_error
        self.bias -= learning_rate * output_error
        return input_error


        

class Activation_Layer(Layer):
    def __init__(self,activation,activation_derivative):
        self.activation = activation
        self.activation_derivative = activation_derivative
    def forward_propagation(self,input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output
    def backward_propagation(self,output_error,learning_rate): #returns derivative of error with respect to derivative of activation, basically gets output error of previous layer for input error of activation layer
        return self.activation_derivative(self.input) * output_error

class Convolution_Layer(Layer):
    def __init__(self,num_inputs,batch_size): #batch size must be divisible by num of inputs, 
        return NotImplementedError
    
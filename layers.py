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
        self.weights = np.random.rand(num_inputs,num_outputs) - 0.5 
        self.bias = np.random.rand(1,num_outputs) - 0.5
    def forward_propagation(self,input_data):
        self.input = input_data
        self.output = np.dot(self.input,self.weights) + self.bias
        return self.output
    def backward_propagation(self,output_error,learning_rate):
        #calculate errors
        print(f'backward propagating')
        print(f'self.input {self.input} output_error{output_error}')
        output_error = output_error.reshape(-1)
        self.input = self.input.reshape(-1)
        if output_error.shape[0]==1:
            output_error = output_error[0]       
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
    
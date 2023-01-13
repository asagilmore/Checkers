import numpy as np
import layers

#we will have the network imputs as the board state, and the output be a single confidence value for the given move
#then we basiaclly have it play against itself, and if it looses it will assume all moves it made were bad and should have been a 0 and vice versa for a win
#we then train the weights for each move given the output and expected value

class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_derivative = None
    
    def add(self,layer):
        self.layers.append(layer)
    
    def setCost(self,cost,cost_derivative):
        self.cost = cost
        self.cost_derivative = cost_derivative
    
    def predict(self,input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        
        return result
    
    def train(self, input_data, output_data, interations, learning_rate): #output_data is true/expected result of input_data

        samples = len(input_data)

        for i in range(interations):
            err = 0
            for j in range(samples):

                output = input_data[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)
                
                err += self.loss(output,output_data[j])

                error = self.loss_derivative(output_data[j],output)

                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error,learning_rate)
            
            err /= samples #average error


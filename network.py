import numpy as np

class Network:
    def __init__(self):
        self.layers = []
        self.cost = None
        self.cost_derivative = None
    
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
                
                err += self.cost(output,output_data[j])

                error = self.cost_derivative(output_data[j],output)

                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error,learning_rate)
            
            err /= samples #average error   
            print('iteration %d/%d   error=%f' % (i+1, interations, err))

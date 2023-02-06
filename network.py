import numpy as np
import math
import random
import ipdb

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
    
    def predictList(self,input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers: #propagate through layers in network
                output = layer.forward_propagation(output)
            result.append(output)
        
        return result
    
    def predict(self,input_data):
        output = input_data
        for layer in self.layers:
            output = layer.forward_propagation(output)
        return output[0][0]
    def train(self, input_data, output_data, iterations, learning_rate): #output_data is true/expected result of input_data #batch_size as % of input data to train on

        input_data = np.array(input_data)
        samples = len(input_data)

        for i in range(iterations):

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
            print('iteration %d/%d   error=%f' % (i+1, iterations, err))

    def batchTrain(self, input_data, output_data, iterations, learning_rate, batch_size): #output_data is true/expected result of input_data #batch_size as % of input data to train on
        
        if len(input_data) != len(output_data): #make sure input and output data is matched
            return error

        training_data = np.array([[input_data[i],output_data[i]] for i in range(len(input_data))])
        batch_len = math.floor(len(training_data)*batch_size)

        for i in range(iterations):

            err = 0
            random.shuffle(training_data)
            error = np.zeros(len(output_data[0])) 
            for j in range(batch_len):
                
                output = training_data[j][0]

                for layer in self.layers:
                    output = layer.forward_propagation(output)
                
                err += self.cost(output,training_data[j][1])
                error += self.cost_derivative(training_data[j][1],output[0])

            error = np.divide(error,batch_len) #average error
            for layer in reversed(self.layers):
                error = layer.backward_propagation(error,learning_rate)
            
            err /= batch_len #average error   
            print('iteration %d/%d   error=%f' % (i+1, iterations, err))


#for in
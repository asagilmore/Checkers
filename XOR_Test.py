from network import Network
from layers import Layer,Activation_Layer,Connected_Layer
from cost import cost_function,cost_function_derivative
import activation

import numpy as np


input_data = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
output_data = np.array([[[0]], [[1]], [[1]], [[0]]])



net = Network()
net.add(Connected_Layer(2,3))
net.add(Activation_Layer(activation.LeakyReLU,activation.LeakyReLU_Derivative))
net.add(Connected_Layer(3,1))
net.add(Activation_Layer(activation.LeakyReLU,activation.LeakyReLU_Derivative))


net.setCost(cost_function,cost_function_derivative)
net.train(input_data,output_data,interations=10000,learning_rate=0.01)

out = net.predict(input_data)
print(out)
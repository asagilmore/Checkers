from network import Network
from layers import Layer,Activation_Layer,Connected_Layer
import cost
import activation

from save import save,load

import numpy as np


input_data = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
output_data = np.array([[[0]], [[1]], [[1]], [[0]]])

if __name__ == '__main__':

    net = Network()
    net.add(Connected_Layer(2,50))
    net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
    net.add(Connected_Layer(50,50))
    net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))
    net.add(Connected_Layer(50,1))
    net.add(Activation_Layer(activation.tanh,activation.tanh_derivative))

    print(f'test {net.predict([1,1])}')
    net.setCost(cost.MSE,cost.MSE_derivative)
    net.train(input_data,output_data,interations=100,learning_rate=0.1)

    out = net.predict([0,0])
    print(out)

    save(net,"XOR.pkl")

    net = load("XOR.pkl")

    out = net.predictList(input_data)
    print(out)
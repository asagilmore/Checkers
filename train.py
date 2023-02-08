from network import Network
from layers import layer, Connected_Layer,Activation_Layer
from cost import MSE,MSE_derivative,MAE_derivative,MAE
from activation import tanh,tanh_derivative,sigmoid,sigmoid_derivative
from save import save

if __name__ == '__main__':
    net = Network()
    net.setCost(MSE,MSE_derivative)
    net.add(Connected_Layer(36608,73216))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(73216,73216))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(73216,73216))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(73216,36608))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(36608,18304))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(18304,4))
    net.add(Activation_Layer(sigmoid,sigmoid_derivative))


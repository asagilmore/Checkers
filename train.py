from network import Network
from layers import Layer, Connected_Layer,Activation_Layer
from cost import MSE,MSE_derivative,MAE_derivative,MAE
from activation import tanh,tanh_derivative,sigmoid,sigmoid_derivative
from save import save
import image

if __name__ == '__main__':
    net = Network()
    net.setCost(MAE,MAE_derivative)
    net.add(Connected_Layer(36608,36608))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(36608,18304))
    net.add(Activation_Layer(tanh,tanh_derivative))
    net.add(Connected_Layer(18304,1))
    net.add(Activation_Layer(sigmoid,sigmoid_derivative))
    
    data_train = []
    data_train.append(image.toArray('moderateDem0.jpg'))
    data_train.append(image.toArray('nonDem0.jpg'))
    data_answer = [1,0]

    print(data_train,data_answer)
    net.train(data_train,data_answer,1000,0.01)
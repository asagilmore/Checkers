import network 
import activation
import cost
import layers
import numpy as np
if __name__ == '__main__':
  net = network.Network()
  net.setCost(cost.MSE,cost.MSE_derivative)

  net.add(layers.Connected_Layer(50,50))
  net.add(layers.Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))
  net.add(layers.Connected_Layer(50,1))
  net.add(layers.Activation_Layer(activation.sigmoid,activation.sigmoid_derivative))
  testdata = np.random.rand(50)
  print(f'zeros : {testdata}')
  prediction = net.predict(testdata)
  print(prediction)
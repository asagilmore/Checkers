import checkers
import activation
import layers as layer
import numpy as np

act_layer = layer.Activation_Layer(activation.sigmoid,activation.sigmoid_derivative)


print(act_layer.activation(100))




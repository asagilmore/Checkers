import numpy as np

def cost_function(prediction,expected):
    return np.mean(np.power(expected-prediction,2)) # average of (expected-predicted)^2

def cost_function_derivative(prediction,expected):
    return 2*(prediction-expected)/expected.size
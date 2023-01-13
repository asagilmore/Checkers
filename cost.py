import numpy as np

def cost_function(expected,prediction):
    return np.mean(np.power(expected-prediction,2)) # average of (expected-predicted)^2

def cost_function_derivative(expected,prediction):
    return 2*(prediction-expected)/expected.size
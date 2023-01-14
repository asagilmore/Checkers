import numpy as np

def MSE(expected,prediction):
    return np.mean(np.power(expected-prediction,2)) # average of (expected-predicted)^2

def MSE_derivative(expected,prediction):
    return 2*(prediction-expected)/expected.size

def MAE(expected,prediction):
    return np.abs(np.subtract(expected,prediction)) # abs(pre - expected)

def MAE_derivative(expected,prediction):
    return np.where(prediction > expected,1,-1) # if pred > true = +1 if true > pred = -1

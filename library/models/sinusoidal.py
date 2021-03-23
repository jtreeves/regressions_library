from numpy import sin
from scipy.optimize import curve_fit

def sinusoidal_function(variable, a, b, c, d):
    return a * sin(b * (variable - c)) + d

inputs = [2.0, 3.0, 5.0, 7.0, 11.0, 13.0, 17.0, 19.0]
outputs = [5.0, 6.0, 8.0, 7.0, 4.0, 3.0, 1.0, 3.0]

parameters, parameters_covariance = curve_fit(sinusoidal_function, inputs, outputs)

parameters_list = list(parameters)

print(parameters_list)
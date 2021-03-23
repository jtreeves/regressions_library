from numpy import sin
from scipy.optimize import curve_fit
from library.statistics.correlation import correlation

def sinusoidal_function(variable, a, b, c, d):
    return a * sin(b * (variable - c)) + d

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputs = []

for i in range(len(inputs)):
    outputs.append(sinusoidal_function(inputs[i], 2, 3, 5, 7))

parameters, parameters_covariance = curve_fit(sinusoidal_function, inputs, outputs)

parameters_list = list(parameters)

print(f'COEFFICIENTS: {parameters_list}')

predicted = []

for i in range(len(inputs)):
    predicted.append(sinusoidal_function(inputs[i], *parameters_list))

print(f'PREDICTED: {predicted}')

accuracy = correlation(outputs, predicted, 4)

print(f'CORRELATION: {accuracy}')
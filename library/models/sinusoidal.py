from numpy import sin
from scipy.optimize import curve_fit
from library.statistics.correlation import correlation

def sinusoidal_function(variable, a, b, c, d):
    return a * sin(b * (variable - c)) + d

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputs = []

for i in range(len(inputs)):
    outputs.append(sinusoidal_function(inputs[i], 2, 3, 5, 7))

print(f'OUTPUTS: {outputs}')
# [8.07314583600087, 6.175763029516487, 7.558830996397852, 6.717759983880265, 7.0, 7.282240016119735, 6.441169003602148, 7.824236970483513, 5.92685416399913, 8.300575680314234]

parameters, parameters_covariance = curve_fit(sinusoidal_function, inputs, outputs)

parameters_list = list(parameters)

print(f'COEFFICIENTS: {parameters_list}')
# SHOULD BE: [2, 3, 5, 7]
# ACTUALLY IS: [0.4440909946304321, 1.904153085572008, 6.333112388074118, 7.1248334760089405]

predicted = []

for i in range(len(inputs)):
    predicted.append(sinusoidal_function(inputs[i], *parameters_list))

print(f'PREDICTED: {predicted}')
# SHOULD BE: [8.07314583600087, 6.175763029516487, 7.558830996397852, 6.717759983880265, 7.0, 7.282240016119735, 6.441169003602148, 7.824236970483513, 5.92685416399913, 8.300575680314234]
# ACTUALLY IS: [7.421078394773893, 6.715269197719326, 7.096621209136528, 7.5528608115194915, 6.872930244775667, 6.861660095461743, 7.548966227331635, 7.110440105456048, 6.71012023093585, 7.410629155659941]

accuracy = correlation(outputs, predicted, 4)

print(f'CORRELATION: {accuracy}')
# SHOULD BE: 1.0
# ACTUALLY IS: 0.4105
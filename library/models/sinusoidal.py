from numpy import sin
from scipy.optimize import curve_fit
from library.statistics.correlation import correlation

def sinusoidal_function(variable, a, b, c, d):
    return a * sin(b * (variable - c)) + d

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputs = [8.0731, 6.1758, 7.5588, 6.7178, 7, 7.2822, 6.4412, 7.8242, 5.9269, 8.3006]

parameters, parameters_covariance = curve_fit(sinusoidal_function, inputs, outputs)

parameters_list = list(parameters)

print(parameters_list)

predicted = []

for i in range(len(inputs)):
    predicted.append(sinusoidal_function(inputs[i], *parameters_list))

print(f'PREDICTED: {predicted}')

accuracy = correlation(outputs, predicted, 4)

print(f'CORRELATION: {accuracy}')

def exponential_function(variable, a, b):
    return a * b ** variable

logarithmic_set = [
    [1, 2],
    [2, 4.0794],
    [3, 5.2958],
    [4, 6.1589],
    [5, 6.8283],
    [6, 7.3753],
    [7, 7.8377],
    [8, 8.2383],
    [9, 8.5917],
    [10, 8.9078]
]

log_in = []
log_out = []

for i in range(len(logarithmic_set)):
    log_in.append(logarithmic_set[i][0])
    log_out.append(logarithmic_set[i][1])

print(log_in)
print(log_out)

pmt, pmtcv = curve_fit(exponential_function, log_in, log_out)

print(pmt)
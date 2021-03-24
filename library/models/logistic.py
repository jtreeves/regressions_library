from numpy import exp
from scipy.optimize import curve_fit
from library.statistics.correlation import correlation

def logistic_function(variable, first_constant, second_constant, third_constant):
    evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
    return evaluation

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputs = []

for i in range(len(inputs)):
    outputs.append(logistic_function(inputs[i], 2, 3, 5))

print(f'OUTPUTS: {outputs}')
# [1.2288349204429436e-05, 0.00024678915197246345, 0.004945246313269549, 0.09485174635513356, 1.0, 1.9051482536448667, 1.9950547536867307, 1.9997532108480274, 1.9999877116507956, 1.999999388195546]

parameters, parameters_covariance = curve_fit(logistic_function, inputs, outputs)

parameters_list = list(parameters)

print(f'COEFFICIENTS: {parameters_list}')
# SHOULD BE: [2, 3, 5]
# ACTUALLY IS: [2.0, 3.000000000000002, 5.0]

predicted = []

for i in range(len(inputs)):
    predicted.append(logistic_function(inputs[i], *parameters_list))

print(f'PREDICTED: {predicted}')
# SHOULD BE: [1.2288349204429436e-05, 0.00024678915197246345, 0.004945246313269549, 0.09485174635513356, 1.0, 1.9051482536448667, 1.9950547536867307, 1.9997532108480274, 1.9999877116507956, 1.999999388195546]
# ACTUALLY IS: [1.2288349204429326e-05, 0.0002467891519724617, 0.004945246313269527, 0.09485174635513335, 1.0, 1.9051482536448667, 1.9950547536867307, 1.9997532108480274, 1.9999877116507956, 1.999999388195546]

accuracy = correlation(outputs, predicted, 4)

print(f'CORRELATION: {accuracy}')
# SHOULD BE: 1.0
# ACTUALLY IS: 1.0
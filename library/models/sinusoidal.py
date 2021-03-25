from numpy import sin, inf
from scipy.optimize import curve_fit
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.sinusoidal import sinusoidal as sinusoidal_equation
from library.analyses.derivatives.sinusoidal import sinusoidal as sinusoidal_derivative
from library.analyses.integrals.sinusoidal import sinusoidal as sinusoidal_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation
from library.statistics.rounding import rounding
from library.statistics.halve import halve_dimension
from library.statistics.mean import mean

def sinusoidal(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    dependent_min = min(dependent_variable)
    dependent_max = max(dependent_variable)
    solution = []
    def sinusoidal_fit(variable, first_constant, second_constant, third_constant, fourth_constant):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    parameters, parameters_covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(-inf, -inf, -inf, dependent_min), (inf, inf, inf, dependent_max)])
    solution = list(parameters)
    constants = []
    for number in solution:
        constants.append(rounding(number, precision))
    equation = sinusoidal_equation(*solution)
    derivative = sinusoidal_derivative(*solution)
    integral = sinusoidal_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('sinusoidal', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value, precision)
    accumulated_iqr = accumulation(integral, q1, q3, precision)
    averages_range = average_values('sinusoidal', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('sinusoidal', equation, integral, q1, q3, solution, precision)
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted, precision)
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    points = {
        'roots': points['roots'],
        'maxima': points['maxima'],
        'minima': points['minima'],
        'inflections': points['inflections']
    }
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    averages = {
        'range': averages_range,
        'iqr': averages_iqr
    }
    result = {
        'constants': constants,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result

test_set = [[1, 3], [2, 8], [3, 3], [4, -2], [5, 3], [6, 8], [7, 3], [8, -2], [9, 3], [10, 8]]
test_run = sinusoidal(test_set, 4)
print(test_run)
# {'constants': [-5.7369, 0.236, -1.2046, 8.0], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x127615670>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x127615790>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x127615820>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 29.5431, 'iqr': 12.9525}, 'averages': {'range': {'average_value_derivative': 0.0128, 'mean_values_derivative': [5.4112, 5.4913, '5.4913 + 26.6236k', '5.4112 + 26.6236k'], 'average_value_integral': 3.2826, 'mean_values_integral': [2.8861, 8.0164, '2.8861 + 26.6236k', '8.0164 + 26.6236k']}, 'iqr': {'average_value_derivative': 0.0147, 'mean_values_derivative': [5.4052, 5.4973, '5.4973 + 26.6236k', '5.4052 + 26.6236k'], 'average_value_integral': 2.5905, 'mean_values_integral': [4.0127, 6.8898, '4.0127 + 26.6236k', '6.8898 + 26.6236k']}}, 'correlation': 0.3081}
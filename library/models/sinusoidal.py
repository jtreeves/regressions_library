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
    dependent_max = max(dependent_variable)
    dependent_min = min(dependent_variable)
    dependent_range = dependent_max - dependent_min
    solution = []
    def sinusoidal_fit(variable, first_constant, second_constant, third_constant, fourth_constant):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    parameters, parameters_covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(-1 * dependent_range, -inf, -inf, dependent_min), (dependent_range, inf, inf, dependent_max)])
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
# {'constants': [-5.0, 1.5708, 3.0, 3.0], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x125fcb940>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x125fcba60>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x125fcbaf0>}, 'points': {'roots': [[3.4097, 0], [4.5903, 0], [7.4097, 0], [8.5903, 0], [11.4097, 0], [12.5903, 0], ['3.4097 + 4.0k', 0], ['4.5903 + 4.0k', 0]], 'maxima': [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]], 'minima': [[4.0, -2.0], [8.0, -2.0], [12.0, -2.0], ['4.0 + 4.0k', -2.0]], 'inflections': [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], [11.0, 3.0], ['3.0 + 2.0k', 3.0]]}, 'accumulations': {'range': 30.1831, 'iqr': 11.8169}, 'averages': {'range': {'average_value_derivative': 0.5556, 'mean_values_derivative': [3.9549, 4.0451, 7.9549, 8.0451, '4.0451 + 4.0k', '3.9549 + 4.0k'], 'average_value_integral': 3.3537, 'mean_values_integral': [2.9549, 5.0451, 6.9549, 9.0451, '2.9549 + 4.0k', '5.0451 + 4.0k']}, 'iqr': {'average_value_derivative': -1.0, 'mean_values_derivative': [3.9187, 4.0813, 7.9187, '3.9187 + 4.0k', '4.0813 + 4.0k'], 'average_value_integral': 2.3634, 'mean_values_integral': [3.0813, 4.9187, 7.0813, '3.0813 + 4.0k', '4.9187 + 4.0k']}}, 'correlation': 1.0}
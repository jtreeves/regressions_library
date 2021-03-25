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
    solution = []
    def sinusoidal_fit(variable, first_constant, second_constant, third_constant, fourth_constant):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    parameters, parameters_covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable)
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
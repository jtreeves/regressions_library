from numpy import exp, inf
from scipy.optimize import curve_fit
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.logistic import logistic as logistic_equation
from library.analyses.derivatives.logistic import logistic as logistic_derivative
from library.analyses.integrals.logistic import logistic as logistic_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation
from library.statistics.rounding import rounding
from library.statistics.halve import halve_dimension
from library.statistics.mean import mean

def logistic(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    halved_data = halve_dimension(data, 1)
    dependent_lower = dimension(halved_data['lower'], 2)
    dependent_upper = dimension(halved_data['upper'], 2)
    mean_lower = mean(dependent_lower)
    mean_upper = mean(dependent_upper)
    dependent_max = max(dependent_variable)
    dependent_min = min(dependent_variable)
    dependent_range = dependent_max - dependent_min
    solution = []
    def logistic_function(variable, first_constant, second_constant, third_constant):
        evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
        return evaluation
    if mean_upper >= mean_lower:
        parameters, parameters_covariance = curve_fit(logistic_function, independent_variable, dependent_variable, bounds=[(dependent_max - dependent_range, 0, -inf), (dependent_max + dependent_range, inf, inf)])
        solution = list(parameters)
    else:
        parameters, parameters_covariance = curve_fit(logistic_function, independent_variable, dependent_variable, bounds=[(dependent_max - dependent_range, -inf, -inf), (dependent_max + dependent_range, 0, inf)])
        solution = list(parameters)
    constants = []
    for number in solution:
        constants.append(rounding(number, precision))
    equation = logistic_equation(*solution)
    derivative = logistic_derivative(*solution)
    integral = logistic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('logistic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value, precision)
    accumulated_iqr = accumulation(integral, q1, q3, precision)
    averages_range = average_values('logistic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('logistic', equation, integral, q1, q3, solution, precision)
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
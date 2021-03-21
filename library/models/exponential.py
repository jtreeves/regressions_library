from math import log, exp
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.derivatives.exponential import exponential as exponential_derivative
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation
from library.statistics.rounding import rounding

def exponential(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i], 1])
        dependent_matrix.append([log(dependent_variable[i])])
    solution = solve(independent_matrix, dependent_matrix, precision)
    constants = [exp(solution[1]), exp(solution[0])]
    coefficients = [rounding(constants[0], precision), rounding(constants[1], precision)]
    equation = exponential_equation(*coefficients)
    derivative = exponential_derivative(*coefficients)
    integral = exponential_integral(*coefficients)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('exponential', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value, precision)
    accumulated_iqr = accumulation(integral, q1, q3, precision)
    averages_range = average_values('exponential', equation, integral, min_value, max_value, coefficients, precision)
    averages_iqr = average_values('exponential', equation, integral, q1, q3, coefficients, precision)
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
        'constants': coefficients,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result
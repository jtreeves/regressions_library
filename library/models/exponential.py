from math import log, exp
from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.unify import unify
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.roots.exponential import exponential as exponential_roots
from library.analyses.derivatives.exponential import exponential as exponential_derivative
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.extrema import extrema as extrema_independent
from library.analyses.inflections import inflections as inflections_independent
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.maximum import maximum
from library.statistics.minimum import minimum
from library.statistics.quartiles import quartiles
from library.statistics.correlation import correlation

def exponential(data):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i], 1])
        dependent_matrix.append([log(dependent_variable[i])])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution_column = multiplication(second_product, dependent_matrix)
    solution = dimension(solution_column, 1)
    constants = [exp(solution[1]), exp(solution[0])]
    equation = exponential_equation(constants[0], constants[1])
    derivative = exponential_derivative(constants[0], constants[1])
    integral = exponential_integral(constants[0], constants[1])['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    roots = exponential_roots(constants[0], constants[1])
    zeroes = []
    for i in range(len(roots)):
        zeroes.append(0)
    root_coordinates = unify(roots, zeroes)
    extrema_inputs = extrema_independent('exponential', constants, first_derivative)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    inflections_inputs = inflections_independent('exponential', constants, second_derivative)
    maxima_outputs = []
    maxima_coordinates = []
    minima_outputs = []
    minima_coordinates = []
    inflections_outputs = []
    inflections_coordinates = []
    if maxima_inputs[0] == None:
        maxima_coordinates = [None]
    else:
        for i in range(len(maxima_inputs)):
            maxima_outputs.append(equation(maxima_inputs[i]))
        maxima_coordinates = unify(maxima_inputs, maxima_outputs)
    if minima_inputs[0] == None:
        minima_coordinates = [None]
    else:
        for i in range(len(minima_inputs)):
            minima_outputs.append(equation(minima_inputs[i]))
        minima_coordinates = unify(minima_inputs, minima_outputs)
    if inflections_inputs[0] == None:
        inflections_coordinates = [None]
    else:
        for i in range(len(inflections_inputs)):
            inflections_outputs.append(equation(inflections_inputs[i]))
        inflections_coordinates = unify(inflections_inputs, inflections_outputs)
    min_value = minimum(independent_variable)
    max_value = maximum(independent_variable)
    q1 = quartiles(independent_variable, 1)
    q3 = quartiles(independent_variable, 3)
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    averages_range = average_values('exponential', equation, integral, min_value, max_value, constants)
    averages_iqr = average_values('exponential', equation, integral, q1, q3, constants)
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted)
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    points = {
        'roots': root_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
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

# test_set = [[3, 7], [5, 19], [10, 84], [15, 231]]
# test_eval = exponential(test_set)
# print(test_eval)
from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.vectors.unify import unify
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.cubic import cubic as cubic_equation
from library.analyses.roots.cubic import cubic as cubic_roots
from library.analyses.derivatives.cubic import cubic as cubic_derivative
from library.analyses.integrals.cubic import cubic as cubic_integral
from library.analyses.extrema import extrema as extrema_independent
from library.analyses.inflections import inflections as inflections_independent
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.maximum import maximum
from library.statistics.minimum import minimum
from library.statistics.quartiles import quartiles
from library.statistics.correlation import correlation

def cubic(data):
    print(f'DATA: {data}')
    independent_variable = dimension(data, 1)
    print(f'INDEPENDENT_VARIABLE: {independent_variable}')
    dependent_variable = dimension(data, 2)
    print(f'DEPENDENT_VARIABLE: {dependent_variable}')
    independent_matrix = []
    dependent_matrix = column(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i]**3, independent_variable[i]**2, independent_variable[i], 1])
    print(f'INDEPENDENT_MATRIX: {independent_matrix}')
    print(f'DEPENDENT_MATRIX: {dependent_matrix}')
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    print(f'SECOND_PRODUCT: {second_product}')
    solution_column = multiplication(second_product, dependent_matrix)
    solution = dimension(solution_column, 1)
    print(f'SOLUTION: {solution}')
    equation = cubic_equation(solution[0], solution[1], solution[2], solution[3])
    roots = cubic_roots(solution[0], solution[1], solution[2], solution[3])
    derivative = cubic_derivative(solution[0], solution[1], solution[2], solution[3])
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    extrema_inputs = extrema_independent('cubic', solution, first_derivative)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    maxima_outputs = []
    minima_outputs = []
    maxima_coordinates = []
    minima_coordinates = []
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
    inflections_inputs = inflections_independent('cubic', solution, second_derivative)
    inflections_outputs = []
    inflections_coordinates = []
    if inflections_inputs[0] == None:
        inflections_coordinates = [None]
    else:
        for i in range(len(inflections_inputs)):
            inflections_outputs.append(equation(inflections_inputs[i]))
        inflections_coordinates = unify(inflections_inputs, inflections_outputs)
    zeroes = []
    for i in range(len(roots)):
        zeroes.append(0)
    root_coordinates = unify(roots, zeroes)
    points = {
        'roots': root_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
    }
    integral = cubic_integral(solution[0], solution[1], solution[2], solution[3])['evaluation']
    min_value = minimum(independent_variable)
    max_value = maximum(independent_variable)
    q1 = quartiles(independent_variable, 1)
    q3 = quartiles(independent_variable, 3)
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    averages_range = average_values('cubic', equation, integral, min_value, max_value, solution)
    averages_iqr = average_values('cubic', equation, integral, q1, q3, solution)
    averages = {
        'range': averages_range,
        'iqr': averages_iqr
    }
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted)
    result = {
        'constants': solution,
        'correlation': accuracy,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages
    }
    return result

test_set = [[2, 3], [4, 27], [8, 1], [11, 15], [13, 52]]
test_solution = cubic(test_set)
print(f'RESULT: {test_solution}')
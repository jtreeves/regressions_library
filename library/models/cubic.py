from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.cubic import cubic as cubic_equation
from library.analyses.roots.cubic import cubic as cubic_roots
from library.analyses.integrals.cubic import cubic as cubic_integral
from library.analyses.accumulation import accumulation
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
    points = {
        'roots': roots
    }
    integral = cubic_integral(solution[0], solution[1], solution[2], solution[3])
    min_value = minimum(independent_variable)
    max_value = maximum(independent_variable)
    q1 = quartiles(independent_variable, 1)
    q3 = quartiles(independent_variable, 3)
    accumulated_range = accumulation(integral['evaluation'], min_value, max_value)
    accumulated_iqr = accumulation(integral['evaluation'], q1, q3)
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted)
    result = {
        'constants': solution,
        'evaluation': equation,
        'correlation': accuracy,
        'accumulations': accumulations,
        'points': points
    }
    return result

test_set = [[2, 3], [4, 7], [8, 9], [11, 11]]
test_solution = cubic(test_set)
print(f'RESULT: {test_solution}')
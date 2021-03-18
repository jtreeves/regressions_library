from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.cubic import cubic as cubic_equation
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
    solution = multiplication(second_product, dependent_matrix)
    print(f'SOLUTION: {solution}')
    equation = lambda x: solution[0][0]*x**3 + solution[1][0]*x**2 + solution[2][0]*x + solution[3][0]
    # inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        # 'error': inaccuracy
    }
    return result

test_set = [[2, 3], [4, 7], [8, 9], [11, 11]]
test_solution = cubic(test_set)
print(f'RESULT: {test_solution}')
from numpy import matrix
from numpy.linalg import inv
from library.statistics.rounding import rounded_value
from library.vectors.dimension import single_dimension
from .multiplication import matrix_product
from .transpose import adjugate

def system_solution(matrix_one, matrix_two, precision):
    transposition = adjugate(matrix_one)
    product = matrix_product(transposition, matrix_one)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = matrix_product(inversion_list, transposition)
    solution_column = matrix_product(second_product, matrix_two)
    solution = single_dimension(solution_column, 1)
    result = []
    for number in solution:
        result.append(rounded_value(number, precision))
    return result
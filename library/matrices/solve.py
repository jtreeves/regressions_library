from numpy import matrix
from numpy.linalg import inv
from library.statistics.rounding import rounding
from library.vectors.dimension import dimension
from .multiplication import multiplication
from .transpose import transpose

def solve(matrix_one, matrix_two, precision):
    transposition = transpose(matrix_one)
    product = multiplication(transposition, matrix_one)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution_column = multiplication(second_product, matrix_two)
    solution = dimension(solution_column, 1)
    result = []
    for number in solution:
        result.append(rounding(number, precision))
    return result
from library.errors.matrices import matrix_of_scalars, level
from library.errors.scalars import positive_integer

def single_dimension(matrix, scalar):
    matrix_of_scalars(matrix, 'first')
    positive_integer(scalar)
    level(matrix, scalar)
    result = []
    for i in range(len(matrix)):
        result.append(matrix[i][scalar - 1])
    return result
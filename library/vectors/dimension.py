from library.errors.matrices import matrix_of_scalars, level
from library.errors.scalars import positive_integer

def single_dimension(matrix, scalar):
    matrix_of_scalars(matrix, 'first')
    positive_integer(scalar)
    level(matrix, scalar)
    result = []
    for element in matrix:
        result.append(element[scalar - 1])
    return result
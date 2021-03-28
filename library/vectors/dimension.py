from library.errors.matrices import matrix_of_scalars, level
from library.errors.scalars import positive_integer

def single_dimension(vector, scalar):
    matrix_of_scalars(vector, 'first')
    positive_integer(scalar)
    level(vector, scalar)
    result = []
    for i in range(len(vector)):
        result.append(vector[i][scalar - 1])
    return result
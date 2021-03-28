from library.errors.matrices import nested, level
from library.errors.scalars import integer

def single_dimension(vector, scalar):
    nested(vector)
    integer(scalar)
    level(vector, scalar)
    result = []
    for i in range(len(vector)):
        result.append(vector[i][scalar - 1])
    return result
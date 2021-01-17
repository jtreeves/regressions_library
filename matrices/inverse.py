from .scalar import scalar, scalar_3d
from .determinant import determinant, determinant_3d
from .transpose import transpose_3d
from .minors import minors
from .cofactors import cofactors

def inverse(matrix):
    determinant_reciprocal = 1 / determinant(matrix)
    transform = [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]
    result = scalar(transform, determinant_reciprocal)
    return result

def inverse_3d(matrix):
    print(matrix)
    determinant_reciprocal = 1 / determinant_3d(matrix)
    print(determinant_reciprocal)
    transform = transpose_3d(cofactors(minors(matrix)))
    print(transform)
    result = scalar_3d(transform, determinant_reciprocal)
    return result
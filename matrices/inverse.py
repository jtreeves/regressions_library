from .scalar import scalar
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
    determinant_reciprocal = 1 / determinant_3d(matrix)
    transform = transpose_3d(cofactors(minors(matrix)))
    result = scalar(transform, determinant_reciprocal)
    return result

A = [
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
]

inv_A = inverse_3d(A)

print(inv_A) # => [[0.2, 0.2, 0], [-0.2, 0.3, 1], [0.2, -0.3, 0]]
from scalar import scalar
from determinant import determinant

def inverse(matrix):
    determinant_reciprocal = 1 / determinant(matrix)
    transform = [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]
    result = scalar(transform, determinant_reciprocal)
    return result
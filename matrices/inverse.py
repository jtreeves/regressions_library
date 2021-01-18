from .scalar import scalar
from .determinant import determinant
from .transpose import transpose
from .minors import minors
from .cofactors import cofactors

def inverse(matrix):
    determinant_reciprocal = 1 / determinant(matrix)
    transform = transpose(cofactors(minors(matrix)))
    result = scalar(transform, determinant_reciprocal)
    return result
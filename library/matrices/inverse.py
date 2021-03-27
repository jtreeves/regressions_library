from .multiplication import scalar_product
from .determinant import linear_determinant
from .transpose import adjugate
from .minors import matrix_of_minors
from .cofactors import matrix_of_cofactors

def inverse_matrix(matrix):
    determinant_reciprocal = 1 / linear_determinant(matrix)
    transform = adjugate(matrix_of_cofactors(matrix_of_minors(matrix)))
    result = scalar_product(transform, determinant_reciprocal)
    return result
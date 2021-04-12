from library.errors.matrices import square_matrix
from .multiplication import scalar_product_matrix
from .determinant import linear_determinant
from .transpose import adjugate
from .minors import matrix_of_minors
from .cofactors import matrix_of_cofactors

def inverse_matrix(matrix):
    """
    Generate the inverse matrix of a given matrix

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers representing a matrix

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain the same amount of lists as the amount of elements contained within its first list
    
    Returns
    -------
    inverse : list
        List of lists corresponding to the inverse of the original matrix

    See Also
    --------
    :func:`~library.matrices.cofactors.matrix_of_cofactors`, :func:`~library.matrices.minors.matrix_of_minors`, :func:`~library.matrices.transpose.adjugate`, :func:`~library.matrices.determinant.linear_determinant`, :func:`~library.matrices.multiplication.scalar_product_matrix`

    Notes
    -----
    - Original matrix: :math:`\\mathbf{A} = \\begin{bmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,n} \\end{bmatrix}`
    - Inverse of matrix: :math:`\\mathbf{A}^{-1} = \\frac{1}{|\\mathbf{A}|}\\cdot{{{\\mathbf{A}^M}^C}^T}`
    - |inverse|

    Examples
    --------
    Generate the inverse of [[1, 2], [3, 4]]
        >>> inverse_2x2 = inverse_matrix([[1, 2], [3, 4]])
        >>> print(inverse_2x2)
        [[-2.0, 1.0], [1.5, -0.5]]
    Generate the inverse of [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
        >>> inverse_3x3 = inverse_matrix([[2, 3, 5], [7, 11, 13], [17, 19, 23]])
        >>> print(inverse_3x3)
        [[-0.07692307692307693, -0.3333333333333333, 0.20512820512820512], [-0.7692307692307692, 0.5, -0.11538461538461538], [0.6923076923076923, -0.16666666666666666, -0.01282051282051282]]
    """
    square_matrix(matrix)
    determinant_reciprocal = 1 / linear_determinant(matrix)
    transform = adjugate(matrix_of_cofactors(matrix_of_minors(matrix)))
    result = scalar_product_matrix(transform, determinant_reciprocal)
    return result
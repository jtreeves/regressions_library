from library.errors.matrices import square_matrix
from .determinant import linear_determinant, inner_determinant

def matrix_of_minors(matrix):
    """
    Create the matrix of minors corresponding to a given matrix

    Parameters
    ----------
    matrix : list
        List of lists of numbers representing a matrix

    Raises
    ------
    TypeError
        Argument must be a 2-dimensional list
    TypeError
        Elements nested within argument must be integers or floats
    ValueError
        Argument must contain the same amount of lists as the amount of elements contained within its first list
    
    Returns
    -------
    matrix : list
        List of lists in which each inner element is a determinant of a subsection of the original matrix

    See Also
    --------
    :func:`~library.matrices.cofactors.matrix_of_cofactors`, :func:`~library.matrices.transpose.adjugate`, :func:`~library.matrices.determinant.linear_determinant`, :func:`~library.matrices.inverse.inverse_matrix`

    Notes
    -----
    - Original matrix: :math:`\\mathbf{A} = \\begin{bmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,j} & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,j} & a_{2,n} \\\\ a_{i,1} & a_{i,2} & \\cdots & a_{i,j} & a_{i,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,j} & a_{m,n} \\end{bmatrix}`
    - Minor of matrix: :math:`|\\mathbf{A}_{i,j}| = \\begin{vmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,n} \\end{vmatrix}`
    - Matrix of minors: :math:`\\mathbf{A}^M = \\begin{bmatrix} |\\mathbf{A}_{1,1}| & |\\mathbf{A}_{1,2}| & \\cdots & |\\mathbf{A}_{1,j}| & |\\mathbf{A}_{1,n}| \\\\ |\\mathbf{A}_{2,1}| & |\\mathbf{A}_{2,2}| & \\cdots & |\\mathbf{A}_{2,j}| & |\\mathbf{A}_{2,n}| \\\\ |\\mathbf{A}_{i,1}| & |\\mathbf{A}_{i,2}| & \\cdots & |\\mathbf{A}_{i,j}| & |\\mathbf{A}_{i,n}| \\\\ \\cdots & \\cdots & \\cdots & \\cdots & \\cdots \\\\ |\\mathbf{A}_{m,1}| & |\\mathbf{A}_{m,2}| & \\cdots & |\\mathbf{A}_{m,j}| & |\\mathbf{A}_{m,n}| \\end{bmatrix}`
    - |minors|

    Examples
    --------
    Create the matrix of minors for [[1, 2], [3, 4]]
        >>> matrix_2x2 = matrix_of_minors([[1, 2], [3, 4]])
        >>> print(matrix_2x2)
        [[4, 3], [2, 1]]
    Create the matrix of minors for [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
        >>> matrix_3x3 = matrix_of_minors([[2, 3, 5], [7, 11, 13], [17, 19, 23]])
        >>> print(matrix_3x3)
        [[6, -60, -54], [-26, -39, -13], [-16, -9, 1]]
    """
    square_matrix(matrix)
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(linear_determinant(inner_determinant(matrix, m, n)))
    return result
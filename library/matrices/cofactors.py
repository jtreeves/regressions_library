from library.errors.matrices import matrix_of_scalars

def matrix_of_cofactors(matrix):
    """
    Create the matrix of cofactors corresponding to a given matrix

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
    
    Returns
    -------
    matrix : list
        List of lists in which each inner element alternates being positive or negative versions of the corresponding element from the original matrix

    See Also
    --------
    :func:`~library.matrices.minors.matrix_of_minors`, :func:`~library.matrices.transpose.transposed_matrix`, :func:`~library.matrices.determinant.linear_determinant`, :func:`~library.matrices.inverse.inverse_matrix`

    Notes
    -----
    - Original matrix: :math:`\\mathbf{A} = \\begin{bmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,n} \\end{bmatrix}`
    - Matrix of cofactors (if :math:`\\mathbf{A}` contains an odd number of rows and columns): :math:`\\mathbf{A}^C = \\begin{bmatrix} a_{1,1} & -1\\cdot{a_{1,2}} & \\cdots & a_{1,n} \\\\ -1\\cdot{a_{2,1}} & a_{2,2} & \\cdots & -1\\cdot{a_{2,n}} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & -1\\cdot{a_{m,2}} & \\cdots & a_{m,n} \\end{bmatrix}`
    - Matrix of cofactors (if :math:`\\mathbf{A}` contains an even number of rows and columns): :math:`\\mathbf{A}^C = \\begin{bmatrix} a_{1,1} & -1\\cdot{a_{1,2}} & \\cdots & -1\\cdot{a_{1,n}} \\\\ -1\\cdot{a_{2,1}} & a_{2,2} & \\cdots & a_{2,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ -1\\cdot{a_{m,1}} & a_{m,2} & \\cdots & a_{m,n} \\end{bmatrix}`
    - |cofactors|

    Examples
    --------
    Create the matrix of cofactors for [[1, 2, 3], [4, 5, 6]]
        >>> matrix_3x2 = matrix_of_cofactors([[1, 2, 3], [4, 5, 6]])
        >>> print(matrix_3x2)
        [[1, -2, 3], [-4, 5, -6]]
    Create the matrix of cofactors for [[2, 3], [5, 7]]
        >>> matrix_2x2 = matrix_of_cofactors([[2, 3], [5, 7]])
        >>> print(matrix_2x2)
        [[2, -3], [-5, 7]]
    """
    matrix_of_scalars(matrix)
    result = []
    for m in range(len(matrix)):
        result.append([])
        if m % 2 == 0:
            for n in range(len(matrix[0])):
                if n % 2 == 0:
                    result[m].append(matrix[m][n])
                else:
                    result[m].append(-1 * matrix[m][n])
        else:
            for n in range(len(matrix[0])):
                if n % 2 == 0:
                    result[m].append(-1 * matrix[m][n])
                else:
                    result[m].append(matrix[m][n])
    return result
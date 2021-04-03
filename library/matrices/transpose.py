from library.errors.matrices import matrix_of_scalars

def adjugate(matrix):
    """
    Transpose a matrix's rows and columns

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers representing a matrix

    Raises
    ------
    TypeError
        Argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within argument must be integers or floats
    
    Returns
    -------
    matrix : list
        List of lists in which each inner element occupies the row that correspond's to the column it occupied in the original matrix and the column that correspond's to the row it occupied in the original matrix

    Examples
    --------
    Transpose [[1, 2, 3], [4, 5, 6]]
        >>> matrix_3x2 = adjugate([[1, 2, 3], [4, 5, 6]])
        >>> print(matrix_3x2)
        [[1, 4], [2, 5], [3, 6]]
    Transpose [[2, 3], [5, 7]]
        >>> matrix_2x2 = adjugate([[2, 3], [5, 7]])
        >>> print(matrix_2x2)
        [[2, 5], [3, 7]]
    """
    matrix_of_scalars(matrix, 'only')
    result = []
    for m in range(len(matrix[0])):
        result.append([])
        for n in range(len(matrix)):
            result[m].append(matrix[n][m])
    return result
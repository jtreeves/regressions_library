from library.errors.matrices import matrix_of_scalars

def matrix_of_cofactors(matrix):
    """
    Create the matrix of cofactors corresponding to a given matrix

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
        List of lists in which each inner element alternates being positive or negative versions of the corresponding element from the original matrix

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
    matrix_of_scalars(matrix, 'only')
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
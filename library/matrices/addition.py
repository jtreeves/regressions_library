from library.errors.matrices import compare_matrices

def matrix_sum(matrix_one, matrix_two):
    """
    Calculates the sum of two matrices

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers representing a matrix
    matrix_two : list or tuple
        List of lists of numbers representing a matrix

    Raises
    ------
    TypeError
        Arguments must be 2-dimensional lists or tuples
    TypeError
        Elements nested within arguments must be integers or floats
    ValueError
        Both arguments must contain the same amount of lists
    ValueError
        First list within first argument and first list within second argument must contain the same amount of elements

    Returns
    -------
    matrix : list
        List of lists in which each inner element is the sum of the corresponding elements from the input matrices

    Examples
    --------
    Add [[1, 2, 3], [4, 5, 6]] and [[2, 3, 5], [7, 11, 13]]
        >>> matrix_2x3 = matrix_sum([[1, 2, 3], [4, 5, 6]], [[2, 3, 5], [7, 11, 13]])
        >>> print(matrix_2x3)
        [[3, 5, 8], [11, 15, 19]]
    Add [[-2, 5], [7, -1]] and [[8, 2], [-3, 4]]
        >>> matrix_2x2 = matrix_sum([[-2, 5], [7, -1]], [[8, 2], [-3, 4]])
        >>> print(matrix_2x2)
        [[6, 7], [4, 3]]
    """
    compare_matrices(matrix_one, matrix_two)
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_one[0])):
            result[m].append(matrix_one[m][n] + matrix_two[m][n])
    return result
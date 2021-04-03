from library.errors.matrices import square_matrix
from .determinant import linear_determinant, inner_determinant

def matrix_of_minors(matrix):
    """
    Create the matrix of minors corresponding to a given matrix

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
    ValueError
        Argument must contain the same amount of lists as the amount of elements contained within its first list
    
    Returns
    -------
    matrix : list
        List of lists in which each inner element is a determinant of a subsection of the original matrix

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
from library.errors.scalars import scalar_value
from library.errors.matrices import matrix_of_scalars, columns_rows
from library.vectors.multiplication import dot_product
from .transpose import adjugate

def scalar_product_matrix(matrix, scalar):
    """
    Calculates the product of a matrix and a scalar

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers representing a matrix
    scalar : int or float
        Number representing a scalar

    Raises
    ------
    TypeError
        First argument must be 2-dimensional lists or tuples
    TypeError
        Elements nested within first argument must be integers or floats
    TypeError
        Second argument must be an integer or a float

    Returns
    -------
    matrix : list
        List of lists in which each inner element is the product of the corresponding element from the input matrix and the scalar value

    Examples
    --------
    Multiply [[1, 2, 3], [4, 5, 6]] and -2
        >>> matrix_2x3 = scalar_product([[1, 2, 3], [4, 5, 6]], -2)
        >>> print(matrix_2x3)
        [[-2, -4, -6], [-8, -10, -12]]
    Multiply [[5, -7], [-3, 8]] and 3
        >>> matrix_2x2 = scalar_product([[5, -7], [-3, 8]], 3)
        >>> print(matrix_2x2)
        [[15, -21], [-9, 24]]
    """
    matrix_of_scalars(matrix, 'first')
    scalar_value(scalar, 'second')
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(matrix[m][n] * scalar)
    return result

def matrix_product(matrix_one, matrix_two):
    """
    Calculates the product of two matrices

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
        First list within first argument must contain the same amount of elements as the amount of lists contained within second argument

    Returns
    -------
    matrix : list
        List of lists in which each inner element is the dot product of the first matrix's row vector corresponding to that element's row position and the second matrix's column vector corresponding to that element's column position; resultant matrix will have the same number of rows as the first matrix and the same number of columns as the second matrix

    Examples
    --------
    Multiply [[1, 2, 3], [4, 5, 6]] and [[2, 3], [5, 7], [11, 13]]
        >>> matrix_2x2 = matrix_product([[1, 2, 3], [4, 5, 6]], [[2, 3], [5, 7], [11, 13]])
        >>> print(matrix_2x2)
        [[45, 56], [99, 125]]
    Multiply [[1, 2, 3], [4, 5, 6]] and [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        >>> matrix_2x4 = matrix_product([[1, 2, 3], [4, 5, 6]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        >>> print(matrix_2x4)
        [[38, 44, 50, 56], [83, 98, 113, 128]]
    """
    columns_rows(matrix_one, matrix_two)
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_two[0])):
            result[m].append(dot_product(matrix_one[m], adjugate(matrix_two)[n]))
    return result
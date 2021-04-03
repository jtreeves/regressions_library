def matrix_of_scalars(matrix, position):
    """
    Ensures argument at a given position is a matrix containing scalar values

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers represening a matrix
    position : str
        String representing the position of the matrix argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within first argument must be integers or floats

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [[1, 2], [3, 4]] is a matrix of scalars
        >>> confirmation = matrix_of_scalars([[1, 2], [3, 4]], 'first')
        >>> print(confirmation)
        First argument is a 2-dimensional list or tuple containing elements that are integers or floats
    Confirm [1, 2, 3] is not a matrix of scalars
        >>> failure = matrix_of_scalars([1, 2, 3], 'first')
        TypeError: First argument must be a 2-dimensional list or tuple
    """
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(matrix, (list, tuple)) or not isinstance(matrix[0], (list, tuple)) or isinstance(matrix[0][0], (list, tuple)):
        raise TypeError(f'{identifier.capitalize()} must be a 2-dimensional list or tuple')
    if not isinstance(matrix[0][0], (int, float)):
        raise TypeError(f'Elements nested within {identifier} must be integers or floats')
    else:
        return f'{identifier.capitalize()} is a 2-dimensional list or tuple containing elements that are integers or floats'

def square_matrix(matrix):
    """
    Ensures argument is a square matrix, with the same number of rows and columns

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers represening a matrix

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
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [[1, 2], [3, 4]] is a square matrix
        >>> confirmation = square_matrix([[1, 2], [3, 4]])
        >>> print(confirmation)
        First argument contains the same amount of lists as the amount of elements contained within its first list
    Confirm [[1, 2, 3], [4, 5, 6]] is not a square matrix
        >>> failure = square_matrix([[1, 2, 3], [4, 5, 6]])
        ValueError: First argument must contain the same amount of lists as the amount of elements contained within its first list
    """
    matrix_of_scalars(matrix, 'first')
    if len(matrix) is not len(matrix[0]):
        raise ValueError('First argument must contain the same amount of lists as the amount of elements contained within its first list')
    else:
        return 'First argument contains the same amount of lists as the amount of elements contained within its first list'

def compare_rows(matrix_one, matrix_two):
    """
    Ensures arguments contain the same number of rows

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers represening a matrix
    matrix_two : list or tuple
        List of lists of numbers represening a matrix

    Raises
    ------
    TypeError
        Arguments must be 2-dimensional lists or tuples
    TypeError
        Elements nested within arguments must be integers or floats
    ValueError
        Both arguments must contain the same amount of lists

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Compare rows in [[1, 2], [3, 4]] and [[5, 6, 7], [8, 9, 10]]
        >>> confirmation = compare_rows([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
        >>> print(confirmation)
        First argument and second argument contain the same amount of lists
    Compare rows in [[1, 2], [3, 4]] and [[5, 6], [7, 8], [9, 10]]
        >>> failure = compare_rows([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
        ValueError: First argument and second argument must contain the same amount of lists
    """
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one) is not len(matrix_two):
        raise ValueError('First argument and second argument must contain the same amount of lists')
    else:
        return 'First argument and second argument contain the same amount of lists'

def compare_columns(matrix_one, matrix_two):
    """
    Ensures arguments contain the same number of columns

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers represening a matrix
    matrix_two : list or tuple
        List of lists of numbers represening a matrix

    Raises
    ------
    TypeError
        Arguments must be 2-dimensional lists or tuples
    TypeError
        Elements nested within arguments must be integers or floats
    ValueError
        First list within first argument and first list within second argument must contain the same amount of elements

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Compare columns in [[1, 2], [3, 4]] and [[5, 6], [7, 8], [9, 10]]
        >>> confirmation = compare_columns([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
        >>> print(confirmation)
        First list within first argument and first list within second argument contain the same amount of elements
    Compare columns in [[1, 2], [3, 4]] and [[5, 6, 7], [8, 9, 10]]
        >>> failure = compare_columns([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
        ValueError: First list within first argument and first list within second argument must contain the same amount of elements
    """
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one[0]) is not len(matrix_two[0]):
        raise ValueError('First list within first argument and first list within second argument must contain the same amount of elements')
    else:
        return 'First list within first argument and first list within second argument contain the same amount of elements'

def compare_matrices(matrix_one, matrix_two):
    """
    Ensures arguments contain the same number of rows and the same number of columns

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers represening a matrix
    matrix_two : list or tuple
        List of lists of numbers represening a matrix

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
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Compare matrices [[1, 2, 3], [4, 5, 6]] and [[7, 8, 9], [10, 11, 12]]
        >>> confirmation = compare_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])
        >>> print(confirmation)
        First argument and second argument contain the same amount of lists; first list within first argument and first list within second argument contain the same amount of elements
    Compare matrices [[1, 2, 3], [4, 5, 6]] and [[7, 8], [9, 10]]
        >>> failure = compare_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10]])
        ValueError: First list within first argument and first list within second argument must contain the same amount of elements
    """
    compare_rows(matrix_one, matrix_two)
    compare_columns(matrix_one, matrix_two)
    return 'First argument and second argument contain the same amount of lists; first list within first argument and first list within second argument contain the same amount of elements'

def columns_rows(matrix_one, matrix_two):
    """
    Ensures the number of columns in the first matrix is equal to the number of rows in the second matrix

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers represening a matrix
    matrix_two : list or tuple
        List of lists of numbers represening a matrix

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
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Compare matrices [[1, 2, 3], [4, 5, 6]] and [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
        >>> confirmation = columns_rows([[1, 2, 3], [4, 5, 6]], [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
        >>> print(confirmation)
        First list within first argument contains the same amount of elements as the amount of lists contained within second argument
    Compare matrices [[1, 2, 3], [4, 5, 6]] and [[7, 8, 9], [10, 11, 12]]
        >>> failure = columns_rows([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])
        ValueError: First list within first argument must contain the same amount of elements as the amount of lists contained within second argument
    """
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one[0]) is not len(matrix_two):
        raise ValueError('First list within first argument must contain the same amount of elements as the amount of lists contained within second argument')
    else:
        return 'First list within first argument contains the same amount of elements as the amount of lists contained within second argument'

def level(matrix, scalar):
    """
    Ensures a scalar value is less than or equal to the number of columns in a matrix

    Parameters
    ----------
    matrix : list or tuple
        List of lists of numbers represening a matrix
    scalar : int
        Number representing a column in a matrix

    Raises
    ------
    ValueError
        Last argument must be less than or equal to the length of the nested lists within the first argument

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 2 is less than or equal to the number of columns in the matrix [[1, 2, 3], [4, 5, 6]]
        >>> confirmation = level([[1, 2, 3], [4, 5, 6]], 2)
        >>> print(confirmation)
        Last argument is less than or equal to the length of the nested lists within the first argument
    Confirm 5 is not less than or equal to the number of columns in the matrix [[1, 2, 3], [4, 5, 6]]
        >>> failure = level([[1, 2, 3], [4, 5, 6]], 5)
        ValueError: Last argument must be less than or equal to the length of the nested lists within the first argument
    """
    if not scalar <= len(matrix[0]):
        raise ValueError('Last argument must be less than or equal to the length of the nested lists within the first argument')
    else:
        return 'Last argument is less than or equal to the length of the nested lists within the first argument'
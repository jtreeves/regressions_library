from library.errors.vectors import vector_of_scalars

def column_conversion(vector):
    """
    Converts a row vector into a column vector

    Parameters
    ----------
    vector : list or tuple
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple

    Returns
    -------
    column : list
        List in which each element is a list containing an element from the input vector

    Examples
    --------
    Convert [1, 2, 3]
        >>> column_3d = column_conversion([1, 2, 3])
        >>> print(column_3d)
        [[1], [2], [3]]
    Convert [-7, 5]
        >>> column_2d = column_conversion([-7, 5])
        >>> print(column_2d)
        [[-7], [5]]
    """
    vector_of_scalars(vector, 'only')
    result = []
    for element in vector:
        result.append([element])
    return result
from library.errors.vectors import vector_of_scalars

def column_conversion(vector):
    """
    Converts a row vector into a column vector

    Parameters
    ----------
    vector : list
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list

    Returns
    -------
    column : list
        List in which each element is a list containing an element from the input vector

    See Also
    --------
    :func:`~library.vectors.dimension.single_dimension`

    Notes
    -----
    - Row vector: :math:`\\langle a_1, a_2, \\cdots, a_n \\rangle`
    - Column vector: :math:`\\left\\langle\\begin{matrix} a_1, \\\\ a_2, \\\\ \\cdots, \\\\ a_n \\end{matrix}\\right\\rangle`

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
    vector_of_scalars(vector)
    result = []
    for element in vector:
        result.append([element])
    return result
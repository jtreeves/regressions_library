from library.errors.vectors import vector_of_scalars

def sum_value(data):
    """
    Calculates the sum of all elements in a data set

    Parameters
    ----------
    data : list or tuple
        List of numbers

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    total : int or float
        Number representing the sum of all elements in the original set

    Examples
    --------
    Find the total sum of all values in the array [2, 3, 5, 7]
        >>> total1 = sum_value([2, 3, 5, 7])
        >>> print(total1)
        17
    Find the total sum of all values in the array [1, -1, 1, -1]
        >>> total2 = sum_value([1, -1, 1, -1])
        >>> print(total2)
        0
    """
    vector_of_scalars(data, 'only')
    result = 0
    for element in data:
        result += element
    return result
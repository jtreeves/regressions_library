from library.errors.vectors import vector_of_scalars

def sum_value(data):
    """
    Calculates the sum of all elements in a data set

    Parameters
    ----------
    data : list
        List of numbers

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    total : float
        Number representing the sum of all elements in the original set

    See Also
    --------
    :func:`~library.statistics.mean.mean_value`, :func:`~library.statistics.correlation.correlation_coefficient`

    Notes
    -----
    - Set of numbers: :math:`a_i = \\{ a_1, a_2, \\cdots, a_n \\}`
    - Sum of all numbers in set: :math:`\\sum\\limits_{i=1}^n a_i = a_1 + a_2 + \\cdots + a_n`
    - |summation_notation|

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
    vector_of_scalars(data)
    result = 0
    for element in data:
        result += element
    return float(result)
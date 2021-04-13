from math import floor
from library.errors.vectors import vector_of_scalars
from .sort import sorted_list

def median_value(data):
    """
    Determines the median value of a data set

    Parameters
    ----------
    data : list
        List of numbers to analyze

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    median : int or float
        Middle value of the data set, splitting the data evenly in half

    See Also
    --------
    :func:`~library.statistics.sort.sorted_list`, :func:`~library.statistics.minimum.minimum_value`, :func:`~library.statistics.maximum.maximum_value`

    Notes
    -----
    - Ordered set of numbers: :math:`a_i = ( a_1, a_2, \\cdots, a_n )`
    - Median of all numbers in set (if set contains an odd amount of numbers): :math:`M = a_{\\lceil n/2 \\rceil}`
    - Median of all numbers in set (if set contains an even amount of numbers): :math:`M = \\frac{a_{n/2} + a_{n/2 + 1}}{2}`
    - |median|

    Examples
    --------
    Determine the median of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> median_even = median_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1])
        >>> print(median_even)
        20.5
    Determine the median of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> median_odd = median_value([12, 81, 13, 8, 42, 72, 91, 20, 20])
        >>> print(median_odd)
        20
    """
    vector_of_scalars(data)
    sorted_data = sorted_list(data)
    length = len(sorted_data)
    if length % 2 == 0:
        upper_index = int(length / 2)
        lower_index = int(upper_index - 1)
        upper_value = sorted_data[upper_index]
        lower_value = sorted_data[lower_index]
        result = (upper_value + lower_value) / 2
        return result
    else:
        index = int(floor(length / 2))
        result = sorted_data[index]
        return result
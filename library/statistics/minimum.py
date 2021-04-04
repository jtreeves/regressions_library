from library.errors.vectors import vector_of_scalars
from .sort import sorted_list

def minimum_value(data):
    """
    Determines the smallest value of a data set

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    minimum : int or float
        Smallest value from the data set

    Examples
    --------
    Determine the minimum of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> minimum_even = minimum_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1])
        >>> print(minimum_even)
        1
    Determine the minimum of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> minimum_odd = minimum_value([12, 81, 13, 8, 42, 72, 91, 20, 20])
        >>> print(minimum_odd)
        8
    """
    vector_of_scalars(data, 'only')
    sorted_data = sorted_list(data)
    result = sorted_data[0]
    return result
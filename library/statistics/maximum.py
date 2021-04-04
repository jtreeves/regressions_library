from library.errors.vectors import vector_of_scalars
from .sort import sorted_list

def maximum_value(data):
    """
    Determines the largest value of a data set

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
    maximum : int or float
        Largest value from the data set

    Examples
    --------
    Determine the maximum of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> maximum_even = maximum_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1])
        >>> print(maximum_even)
        72
    Determine the maximum of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> maximum_odd = maximum_value([12, 81, 13, 8, 42, 72, 91, 20, 20])
        >>> print(maximum_odd)
        91
    """
    vector_of_scalars(data, 'only')
    sorted_data = sorted_list(data)
    result = sorted_data[-1]
    return result
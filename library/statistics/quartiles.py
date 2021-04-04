from library.errors.vectors import vector_of_scalars
from library.errors.scalars import select_integers
from .median import median_value
from .halve import half

def quartile_value(data, q):
    """
    Determines the first, second, or third quartile values of a data set

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze
    q : int
        Number determining which quartile to provide

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        Elements of first argument must be integers or floats
    ValueError
        Second argument must be an integer contained within the set [1, 2, 3]

    Returns
    -------
    quartile : int or float
        Quartile value of the data set

    Examples
    --------
    Determine the first quartile of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> quartile1 = quartile_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1], 1)
        >>> print(quartile1)
        9
    Determine the third quartile of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> quartile3 = quartile_value([12, 81, 13, 8, 42, 72, 91, 20, 20], 3)
        >>> print(quartile3)
        76.5
    """
    vector_of_scalars(data, 'first')
    select_integers(q, [1, 2, 3])
    halved_data = half(data)
    result = ''
    if q == 2:
        result = median_value(data)
    elif q == 1:
        result = median_value(halved_data['lower'])
    elif q == 3:
        result = median_value(halved_data['upper'])
    return result
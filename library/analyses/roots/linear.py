from library.errors.scalars import two_scalars, positive_integer
from library.statistics.rounding import rounded_value

def linear_roots(first_constant, second_constant, precision):
    """
    Calculates the roots of a linear function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term of the original linear function
    second_constant : int or float
        Coefficient of the constant term of the original linear function
    precision : int
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First two arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of all of the x-intercepts of the original function

    Examples
    --------
    Calculate the roots of a linear function with coefficients 2 and 3 (and round roots to four decimal places)
        >>> roots1 = linear_roots(2, 3, 4)
        >>> print(roots1)
        [-1.5]
    Calculate the roots of a linear function with coefficients 7 and -5 (and round roots to four decimal places)
        >>> roots2 = linear_roots(7, -5, 4)
        >>> print(roots2)
        [0.7143]
    """
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    root = -1 * second_constant / first_constant
    result = [rounded_value(root, precision)]
    return result
from library.errors.scalars import two_scalars, positive_integer
from library.statistics.rounding import rounded_value

def hyperbolic_roots(first_constant, second_constant, precision):
    """
    Calculates the roots of a hyperbolic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the reciprocal variable of the original hyperbolic function
    second_constant : int or float
        Coefficient of the constant term of the original hyperbolic function
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
        List of the x-coordinates of all of the x-intercepts of the original function; if the function never crosses the x-axis, then it will return a list of `None`

    Examples
    --------
    Calculate the roots of a hyperbolic function with coefficients 2 and 3 (and round roots to four decimal places)
        >>> roots1 = hyperbolic_roots(2, 3, 4)
        >>> print(roots1)
        [-0.6667]
    Calculate the roots of a hyperbolic function with coefficients 5 and 7 (and round roots to four decimal places)
        >>> roots2 = hyperbolic_roots(5, 7, 4)
        >>> print(roots2)
        [-0.7143]
    """
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    root = -1 * first_constant / second_constant
    result = [rounded_value(root, precision)]
    return result
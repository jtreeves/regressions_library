from library.errors.scalars import three_scalars, positive_integer

def logistic_roots(first_constant, second_constant, third_constant, precision):
    """
    Calculates the roots of a logistic function

    Parameters
    ----------
    first_constant : int or float
        Carrying capacity of the original logistic function
    second_constant : int or float
        Growth rate of the original logistic function
    third_constant : int or float
        Value of the sigmoid's midpoint of the original logistic function
    precision : int
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First three arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of all of the x-intercepts of the original function; if the function never crosses the x-axis, then it will return a list of `None`

    Examples
    --------
    Calculate the roots of a logistic function with coefficients 2, 3, and 5 (and round roots to four decimal places)
        >>> roots1 = logistic_roots(2, 3, 5, 4)
        >>> print(roots1)
        [None]
    Calculate the roots of a logistic function with coefficients 135, 246, and 43 (and round roots to ten decimal places)
        >>> roots2 = logistic_roots(135, 246, 43, 10)
        >>> print(roots2)
        [None]
    """
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    root = [None]
    return root
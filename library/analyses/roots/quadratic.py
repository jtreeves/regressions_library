from library.errors.scalars import three_scalars, positive_integer
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value

def quadratic_roots(first_constant, second_constant, third_constant, precision):
    """
    Calculates the roots of a quadratic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the quadratic term of the original quadratic function
    second_constant : int or float
        Coefficient of the linear term of the original quadratic function
    third_constant : int or float
        Coefficient of the constant term of the original quadratic function
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
    Calculate the roots of a quadratic function with coefficients 2, 3, and 5 (and round roots to four decimal places)
        >>> test = quadratic_roots(2, 3, 5, 4)
    Print the roots
        >>> print(test)
        [None]
    """
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    roots = []
    if first_constant == 0:
        first_constant = 10**(-precision)
    discriminant = second_constant**2 - 4 * first_constant * third_constant
    first_root = (-1 * second_constant + discriminant**(1/2)) / (2 * first_constant)
    second_root = (-1 * second_constant - discriminant**(1/2)) / (2 * first_constant)
    if first_root == second_root:
        roots.append(first_root)
    else:
        if not isinstance(first_root, complex):
            roots.append(first_root)
        if not isinstance(second_root, complex):
            roots.append(second_root)
    if not roots:
        roots = [None]
    sorted_roots = sorted_list(roots)
    result = []
    for number in sorted_roots:
        result.append(rounded_value(number, precision))
    return result
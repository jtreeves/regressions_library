from math import log
from library.errors.scalars import two_scalars, positive_integer
from library.errors.adjustments import no_zeroes

def exponential_roots(first_constant, second_constant, precision = 4):
    """
    Calculates the roots of an exponential function

    Parameters
    ----------
    first_constant : int or float
        Constant multiple of the original exponential function
    second_constant : int or float
        Base rate of variable of the original exponential function
    precision : int, default=4
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

    See Also
    --------
    :func:`~library.analyses.equations.exponential.exponential_equation`, :func:`~library.analyses.derivatives.exponential.exponential_derivatives`, :func:`~library.analyses.integrals.exponential.exponential_integral`, :func:`~library.models.exponential.exponential_model`

    Notes
    -----
    - Standard form of a exponential function: :math:`f(x) = a\\cdot{b^x}`
    - Exponential formula: :math:`x = \\varnothing`

    Examples
    --------
    Calculate the roots of an exponential function with coefficients 2 and 3 (and round roots to six decimal places)
        >>> roots1 = exponential_roots(2, 3, 6)
        >>> print(roots1)
        [None]
    Calculate the roots of an exponential function with coefficients 157 and -259 (and round roots to ten decimal places)
        >>> roots2 = exponential_roots(257, -259, 10)
        >>> print(roots2)
        [None]
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant], precision)
    
    # Create root
    root = [None]
    return root

def exponential_roots_first_derivative(first_constant, second_constant, precision = 4):
    root = [None]
    return root

def exponential_roots_second_derivative(first_constant, second_constant, precision = 4):
    root = [None]
    return root
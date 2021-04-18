from math import log
from library.errors.scalars import two_scalars, three_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.rounding import rounded_value

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

    # Create list to return
    result = []
    
    # Determine root
    root = None

    # Return result
    result.append(root)
    return result

def exponential_roots_first_derivative(first_constant, second_constant, precision = 4):
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)

    # Create list to return
    result = []
    
    # Determine root of first derivative
    root = None

    # Return result
    result.append(root)
    return result

def exponential_roots_second_derivative(first_constant, second_constant, precision = 4):
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)

    # Create list to return
    result = []
    
    # Determine root of second derivative
    root = None

    # Return result
    result.append(root)
    return result

def exponential_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    # Handle input errors
    three_scalars(first_constant, second_constant, initial_value)
    positive_integer(precision)

    # Create list to return
    result = []

    # Create intermediary variables
    numerator = log(abs(initial_value / first_constant))
    denominator = log(abs(second_constant))

    # Circumvent division by zero
    if denominator == 0:
        denominator = 10**(-precision)

    # Determine root given an initial value
    ratio = numerator / denominator

    # Round root
    rounded_ratio = rounded_value(ratio, precision)

    # Return result
    result.append(rounded_ratio)
    return result

def exponential_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    # Handle input errors
    three_scalars(first_constant, second_constant, initial_value)
    positive_integer(precision)

    # Circumvent division by zero
    denominator = log(abs(second_constant))
    if denominator == 0:
        denominator = 10**(-precision)

    # Determine root of derivative given an initial value
    result = exponential_roots_initial_value(first_constant * denominator, second_constant, initial_value, precision)
    return result
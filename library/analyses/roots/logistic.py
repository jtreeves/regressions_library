from math import log
from library.errors.scalars import three_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from .quadratic import quadratic_roots

def logistic_roots(first_constant, second_constant, third_constant, precision = 4):
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
    precision : int, default=4
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

    See Also
    --------
    :func:`~library.analyses.equations.logistic.logistic_equation`, :func:`~library.analyses.derivatives.logistic.logistic_derivatives`, :func:`~library.analyses.integrals.logistic.logistic_integral`, :func:`~library.models.logistic.logistic_model`

    Notes
    -----
    - Standard form of a logistic function: :math:`f(x) = \\frac{a}{1 + \\text{e}^{-b\\cdot(x - c)}}`
    - Logistic formula: :math:`x = \\varnothing`

    Examples
    --------
    Calculate the roots of a logistic function with coefficients 2, 3, and 5 (and round roots to six decimal places)
        >>> roots1 = logistic_roots(2, 3, 5, 6)
        >>> print(roots1)
        [None]
    Calculate the roots of a logistic function with coefficients 135, 246, and 43 (and round roots to ten decimal places)
        >>> roots2 = logistic_roots(135, 246, 43, 10)
        >>> print(roots2)
        [None]
    """
    # Handle input errors
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant, third_constant], precision)

    # Create root
    root = [None]
    return root

def logistic_roots_first_derivative(first_constant, second_constant, third_constant, precision = 4):
    root = [None]
    return root

def logistic_roots_second_derivative(first_constant, second_constant, third_constant, precision = 4):
    root = [rounded_value(third_constant)]
    return root

def logistic_roots_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    log_argument = first_constant / initial_value - 1
    if log_argument == 0:
        log_argument = 10**(-precision)
    numerator = log(abs(log_argument))
    denominator = second_constant
    ratio = numerator / denominator
    root = third_constant - ratio
    rounded_root = rounded_value(root, precision)
    final_roots = [rounded_root]
    return final_roots

def logistic_roots_derivative_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    intermediary_roots = quadratic_roots(initial_value, 2 * initial_value - first_constant * second_constant, initial_value, precision)
    final_roots = []
    if intermediary_roots[0] == None:
        final_roots.append(None)
    else:
        for intermediary in intermediary_roots:
            if intermediary == 0:
                root = third_constant - log(10**(-precision)) / second_constant
                rounded_root = rounded_value(root, precision)
                final_roots.append(rounded_root)
            else:
                root = third_constant - log(abs(intermediary)) / second_constant
                rounded_root = rounded_value(root, precision)
                final_roots.append(rounded_root)
    sorted_roots = sorted_list(final_roots)
    return sorted_roots
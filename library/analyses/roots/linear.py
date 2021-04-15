from library.errors.scalars import two_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.rounding import rounded_value

def linear_roots(first_constant, second_constant, precision = 4):
    """
    Calculates the roots of a linear function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term of the original linear function
    second_constant : int or float
        Coefficient of the constant term of the original linear function
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
        List of the x-coordinates of all of the x-intercepts of the original function

    See Also
    --------
    :func:`~library.analyses.equations.linear.linear_equation`, :func:`~library.analyses.derivatives.linear.linear_derivatives`, :func:`~library.analyses.integrals.linear.linear_integral`, :func:`~library.models.linear.linear_model`

    Notes
    -----
    - Standard form of a linear function: :math:`f(x) = a\\cdot{x} + b`
    - Linear formula: :math:`x = -\\frac{b}{a}`
    - |linear_formula|

    Examples
    --------
    Calculate the roots of a linear function with coefficients 2 and 3
        >>> roots1 = linear_roots(2, 3)
        >>> print(roots1)
        [-1.5]
    Calculate the roots of a linear function with coefficients 7 and -5
        >>> roots2 = linear_roots(7, -5)
        >>> print(roots2)
        [0.7143]
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant], precision)
    
    # Create root
    root = -1 * coefficients[1] / coefficients[0]

    # Round root
    result = [rounded_value(root, precision)]
    return result
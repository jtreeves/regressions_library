from library.errors.scalars import three_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value, rounded_list
from library.analyses.derivatives.quadratic import quadratic_derivatives
from .linear import linear_roots

def quadratic_roots(first_constant, second_constant, third_constant, precision = 4):
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
    :func:`~library.analyses.equations.quadratic.quadratic_equation`, :func:`~library.analyses.derivatives.quadratic.quadratic_derivatives`, :func:`~library.analyses.integrals.quadratic.quadratic_integral`, :func:`~library.models.quadratic.quadratic_model`

    Notes
    -----
    - Standard form of a quadratic function: :math:`f(x) = a\\cdot{x^2} + b\\cdot{x} + c`
    - Quadratic formula: :math:`x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}`
    - |quadratic_formula|

    Examples
    --------
    Calculate the roots of a quadratic function with coefficients 10, 7, and -15
        >>> roots1 = quadratic_roots(10, 7, -15)
        >>> print(roots1)
        [-5.0, 1.5]
    Calculate the roots of a quadratic function with coefficients 9, -42, and 49
        >>> roots2 = quadratic_roots(9, -42, 49)
        >>> print(roots2)
        [2.3333]
    """
    # Handle input errors
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant, third_constant], precision)

    # Create intermediary variable
    discriminant = coefficients[1]**2 - 4 * coefficients[0] * coefficients[2]

    # Create roots
    roots = []
    first_root = (-1 * coefficients[1] + discriminant**(1/2)) / (2 * coefficients[0])
    second_root = (-1 * coefficients[1] - discriminant**(1/2)) / (2 * coefficients[0])

    # Eliminate duplicate roots
    if first_root == second_root:
        roots.append(first_root)
    
    # Eliminate complex roots
    else:
        if not isinstance(first_root, complex):
            roots.append(first_root)
        if not isinstance(second_root, complex):
            roots.append(second_root)
    
    # Handle no roots
    if not roots:
        roots = [None]
    
    # Sort roots
    sorted_roots = sorted_list(roots)
    
    # Round roots
    result = rounded_list(sorted_roots, precision)
    return result

def quadratic_roots_first_derivative(first_constant, second_constant, third_constant, precision = 4):
    constants = quadratic_derivatives(first_constant, second_constant, third_constant)['first']['constants']
    roots = linear_roots(*constants, precision)
    return roots

def quadratic_roots_second_derivative(first_constant, second_constant, third_constant, precision = 4):
    root = [None]
    return root

def quadratic_roots_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    roots = quadratic_roots(first_constant, second_constant, third_constant - initial_value, precision)
    return roots

def quadratic_roots_derivative_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    roots = linear_roots(2 * first_constant, second_constant - initial_value, precision)
    return roots
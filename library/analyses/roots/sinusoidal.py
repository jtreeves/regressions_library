from math import asin, pi
from library.errors.scalars import four_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value

def sinusoidal_roots(first_constant, second_constant, third_constant, fourth_constant, precision = 4):
    """
    Calculates the roots of a sinusoidal function

    Parameters
    ----------
    first_constant : int or float
        Vertical stretch factor of the original sine function
    second_constant : int or float
        Horizontal stretch factor of the original sine function
    third_constant : int or float
        Horizontal shift of the original sine function
    fourth_constant : int or float
        Vertical shift of the original sine function
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First four arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of the initial x-intercepts within two periods of the original function in float format, along with the general forms in string format that can be used to determine all other x-intercepts by plugging in any integer value for 'k' and evaluating; if the function never crosses the x-axis, then it will return a list of `None`

    See Also
    --------
    :func:`~library.analyses.equations.sinusoidal.sinusoidal_equation`, :func:`~library.analyses.derivatives.sinusoidal.sinusoidal_derivatives`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`, :func:`~library.models.sinusoidal.sinusoidal_model`

    Notes
    -----
    - Standard form of a sinusoidal function: :math:`f(x) = a\\cdot{\\sin(b\\cdot(x - c))} + d`
    - Sinusoidal formula: :math:`x_0 = c + \\frac{1}{b}\\cdot{\\sin^{-1}(-\\frac{d}{a})} + \\frac{2\\pi}{b}\\cdot{k}`

        - :math:`\\text{if} -1 < -\\frac{d}{a} < 0 \\text{ or } 0 < -\\frac{d}{a} < 1, x_1 = c + \\frac{\\pi}{b} - \\frac{1}{b}\\cdot{\\sin^{-1}(-\\frac{d}{a})} + \\frac{2\\pi}{b}\\cdot{k}`
        - :math:`\\text{if} -\\frac{d}{a} = 0, x_1 = c - \\frac{\\pi}{b} + \\frac{2\\pi}{b}\\cdot{k}`
        - :math:`k \\in \\mathbb{Z}`

    Examples
    --------
    Calculate the roots of a sinusoidal function with coefficients 2, 3, 5, and 1
        >>> roots1 = sinusoidal_roots(2, 3, 5, 1)
        >>> print(roots1)
        [4.8255, 6.2217, 6.9199, 8.3161, 9.0143, 10.4105, '4.8255 + 2.0944k', '6.2217 + 2.0944k']
    Calculate the roots of a sinusoidal function with coefficients 3, 1, -2, and 3
        >>> roots2 = sinusoidal_roots(3, 1, -2, 3)
        >>> print(roots2)
        [-3.5708, 2.7124, 8.9956, '-3.5708 + 6.2832k']
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant], precision)
    roots = []
    ratio = -1 * coefficients[3] / coefficients[0]
    if ratio > 1 or ratio < -1:
        roots = [None]
    else:
        radians = asin(ratio)
        periodic_radians = radians / coefficients[1]
        if ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / coefficients[1]
            initial_value = coefficients[2] + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / coefficients[1]
            initial_value = coefficients[2] + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            alternative_initial_value = coefficients[2] + pi / coefficients[1] - periodic_radians
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            rounded_alternative_initial_value = rounded_value(alternative_initial_value, precision)
            alternative_general_form = str(rounded_alternative_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, alternative_initial_value, alternative_first_value, alternative_second_value, general_form, alternative_general_form]
    if not roots:
        roots = [None]
    numerical_roots = []
    other_roots = []
    for item in roots:
        if isinstance(item, (int, float)):
            numerical_roots.append(item)
        else:
            other_roots.append(item)
    sorted_roots = sorted_list(numerical_roots)
    rounded_roots = []
    for number in sorted_roots:
        rounded_roots.append(rounded_value(number, precision))
    result = rounded_roots + other_roots
    return result
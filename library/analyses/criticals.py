from math import pi
from library.errors.scalars import select_integers, positive_integer
from library.errors.vectors import vector_of_scalars
from library.errors.analyses import select_equations
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from .roots.linear import linear_roots
from .roots.quadratic import quadratic_roots
from .derivatives.quadratic import quadratic_derivatives
from .derivatives.cubic import cubic_derivatives

def critical_points(equation_type, coefficients, derivative_level, precision = 4):
    """
    Calculates the critical points of a specific function at a certain derivative level

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which critical points must be determined (e.g., 'linear', 'quadratic')
    coefficients : list
        Coefficients to use to generate the equation to investigate
    derivative_level : int
        Integer corresponding to which derivative to investigate for critical points (1 for the first derivative and 2 for the second derivative)
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list containing elements that are integers or floats
    ValueError
        Third argument must be one of the following integers: [1, 2]
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points : list
        Values of the x-coordinates at which the original function's derivative either crosses the x-axis or does not exist; if the function is sinusoidal, then only five results within a two period interval will be listed, but a general form will also be included; if the derivative has no critical points, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.points.key_coordinates`

    Notes
    -----
    - Function to analyze: :math:`f(x)`
    - Derivative of the function: :math:`f'(x)`
    - Domain of the function: :math:`x_i = \\{ x_1, x_2, \\cdots, x_n \\}`
    - Potential critical points of the derivative: :math:`x_c = \\{ c \\mid c \\in x_i \\cap f'(c) = 0 \\cup f'(c) \\nexists \\}`
    - |critical_points|

    Examples
    --------
    Calulate the critical points of the second derivative of a cubic function with coefficients 2, 3, 5, and 7
        >>> points_cubic = critical_points('cubic', [2, 3, 5, 7], 2)
        >>> print(points_cubic)
        [-0.5]
    Calulate the critical points of the first derivative of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> points_sinusoidal = critical_points('sinusoidal', [2, 3, 5, 7], 1)
        >>> print(points_sinusoidal)
        [5.5236, 6.5708, 7.618, 8.6652, 9.7124, '5.5236 + 1.0472k']
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    select_integers(derivative_level, [1, 2], 'third')
    positive_integer(precision)
    results = []
    if derivative_level == 1:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            constants = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
            results = quadratic_roots(constants[0], constants[1], constants[2], precision)
        elif equation_type == 'hyperbolic':
            results = [0]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
        elif equation_type == 'logistic':
            results = [None]
        elif equation_type == 'sinusoidal':
            periodic_unit = pi / coefficients[1]
            initial_value = coefficients[2] + pi / (2 * coefficients[1])
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            values = [initial_value, first_value, second_value, third_value, fourth_value]
            sorted_values = sorted_list(values)
            rounded_values = []
            for number in sorted_values:
                rounded_values.append(rounded_value(number, precision))
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            rounded_initial_value = rounded_value(initial_value, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            results = [*rounded_values, general_form]
    elif derivative_level == 2:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            results = [None]
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'hyperbolic':
            results = [0]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
        elif equation_type == 'logistic':
            results = [rounded_value(coefficients[2], precision)]
        elif equation_type == 'sinusoidal':
            periodic_unit = pi / coefficients[1]
            initial_value = coefficients[2]
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            values = [initial_value, first_value, second_value, third_value, fourth_value]
            sorted_values = sorted_list(values)
            rounded_values = []
            for number in sorted_values:
                rounded_values.append(rounded_value(number, precision))
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            rounded_initial_value = rounded_value(initial_value, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            results = [*rounded_values, general_form]
    return results
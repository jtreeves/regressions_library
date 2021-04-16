from library.errors.analyses import select_equations
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from library.statistics.rounding import rounded_value
from .maxima import maxima_points
from .minima import minima_points
from .intervals import sign_chart

def extrema_points(equation_type, coefficients, precision = 4):
    """
    Calculates the extrema of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which extrema must be determined (e.g., 'linear', 'quadratic')
    coefficients : list
        Coefficients to use to generate the equation to investigate
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points['maxima'] : list
        Values of the x-coordinates at which the original function has a relative maximum; if the function is sinusoidal, then only two or three results within a two period interval will be listed, but a general form will also be included; if the function has no maxima, then it will return a list of `None`
    points['minima'] : list
        Values of the x-coordinates at which the original function has a relative minimum; if the function is sinusoidal, then only two or three results within a two period interval will be listed, but a general form will also be included; if the function has no minima, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.criticals.critical_points`, :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.maxima.maxima_points`, :func:`~library.analyses.minima.minima_points`, :func:`~library.analyses.points.key_coordinates`

    Notes
    -----
    - Critical points for the derivative of a function: :math:`c_i = \\{ c_1, c_2, c_3,  \\cdots, c_{n-1}, c_n \\}`
    - X-coordinates of the extrema of the function: :math:`x_{ext} = \\{ x \\mid x \\in c_i, \\left( f'(\\frac{c_{j-1} + c_j}{2}) < 0 \\cap f'(\\frac{c_j + c_{j+1}}{2}) > 0 \\right) \\\\ \\cup \\left( f'(\\frac{c_{j-1} + c_j}{2}) > 0 \\cap f'(\\frac{c_j + c_{j+1}}{2}) < 0 \\right) \\}`
    - |extrema_values|

    Examples
    --------
    Calulate the extrema of a cubic function with coefficients 1, -15, 63, and -7
        >>> points_cubic = extrema_points('cubic', [1, -15, 63, -7])
        >>> print(points_cubic['maxima'])
        [3.0]
        >>> print(points_cubic['minima'])
        [7.0]
    Calulate the extrema of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> points_sinusoidal = extrema_points('sinusoidal', [2, 3, 5, 7])
        >>> print(points_sinusoidal['maxima'])
        [5.5236, 7.618, 9.7124, '1.0472k']
        >>> print(points_sinusoidal['minima'])
        [6.5708, 8.6652, '1.0472k']
    """
    # Handle input errors
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    positive_integer(precision)
    
    # Determine maxima and minima
    max_points = maxima_points(equation_type, coefficients, precision)
    min_points = minima_points(equation_type, coefficients, precision)
    
    # Create object to return
    result = {}

    # Handle sinusoidal case
    if equation_type == 'sinusoidal':
        # Recreate sign chart
        intervals_set = sign_chart('sinusoidal', coefficients, 1, precision)

        # Grab general form
        general_form = intervals_set[-1]

        # Extract periodic unit
        periodic_unit_index = general_form.find(' + ') + 3
        periodic_unit = 2 * float(general_form[periodic_unit_index:-1])
        rounded_periodic_unit = rounded_value(periodic_unit, precision)

        # Create general forms for max and min
        max_general_form = str(max_points[0]) + ' + ' + str(rounded_periodic_unit) + 'k'
        min_general_form = str(min_points[0]) + ' + ' + str(rounded_periodic_unit) + 'k'

        # Append general form as final element of each list
        max_extended = max_points + [max_general_form]
        min_extended = min_points + [min_general_form]
        result = {
            'maxima': max_extended,
            'minima': min_extended
        }
    
    # Handle all other cases
    else:
        result = {
            'maxima': max_points,
            'minima': min_points
        }
    return result
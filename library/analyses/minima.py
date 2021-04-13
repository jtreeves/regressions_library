from library.errors.analyses import select_equations
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .intervals import sign_chart

def minima_points(equation_type, coefficients, precision = 4):
    """
    Calculates the minima of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which the minima must be determined (e.g., 'linear', 'quadratic')
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
    points : list
        Values of the x-coordinates at which the original function has a relative minimum; if the function is sinusoidal, then only two or three results within a two period interval will be listed, but a general form will also be included; if the function has no minima, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.criticals.critical_points`, :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.maxima.maxima_points`, :func:`~library.analyses.extrema.extrema_points`, :func:`~library.analyses.points.key_coordinates`

    Notes
    -----
    - Minima occur at x-coordinates where the sign of the first derivative changes from 'negative' to 'positive'
    - |minima_values|

    Examples
    --------
    Calculate the minima of a cubic function with coefficients 1, -15, 63, and -7
        >>> points_cubic = minima_points('cubic', [1, -15, 63, -7])
        >>> print(points_cubic)
        [7.0]
    Calculate the minima of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> points_sinusoidal = minima_points('sinusoidal', [2, 3, 5, 7])
        >>> print(points_sinusoidal)
        [6.5708, 8.6652, '1.0472k']
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    positive_integer(precision)
    result = []
    intervals = sign_chart(equation_type, coefficients, 1, precision)
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'negative' and intervals[i + 2] == 'positive':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result
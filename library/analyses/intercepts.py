from library.errors.analyses import select_equations
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .roots.linear import linear_roots
from .roots.quadratic import quadratic_roots
from .roots.cubic import cubic_roots
from .roots.hyperbolic import hyperbolic_roots
from .roots.exponential import exponential_roots
from .roots.logarithmic import logarithmic_roots
from .roots.logistic import logistic_roots
from .roots.sinusoidal import sinusoidal_roots

def intercept_points(equation_type, coefficients, precision = 4):
    """
    Calculates the roots of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which intercepts must be determined (e.g., 'linear', 'quadratic')
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
        Values of the x-coordinates at which the original function crosses the x-axis; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but general forms will also be included; if the function has no x-intercepts, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.criticals.critical_points`, :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.points.key_coordinates`

    Notes
    -----
    - Function to analyze: :math:`f(x)`
    - Domain of the function: :math:`x_i = \\{ x_1, x_2, \\cdots, x_n \\}`
    - X-intercepts (roots) of the function: :math:`x_r = \\{ r \\mid r \\in x_i and f(r) = 0 \\}`
    - |intercepts|

    Examples
    --------
    Calculate the roots of a cubic function with coefficients 1, -15, 66, and -80
        >>> points_cubic = intercept_points('cubic', [1, -15, 66, -80])
        >>> print(points_cubic)
        [2.0, 5.0, 8.0]
    Calculate the roots of a sinusoidal function with coefficients 3, 1, -2, and 3
        >>> points_sinusoidal = intercept_points('sinusoidal', [3, 1, -2, 3])
        >>> print(points_sinusoidal)
        [-3.5708, 2.7124, 8.9956, '-3.5708 + 6.2832k']
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    positive_integer(precision)
    result = []
    if equation_type == 'linear':
        result = linear_roots(*coefficients, precision)
    elif equation_type == 'quadratic':
        result = quadratic_roots(*coefficients, precision)
    elif equation_type == 'cubic':
        result = cubic_roots(*coefficients, precision)
    elif equation_type == 'hyperbolic':
        result = hyperbolic_roots(*coefficients, precision)
    elif equation_type == 'exponential':
        result = exponential_roots(*coefficients, precision)
    elif equation_type == 'logarithmic':
        result = logarithmic_roots(*coefficients, precision)
    elif equation_type == 'logistic':
        result = logistic_roots(*coefficients, precision)
    elif equation_type == 'sinusoidal':
        result = sinusoidal_roots(*coefficients, precision)
    return result
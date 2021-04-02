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

def intercept_points(equation_type, coefficients, precision):
    """
    Calculates the roots of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which extrema must be determined (e.g., 'linear', 'quadratic')
    coefficients : list or tuple
        Coefficients to use to generate the equation to investigate
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points : list
        Values of the x-coordinates at which the original function crosses the x-axis; if the function has no x-intercepts, then it will return a list of `None`

    Examples
    --------
    Calulate the roots of a cubic function with coefficients 1, -15, 63, and -7 (and round the results to two decimal places)
        >>> test = intercept_points('cubic', [1, -15, 63, -7], 2)
    Print the results
        >>> print(test)
        [0.11]
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
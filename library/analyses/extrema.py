from library.errors.analyses import select_equations, callable_function
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .criticals import critical_points
from .intervals import sign_chart
from .maxima import maxima_points
from .minima import minima_points

def extrema_points(equation_type, coefficients, derivative, precision):
    """
    Calculates the extrema of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which extrema must be determined (e.g., 'linear', 'quadratic')
    coefficients : list or tuple
        Coefficients to use to generate the equation to investigate
    derivative : function
        Function of the first derivative to use for generating a list of critical points
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    TypeError
        Third argument must be a callable function
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points['maxima'] : list
        Values of the x-coordinates at which the original function has a relative maximum; if the function has no maxima, then it will return a list of `None`
    points['minima'] : list
        Values of the x-coordinates at which the original function has a relative minimum; if the function has no minima, then it will return a list of `None`

    Examples
    --------
    Generate the derivatives of a cubic function with coefficients 1, -15, 63, and -7
        >>> test1 = cubic_derivatives(1, -15, 63, -7)
    Calulate the extrema of that cubic function (and round the results to four decimal places)
        >>> test2 = extrema_points('cubic', [1, -15, 63, -7], test1['first']['evaluation'], 4)
    Print the results
        >>> print(test2['maxima'])
        [3.0]
        >>> print(test2['minima'])
        [7.0]
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    callable_function(derivative, 'third')
    positive_integer(precision)
    points = critical_points(equation_type, 1, coefficients, precision)
    intervals_set = sign_chart(derivative, points)
    result = {}
    if equation_type == 'sinusoidal':
        general_form = intervals_set[-1]
        periodic_unit_index = general_form.find(' + ') + 3
        periodic_unit = general_form[periodic_unit_index:]
        max_points = maxima_points(intervals_set)
        min_points = minima_points(intervals_set)
        max_extended = max_points + [periodic_unit]
        min_extended = min_points + [periodic_unit]
        result = {
            'maxima': max_extended,
            'minima': min_extended
        }
    else:
        max_points = maxima_points(intervals_set)
        min_points = minima_points(intervals_set)
        result = {
            'maxima': max_points,
            'minima': min_points
        }
    return result
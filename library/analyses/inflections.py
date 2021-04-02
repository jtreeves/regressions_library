from library.errors.analyses import select_equations, callable_function
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .criticals import critical_points
from .intervals import sign_chart

def inflection_points(equation_type, coefficients, derivative, precision):
    """
    Calculates the inflection points of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which extrema must be determined (e.g., 'linear', 'quadratic')
    coefficients : list or tuple
        Coefficients to use to generate the equation to investigate
    derivative : function
        Function of the second derivative to use for generating a list of critical points
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
    points : list
        Values of the x-coordinates at which the original function has an inflection point; if the function has no inflection points, then it will return a list of `None`

    Examples
    --------
    Generate the derivatives of a cubic function with coefficients 1, -15, 63, and -7
        >>> test1 = cubic_derivatives(1, -15, 63, -7)
    Calulate the inflection points of that cubic function (and round the results to four decimal places)
        >>> test2 = inflection_points('cubic', [1, -15, 63, -7], test1['second']['evaluation'], 4)
    Print the results
        >>> print(test2)
        [5.0]
    
    ALTERNATIVE
    Calculate the inflection points of a cubic functions with coefficients 1, -15, 63, and -7 (and round the results to four decimal places)
        >>> test = inflection_points('cubic', [1, -15, 63, -7], lambda x : 6 * x - 30, 4)
        [5.0]
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    callable_function(derivative, 'third')
    positive_integer(precision)
    points = critical_points(equation_type, 2, coefficients, precision)
    intervals_set = sign_chart(derivative, points)
    result = []
    for i in range(len(intervals_set)):
        try:
            if (intervals_set[i] == 'positive' and intervals_set[i + 2] == 'negative') or (intervals_set[i] == 'negative' and intervals_set[i + 2] == 'positive'):
                try:
                    derivative(intervals_set[i + 1])
                    result.append(intervals_set[i + 1])
                except ZeroDivisionError:
                    break
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    if equation_type == 'sinusoidal':
        result.append(points[-1])
    return result
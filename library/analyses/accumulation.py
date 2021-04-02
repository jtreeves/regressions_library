from library.errors.scalars import compare_scalars, positive_integer
from library.errors.analyses import callable_function
from library.statistics.rounding import rounded_value

def accumulated_area(integral, start, end, precision):
    """
    Evaluates the definite integral between two points for a given integral

    Parameters
    ----------
    integral : function
        Function of the indefinite integral to use for evaluating the definite integral
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the definite integral
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the definite integral
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    TypeError
        First argument must be a callable function
    TypeError
        Second and third arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    area : float
        Definite integral of the original indefinite integral, evaluated between two points

    Examples
    --------
    Generate the integral of a linear function with coefficients 2 and 3
        >>> test = linear_integral(2, 3)
    Print the definite integral of that integral, evaluated from 10 to 20 (and round the area to four decimal places)
        >>> print(accumulated_area(test['evaluation'], 10, 20, 4))
        330.0
    """
    callable_function(integral, 'first')
    compare_scalars(start, end, 'second', 'third')
    positive_integer(precision)
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result
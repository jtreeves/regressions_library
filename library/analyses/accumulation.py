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
    area : int or float
        Definite integral of the original indefinite integral, evaluated between two points

    See Also
    --------
    :func:`~library.analyses.integrals.linear.linear_integral`, :func:`~library.analyses.integrals.quadratic.quadratic_integral`, :func:`~library.analyses.integrals.cubic.cubic_integral`, :func:`~library.analyses.integrals.hyperbolic.hyperbolic_integral`, :func:`~library.analyses.integrals.exponential.exponential_integral`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.analyses.integrals.logistic.logistic_integral`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`

    Notes
    -----
    Definite integral: :math:`\\int_{a}^{b} f(x) \\,dx = F(b) - F(a)`

    Examples
    --------
    Evaluate the definite integral of a linear function with coefficients 2 and 3 between the end points 10 and 20 (and round the area to four decimal places)
        >>> area_linear = accumulated_area(lambda x : x**2 + 3 * x, 10, 20, 4)
        >>> print(area_linear)
        330
    Evaluate the definite integral of a cubic function with coefficients 8, 6, -10, and 7 between the end points 10 and 20 (and round the area to four decimal places)
        >>> area_cubic = accumulated_area(lambda x : 2 * x**4 + 2 * x**3 - 5 * x**2 + 7 * x, 10, 20, 4)
        >>> print(area_cubic)
        312570
    """
    callable_function(integral, 'first')
    compare_scalars(start, end, 'second', 'third')
    positive_integer(precision)
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result
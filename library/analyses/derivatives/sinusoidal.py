from math import sin, cos
from library.errors.scalars import four_scalars

def sinusoidal_derivatives(first_constant, second_constant, third_constant, fourth_constant):
    """
    Calculates first and second derivatives of a sinusoidal function

    Parameters
    ----------
    first_constant : int or float
        Vertical stretch factor; amplitude
    second_constant : int or float
        Horizontal stretch factor; reciprocal relationship with period
    third_constant : int or float
        Horizontal shift; phase adjustment
    fourth_constant : int or float
        Vertical shift; midline

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    derivatives['first']['constants'] : list
        Coefficients of first derivative
    derivatives['first']['evaluation'] : function
        Function for evaluating first derivative at any float argument
    derivatives['second']['constants'] : list
        Coefficients of second derivative
    derivatives['second']['evaluation'] : function
        Function for evaluating second derivative at any float argument

    Examples
    --------
    Evaluate derivatives of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> test = sinusoidal_derivatives(2, 3, 5, 7)
    Print coefficients of first derivative
        >>> print(test['first']['constants'])
        [6, 3, 5]
    Print evaluation of second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
        -11.705181122828105
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    first_constants = [first_constant * second_constant, second_constant, third_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * cos(first_constants[1] * (variable - first_constants[2]))
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [-1 * first_constants[0] * first_constants[1], first_constants[1], first_constants[2]]
    def second_derivative(variable):
        evaluation = second_constants[0] * sin(second_constants[1] * (variable - second_constants[2]))
        return evaluation
    second_object = {
        'constants': second_constants,
        'evaluation': second_derivative
    }
    results = {
        'first': first_object,
        'second': second_object
    }
    return results
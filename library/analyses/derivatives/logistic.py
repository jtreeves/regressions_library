from math import exp
from library.errors.scalars import three_scalars

def logistic_derivatives(first_constant, second_constant, third_constant):
    """
    Calculates first and second derivatives of a logistic function

    Parameters
    ----------
    first_constant : int or float
        Carrying capacity of function
    second_constant : int or float
        Logistic growth rate
    third_constant : int or float
        Value of sigmoid's midpoint

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
    Evaluate derivatives of a logistic function with coefficients 2, 3, and 5
        >>> test = logistic_derivatives(2, 3, 5)
    Print coefficients of first derivative
        >>> print(test['first']['constants'])
        [6, 3, 5]
    Print evaluation of second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
        -5.506235031548963e-06
    """
    three_scalars(first_constant, second_constant, third_constant)
    first_constants = [first_constant * second_constant, second_constant, third_constant]
    def first_derivative(variable):
        exponential = exp(-1 * first_constants[1] * (variable - first_constants[2]))
        evaluation = first_constants[0] * exponential * (1 + exponential)**(-2)
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [first_constants[0] * first_constants[1], first_constants[1], first_constants[2]]
    def second_derivative(variable):
        exponential = exp(-1 * second_constants[1] * (variable - second_constants[2]))
        evaluation = second_constants[0] * exponential * (1 + exponential)**(-2) * (2 * exponential / (1 + exponential) - 1)
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
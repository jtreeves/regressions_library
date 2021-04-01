from math import log
from library.errors.scalars import two_scalars

def exponential_derivatives(first_constant, second_constant):
    """
    Calculates first and second derivatives of exponential function

    Parameters
    ----------
    first_constant : int or float
        Constant multiple
    second_constant : int or float
        Base rate of exponent

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
    Evaluate exponential derivatives with coefficients 2 and 3
        >>> test = exponential_derivatives(2, 3)
    Print coefficients of first derivative
        >>> print(test['first']['constants'])
        [2.1972245773362196, 3]
    Print evaluation of second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
        142538.25837404432
    """
    two_scalars(first_constant, second_constant)
    first_constants = [first_constant * log(second_constant), second_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * first_constants[1]**variable
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [first_constants[0] * log(first_constants[1]), first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * second_constants[1]**variable
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
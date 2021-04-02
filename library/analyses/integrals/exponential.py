from math import log
from library.errors.scalars import two_scalars

def exponential_integral(first_constant, second_constant):
    """
    Generates the integral of an exponential function

    Parameters
    ----------
    first_constant : int or float
        Constant multiple of the original exponential function
    second_constant : int or float
        Base rate of variable of the original exponential function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    integral['constants'] : list
        Coefficients of the resultant integral
    integral['evaluation'] : function
        Function for evaluating the resultant integral at any float or integer argument

    Examples
    --------
    Generate the integral of an exponential function with coefficients 2 and 3
        >>> integral = exponential_integral(2, 3)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [1.8204784532536746, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        107497.43218617623
    """
    two_scalars(first_constant, second_constant)
    constants = [first_constant / log(second_constant), second_constant]
    def exponential_evaluation(variable):
        evaluation = constants[0] * constants[1]**variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': exponential_evaluation
    }
    return results
from math import exp, log
from library.errors.scalars import three_scalars

def logistic_integral(first_constant, second_constant, third_constant):
    """
    Generates the integral of a logistic function

    Parameters
    ----------
    first_constant : int or float
        Carrying capacity of the original logistic function
    second_constant : int or float
        Growth rate of the original logistic function
    third_constant : int or float
        Value of the sigmoid's midpoint of the original logistic function

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
    Generate the integral of a logistic function with coefficients 2, 3, and 5
        >>> test = logistic_integral(2, 3, 5)
    Print the coefficients of the integral
        >>> print(test['constants'])
        [0.6666666666666666, 3, 5]
    Print the evaluation of the integral at an input of 10
        >>> print(test['evaluation'](10))
        10.00000020393485
    """
    three_scalars(first_constant, second_constant, third_constant)
    constants = [first_constant / second_constant, second_constant, third_constant]
    def logistic_evaluation(variable):
        evaluation = constants[0] * log(abs(exp(constants[1] * (variable - constants[2])) + 1))
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logistic_evaluation
    }
    return results
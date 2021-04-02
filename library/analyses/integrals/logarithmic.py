from math import log
from library.errors.scalars import two_scalars

def logarithmic_integral(first_constant, second_constant):
    """
    Generates the integral of a logarithmic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the original logarithmic function
    second_constant : int or float
        Coefficient of the constant term of the original logarithmic function

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
    Generate the integral of a logarithmic function with coefficients 2 and 3
        >>> test = logarithmic_integral(2, 3)
    Print the coefficients of the integral
        >>> print(test['constants'])
        [2, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(test['evaluation'](10))
        56.05170185988092
    """
    two_scalars(first_constant, second_constant)
    constants = [first_constant, second_constant]
    def logarithmic_evaluation(variable):
        evaluation = constants[0] * variable * (log(variable) - 1) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results
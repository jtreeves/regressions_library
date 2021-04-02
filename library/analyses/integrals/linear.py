from library.errors.scalars import two_scalars

def linear_integral(first_constant, second_constant):
    """
    Generates the integral of a linear function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term of the original linear function
    second_constant : int or float
        Coefficient of the constant term of the original linear function

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
    Generate the integral of a linear function with coefficients 2 and 3
        >>> test = linear_integral(2, 3)
    Print the coefficients of the integral
        >>> print(test['constants'])
        [1.0, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(test['evaluation'](10))
        130.0
    """
    two_scalars(first_constant, second_constant)
    constants = [(1/2) * first_constant, second_constant]
    def linear_evaluation(variable):
        evaluation = constants[0] * variable**2 + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': linear_evaluation
    }
    return results
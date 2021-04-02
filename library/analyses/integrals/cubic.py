from library.errors.scalars import four_scalars

def cubic_integral(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates the integral of a cubic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the cubic term of the original cubic function
    second_constant : int or float
        Coefficient of the quadratic term of the original cubic function
    third_constant : int or float
        Coefficient of the linear term of the original cubic function
    fourth_constant : int or float
        Coefficient of the constant term of the original cubic function

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
    Generate the integral of a cubic function with coefficients 2, 3, 5, and 7
        >>> test = cubic_integral(2, 3, 5, 7)
    Print the coefficients of the integral
        >>> print(test['constants'])
        [0.5, 1.0, 2.5, 7]
    Print the evaluation of the integral at an input of 10
        >>> print(test['evaluation'](10))
        6320.0
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    constants = [(1/4) * first_constant, (1/3) * second_constant, (1/2) * third_constant, fourth_constant]
    def cubic_evaluation(variable):
        evaluation = constants[0] * variable**4 + constants[1] * variable**3 + constants[2] * variable**2 + constants[3] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': cubic_evaluation
    }
    return results
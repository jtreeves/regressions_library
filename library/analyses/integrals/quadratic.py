from library.errors.scalars import three_scalars

def quadratic_integral(first_constant, second_constant, third_constant):
    """
    Generates the integral of a quadratic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the quadratic term of the original quadratic function
    second_constant : int or float
        Coefficient of the linear term of the original quadratic function
    third_constant : int or float
        Coefficient of the constant term of the original quadratic function

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
    Generate the integral of a quadratic function with coefficients 2, 3, and 5
        >>> integral = quadratic_integral(2, 3, 5)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [0.6666666666666666, 1.5, 5]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        866.6666666666666
    """
    three_scalars(first_constant, second_constant, third_constant)
    constants = [(1/3) * first_constant, (1/2) * second_constant, third_constant]
    def quadratic_evaluation(variable):
        evaluation = constants[0] * variable**3 + constants[1] * variable**2 + constants[2] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': quadratic_evaluation
    }
    return results
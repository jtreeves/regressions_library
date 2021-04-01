from library.errors.scalars import two_scalars

def linear_derivatives(first_constant, second_constant):
    """
    Calculates first and second derivatives of a linear function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term
    second_constant : int or float
        Coefficient of the constant term

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
    Evaluate derivatives of a linear function with coefficients 2 and 3
        >>> test = linear_derivatives(2, 3)
    Print coefficients of first derivative
        >>> print(test['first']['constants'])
        [2]
    Print evaluation of second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
        0
    """
    two_scalars(first_constant, second_constant)
    first_constants = [first_constant]
    def first_derivative(variable):
        evaluation = first_constants[0]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [0]
    def second_derivative(variable):
        evaluation = second_constants[0]
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
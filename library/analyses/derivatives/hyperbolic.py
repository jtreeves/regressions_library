from library.errors.scalars import two_scalars

def hyperbolic_derivatives(first_constant, second_constant):
    """
    Calculates the first and second derivatives of a hyperbolic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the reciprocal variable of the original hyperbolic function
    second_constant : int or float
        Coefficient of the constant term of the original hyperbolic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    derivatives['first']['constants'] : list
        Coefficients of the resultant first derivative
    derivatives['first']['evaluation'] : function
        Function for evaluating the resultant first derivative at any float or integer argument
    derivatives['second']['constants'] : list
        Coefficients of the resultant second derivative
    derivatives['second']['evaluation'] : function
        Function for evaluating the resultant second derivative at any float or integer argumentor evaluating second derivative at any float argument

    Examples
    --------
    Generate the derivatives of a hyperbolic function with coefficients 2 and 3
        >>> derivatives = hyperbolic_derivatives(2, 3)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [-2]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        0.004
    """
    two_scalars(first_constant, second_constant)
    first_constants = [-1 * first_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] / variable**2
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [-2 * first_constants[0]]
    def second_derivative(variable):
        evaluation = second_constants[0] / variable**3
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
from library.errors.scalars import two_scalars

def hyperbolic_derivatives(first_constant, second_constant):
    """
    Calculates first and second derivatives of a hyperbolic function

    Parameters
    ----------
    first_constant : int or float
        Constant multiple of reciprocal variable
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
    Evaluate derivatives of a hyperbolic function with coefficients 2 and 3
        >>> test = hyperbolic_derivatives(2, 3)
    Print coefficients of first derivative
        >>> print(test['first']['constants'])
        [-2]
    Print evaluation of second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
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

test = hyperbolic_derivatives(2, 3)
print(test['first']['constants'])
print(test['second']['evaluation'](10))
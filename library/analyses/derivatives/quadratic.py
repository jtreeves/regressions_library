from library.errors.scalars import three_scalars

def quadratic_derivatives(first_constant, second_constant, third_constant):
    """
    Calculates the first and second derivatives of a quadratic function

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
    derivatives['first']['constants'] : list
        Coefficients of the resultant first derivative
    derivatives['first']['evaluation'] : function
        Function for evaluating the resultant first derivative at any float or integer argument
    derivatives['second']['constants'] : list
        Coefficients of the resultant second derivative
    derivatives['second']['evaluation'] : function
        Function for evaluating the resultant second derivative at any float or integer argument

    Examples
    --------
    Generate the derivatives of a quadratic function with coefficients 2, 3, and 5
        >>> test = quadratic_derivatives(2, 3, 5)
    Print the coefficients of the first derivative
        >>> print(test['first']['constants'])
        [4, 3]
    Print the evaluation of the second derivative at an input of 10
        >>> print(test['second']['evaluation'](10))
        4
    """
    three_scalars(first_constant, second_constant, third_constant)
    first_constants = [2 * first_constant, second_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable + first_constants[1]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [first_constants[0]]
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
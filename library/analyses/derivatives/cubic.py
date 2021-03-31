from library.errors.scalars import four_scalars

def cubic_derivatives(first_constant, second_constant, third_constant, fourth_constant):
    """
    Calculates first and second derivatives of cubic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the cubic term
    second_constant : int or float
        Coefficient of the quadratic term
    third_constant : int or float
        Coefficient of the linear term
    fourth_constant : int or float
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
    Print coefficients of first derivative
        >>> cbdr = cubic_derivatives(2, 3, 5, 7)
        >>> print(cbdr['first']['constants'])
        [6, 6, 5]
    Evaluate second derivative with an input of 10
        >>> cbdr = cubic_derivatives(2, 3, 5, 7)
        >>> scnd = cbdr['second']['evaluation']
        >>> eval = scnd(10)
        >>> print(eval)
        126
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    first_constants = [3 * first_constant, 2 * second_constant, third_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable**2 + first_constants[1] * variable + first_constants[2]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [2 * first_constants[0], first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * variable + second_constants[1]
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
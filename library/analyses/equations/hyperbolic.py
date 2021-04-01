from library.errors.scalars import two_scalars

def hyperbolic_equation(first_constant, second_constant):
    """
    Generates a hyperbolic function to provide evaluations at variable inputs

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
    evaluation : function
        Function for evaluating a hyperbolic equation when passed any integer or float arguments

    Examples
    --------
    Create a hyperbolic function with coefficients 2 and 3
        >>> test = hyperbolic_equation(2, 3)
    Print evaluation of function at an input of 10
        >>> print(test(10))
        3.2
    """
    two_scalars(first_constant, second_constant)
    def hyperbolic_evaluation(variable):
        result = first_constant / variable + second_constant
        return result
    return hyperbolic_evaluation
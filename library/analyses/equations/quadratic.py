from library.errors.scalars import three_scalars

def quadratic_equation(first_constant, second_constant, third_constant):
    """
    Generates a quadratic function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the quadratic term of the resultant quadratic function
    second_constant : int or float
        Coefficient of the linear term of the resultant quadratic function
    third_constant : int or float
        Coefficient of the constant term of the resultant quadratic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a quadratic equation when passed any integer or float argument

    Examples
    --------
    Create a quadratic function with coefficients 2, 3, and 5
        >>> test = quadratic_equation(2, 3, 5)
    Print the evaluation of the function at an input of 10
        >>> print(test(10))
        235
    """
    three_scalars(first_constant, second_constant, third_constant)
    def quadratic_evaluation(variable):
        result = first_constant * variable**2 + second_constant * variable + third_constant
        return result
    return quadratic_evaluation
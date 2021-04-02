from library.errors.scalars import two_scalars

def linear_equation(first_constant, second_constant):
    """
    Generates a linear function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term of the resultant linear function
    second_constant : int or float
        Coefficient of the constant term of the resultant linear function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a linear equation when passed any integer or float argument

    Examples
    --------
    Create a linear function with coefficients 2 and 3
        >>> test = linear_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(test(10))
        23
    """
    two_scalars(first_constant, second_constant)
    def linear_evaluation(variable):
        result = first_constant * variable + second_constant
        return result
    return linear_evaluation
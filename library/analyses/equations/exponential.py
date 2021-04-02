from library.errors.scalars import two_scalars

def exponential_equation(first_constant, second_constant):
    """
    Generates an exponential function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Constant multiple of the resultant exponential function
    second_constant : int or float
        Base rate of variable of the resultant exponential function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating an exponential equation when passed any integer or float argument

    Examples
    --------
    Create an exponential function with coefficients 2 and 3
        >>> test = exponential_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(test(10))
        118098
    """
    two_scalars(first_constant, second_constant)
    def exponential_evaluation(variable):
        result = first_constant * second_constant**variable
        return result
    return exponential_evaluation
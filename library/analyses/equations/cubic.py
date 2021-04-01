from library.errors.scalars import four_scalars

def cubic_equation(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates a cubic function to provide evaluations at variable inputs

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
    evaluation : function
        Function for evaluating a cubic equation when passed any integer or float arguments

    Examples
    --------
    Create a cubic function with coefficients 2, 3, 5, and 7
        >>> test = cubic_equation(2, 3, 5, 7)
    Print evaluation of function at an input of 10
        >>> print(test(10))
        2357
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    def cubic_evaluation(variable):
        result = first_constant * variable**3 + second_constant * variable**2 + third_constant * variable + fourth_constant
        return result
    return cubic_evaluation
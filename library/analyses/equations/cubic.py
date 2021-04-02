from library.errors.scalars import four_scalars

def cubic_equation(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates a cubic function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the cubic term of the resultant cubic function
    second_constant : int or float
        Coefficient of the quadratic term of the resultant cubic function
    third_constant : int or float
        Coefficient of the linear term of the resultant cubic function
    fourth_constant : int or float
        Coefficient of the constant term of the resultant cubic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a cubic equation when passed any integer or float argument

    Examples
    --------
    Create a cubic function with coefficients 2, 3, 5, and 7
        >>> evaluation = cubic_equation(2, 3, 5, 7)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        2357
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    def cubic_evaluation(variable):
        result = first_constant * variable**3 + second_constant * variable**2 + third_constant * variable + fourth_constant
        return result
    return cubic_evaluation
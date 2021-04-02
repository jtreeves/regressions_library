from math import exp
from library.errors.scalars import three_scalars

def logistic_equation(first_constant, second_constant, third_constant):
    """
    Generates a logistic function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Carrying capacity of the resultant logistic function
    second_constant : int or float
        Growth rate of the resultant logistic function
    third_constant : int or float
        Value of the sigmoid's midpoint of the resultant logistic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a logistic equation when passed any integer or float argument

    Examples
    --------
    Create a logistic function with coefficients 2, 3, and 5
        >>> test = logistic_equation(2, 3, 5)
    Print the evaluation of the function at an input of 10
        >>> print(test(10))
        1.999999388195546
    """
    three_scalars(first_constant, second_constant, third_constant)
    def logistic_evaluation(variable):
        result = first_constant * (1 + exp(-1 * second_constant * (variable - third_constant)))**(-1)
        return result
    return logistic_evaluation
from math import sin
from library.errors.scalars import four_scalars

def sinusoidal_equation(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates a sinusoidal function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Vertical stretch factor of the resultant sine function
    second_constant : int or float
        Horizontal stretch factor of the resultant sine function
    third_constant : int or float
        Horizontal shift of the resultant sine function
    fourth_constant : int or float
        Vertical shift of the resultant sine function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a sinusoidal equation when passed any integer or float argument

    Examples
    --------
    Create a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> evaluation = sinusoidal_equation(2, 3, 5, 7)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        8.300575680314234
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    def sinusoidal_evaluation(variable):
        result = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return result
    return sinusoidal_evaluation
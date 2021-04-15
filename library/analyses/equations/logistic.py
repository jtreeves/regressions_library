from math import exp
from library.errors.scalars import three_scalars
from library.errors.adjustments import no_zeroes

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

    See Also
    --------
    :func:`~library.analyses.derivatives.logistic.logistic_derivatives`, :func:`~library.analyses.integrals.logistic.logistic_integral`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.models.logistic.logistic_model`

    Notes
    -----
    - Standard form of a logistic function: :math:`f(x) = \\frac{a}{1 + \\text{e}^{-b\\cdot(x - c)}}`
    - |logistic_functions|

    Examples
    --------
    Create a logistic function with coefficients 2, 3, and 5
        >>> evaluation = logistic_equation(2, 3, 5)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        1.999999388195546
    """
    # Handle input errors
    three_scalars(first_constant, second_constant, third_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant])

    # Create evaluation
    def logistic_evaluation(variable):
        result = coefficients[0] * (1 + exp(-1 * coefficients[1] * (variable - coefficients[2])))**(-1)
        return result
    return logistic_evaluation
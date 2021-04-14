from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

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

    See Also
    --------
    :func:`~library.analyses.derivatives.linear.linear_derivatives`, :func:`~library.analyses.integrals.linear.linear_integral`, :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.models.linear.linear_model`

    Notes
    -----
    - Standard form of a linear function: :math:`f(x) = a\\cdot{x} + b`
    - |linear_functions|

    Examples
    --------
    Create a linear function with coefficients 2 and 3
        >>> evaluation = linear_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        23
    """
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])
    def linear_evaluation(variable):
        result = coefficients[0] * variable + coefficients[1]
        return result
    return linear_evaluation
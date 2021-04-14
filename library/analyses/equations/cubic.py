from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

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
    
    See Also
    --------
    :func:`~library.analyses.derivatives.cubic.cubic_derivatives`, :func:`~library.analyses.integrals.cubic.cubic_integral`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.models.cubic.cubic_model`

    Notes
    -----
    - Standard form of a cubic function: :math:`f(x) = a\\cdot{x^3} + b\\cdot{x^2} + c\\cdot{x} + d`
    - |cubic_functions|

    Examples
    --------
    Create a cubic function with coefficients 2, 3, 5, and 7
        >>> evaluation = cubic_equation(2, 3, 5, 7)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        2357
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])
    def cubic_evaluation(variable):
        result = coefficients[0] * variable**3 + coefficients[1] * variable**2 + coefficients[2] * variable + coefficients[3]
        return result
    return cubic_evaluation
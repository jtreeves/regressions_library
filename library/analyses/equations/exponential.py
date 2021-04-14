from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

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
    
    See Also
    --------
    :func:`~library.analyses.derivatives.exponential.exponential_derivatives`, :func:`~library.analyses.integrals.exponential.exponential_integral`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.models.exponential.exponential_model`

    Notes
    -----
    - Standard form of an exponential function: :math:`f(x) = a\\cdot{b^x}`
    - |exponential_functions|

    Examples
    --------
    Create an exponential function with coefficients 2 and 3
        >>> evaluation = exponential_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        118098
    """
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])
    def exponential_evaluation(variable):
        result = coefficients[0] * coefficients[1]**variable
        return result
    return exponential_evaluation
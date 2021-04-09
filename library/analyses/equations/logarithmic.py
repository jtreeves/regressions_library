from math import log
from library.errors.scalars import two_scalars

def logarithmic_equation(first_constant, second_constant):
    """
    Generates a logarithmic function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the resultant logarithmic function
    second_constant : int or float
        Coefficient of the constant term of the resultant logarithmic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a logarithmic equation when passed any integer or float argument

    See Also
    --------
    :func:`~library.analyses.derivatives.logarithmic.logarithmic_derivatives`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.models.logarithmic.logarithmic_model`

    Notes
    -----
    - Standard form of a logarithmic function: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - |logarithmic_functions|

    Examples
    --------
    Create a logarithmic function with coefficients 2 and 3
        >>> evaluation = logarithmic_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        7.605170185988092
    """
    two_scalars(first_constant, second_constant)
    def logarithmic_evaluation(variable):
        result = first_constant * log(variable) + second_constant 
        return result
    return logarithmic_evaluation
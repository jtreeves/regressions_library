from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

def hyperbolic_equation(first_constant, second_constant):
    """
    Generates a hyperbolic function to provide evaluations at variable inputs

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the reciprocal variable of the resultant hyperbolic function
    second_constant : int or float
        Coefficient of the constant term of the resultant hyperbolic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    evaluation : function
        Function for evaluating a hyperbolic equation when passed any integer or float argument

    See Also
    --------
    :func:`~library.analyses.derivatives.hyperbolic.hyperbolic_derivatives`, :func:`~library.analyses.integrals.hyperbolic.hyperbolic_integral`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.models.hyperbolic.hyperbolic_model`

    Notes
    -----
    - Standard form of a hyperbolic function: :math:`f(x) = a\\cdot{\\frac{1}{x}} + b`
    - |rational_functions|

    Examples
    --------
    Create a hyperbolic function with coefficients 2 and 3
        >>> evaluation = hyperbolic_equation(2, 3)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        3.2
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])

    # Create evaluation
    def hyperbolic_evaluation(variable):
        # Circumvent division by zero
        if variable == 0:
            variable = 0.0001
        result = coefficients[0] / variable + coefficients[1]
        return result
    return hyperbolic_evaluation
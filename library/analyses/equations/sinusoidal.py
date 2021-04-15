from math import sin
from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

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

    See Also
    --------
    :func:`~library.analyses.derivatives.sinusoidal.sinusoidal_derivatives`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`, :func:`~library.models.sinusoidal.sinusoidal_model`

    Notes
    -----
    - Standard form of a sinusoidal function: :math:`f(x) = a\\cdot{\\sin(b\\cdot(x - c))} + d`

        - Period of function: :math:`\\frac{2\\pi}{|b|}`
        - Amplitude of function: :math:`|a|`

    - |sine_functions|

    Examples
    --------
    Create a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> evaluation = sinusoidal_equation(2, 3, 5, 7)
    Print the evaluation of the function at an input of 10
        >>> print(evaluation(10))
        8.300575680314234
    """
    # Handle input errors
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])

    # Create evaluation
    def sinusoidal_evaluation(variable):
        result = coefficients[0] * sin(coefficients[1] * (variable - coefficients[2])) + coefficients[3]
        return result
    return sinusoidal_evaluation
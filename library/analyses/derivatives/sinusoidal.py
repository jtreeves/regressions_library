from math import sin, cos
from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

def sinusoidal_derivatives(first_constant, second_constant, third_constant, fourth_constant):
    """
    Calculates the first and second derivatives of a sinusoidal function

    Parameters
    ----------
    first_constant : int or float
        Vertical stretch factor of the original sine function
    second_constant : int or float
        Horizontal stretch factor of the original sine function
    third_constant : int or float
        Horizontal shift of the original sine function
    fourth_constant : int or float
        Vertical shift of the original sine function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    derivatives['first']['constants'] : list
        Coefficients of the resultant first derivative
    derivatives['first']['evaluation'] : function
        Function for evaluating the resultant first derivative at any float or integer argument
    derivatives['second']['constants'] : list
        Coefficients of the resultant second derivative
    derivatives['second']['evaluation'] : function
        Function for evaluating the resultant second derivative at any float or integer argument

    See Also
    --------
    :func:`~library.analyses.equations.sinusoidal.sinusoidal_equation`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`, :func:`~library.models.sinusoidal.sinusoidal_model`

    Notes
    -----
    - Standard form of a sinusoidal function: :math:`f(x) = a\\cdot{\\sin(b\\cdot(x - c))} + d`
    - First derivative of a sinusoidal function: :math:`f'(x) = ab\\cdot{\\cos(b\\cdot(x - c))}`
    - Second derivative of a sinusoidal function: :math:`f''(x) = -ab^2\\cdot{\\sin(b\\cdot(x - c))}`
    - |differentiation_formulas|
    - |chain_rule|
    - |trigonometric|

    Examples
    --------
    Generate the derivatives of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> derivatives = sinusoidal_derivatives(2, 3, 5, 7)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [6, 3, 5]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        -11.705181122828105
    """
    # Handle input errors
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])

    # Create first derivative
    first_constants = [coefficients[0] * coefficients[1], coefficients[1], coefficients[2]]
    def first_derivative(variable):
        evaluation = first_constants[0] * cos(first_constants[1] * (variable - first_constants[2]))
        return evaluation
    first_dictionary = {
        'constants': first_constants,
        'evaluation': first_derivative
    }

    # Create second derivative
    second_constants = [-1 * first_constants[0] * first_constants[1], first_constants[1], first_constants[2]]
    def second_derivative(variable):
        evaluation = second_constants[0] * sin(second_constants[1] * (variable - second_constants[2]))
        return evaluation
    second_dictionary = {
        'constants': second_constants,
        'evaluation': second_derivative
    }

    # Package both derivatives in single dictionary
    results = {
        'first': first_dictionary,
        'second': second_dictionary
    }
    return results
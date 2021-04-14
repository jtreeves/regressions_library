from math import cos
from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

def sinusoidal_integral(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates the integral of a sinusoidal function

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
    integral['constants'] : list
        Coefficients of the resultant integral
    integral['evaluation'] : function
        Function for evaluating the resultant integral at any float or integer argument

    See Also
    --------
    :func:`~library.analyses.equations.sinusoidal.sinusoidal_equation`, :func:`~library.analyses.derivatives.sinusoidal.sinusoidal_derivatives`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`, :func:`~library.models.sinusoidal.sinusoidal_model`

    Notes
    -----
    - Standard form of a sinusoidal function: :math:`f(x) = a\\cdot{\\sin(b\\cdot(x - c))} + d`
    - Integral of a sinusoidal function: :math:`F(x) = -\\frac{a}{b}\\cdot{\\cos(b\\cdot(x - c))} + d\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|
    - |substitution_rule|

    Examples
    --------
    Generate the integral of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> integral = sinusoidal_integral(2, 3, 5, 7)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [-0.6666666666666666, 3, 5, 7]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        70.50645860857254
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])
    constants = [-1 * coefficients[0] / coefficients[1], coefficients[1], coefficients[2], coefficients[3]]
    def sinusoidal_evaluation(variable):
        evaluation = constants[0] * cos(constants[1] * (variable - constants[2])) + constants[3] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': sinusoidal_evaluation
    }
    return results
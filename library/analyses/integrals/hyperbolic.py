from math import log
from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

def hyperbolic_integral(first_constant, second_constant):
    """
    Generates the integral of a hyperbolic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the reciprocal variable of the original hyperbolic function
    second_constant : int or float
        Coefficient of the constant term of the original hyperbolic function

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
    :func:`~library.analyses.equations.hyperbolic.hyperbolic_equation`, :func:`~library.analyses.derivatives.hyperbolic.hyperbolic_derivatives`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.models.hyperbolic.hyperbolic_model`

    Notes
    -----
    - Standard form of a hyperbolic function: :math:`f(x) = a\\cdot{\\frac{1}{x}} + b`
    - Integral of a hyperbolic function: :math:`F(x) = a\\cdot{\\ln|x|} + b\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|

    Examples
    --------
    Generate the integral of a hyperbolic function with coefficients 2 and 3
        >>> integral = hyperbolic_integral(2, 3)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [2, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        34.605170185988094
    """
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])
    constants = [coefficients[0], coefficients[1]]
    def hyperbolic_evaluation(variable):
        if variable == 0:
            variable = 0.0001
        evaluation = constants[0] * log(abs(variable)) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': hyperbolic_evaluation
    }
    return results
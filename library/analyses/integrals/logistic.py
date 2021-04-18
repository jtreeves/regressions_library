from math import exp, log
from library.errors.scalars import three_scalars
from library.errors.adjustments import no_zeroes

def logistic_integral(first_constant, second_constant, third_constant):
    """
    Generates the integral of a logistic function

    Parameters
    ----------
    first_constant : int or float
        Carrying capacity of the original logistic function
    second_constant : int or float
        Growth rate of the original logistic function
    third_constant : int or float
        Value of the sigmoid's midpoint of the original logistic function

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
    :func:`~library.analyses.equations.logistic.logistic_equation`, :func:`~library.analyses.derivatives.logistic.logistic_derivatives`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.models.logistic.logistic_model`

    Notes
    -----
    - Standard form of a logistic function: :math:`f(x) = \\frac{a}{1 + \\text{e}^{-b\\cdot(x - c)}}`
    - Integral of a logistic function: :math:`F(x) = \\frac{a}{b}\\cdot{\\ln|\\text{e}^{b\\cdot(x - c)} + 1|}`
    - |indefinite_integral|
    - |integration_formulas|
    - |substitution_rule|

    Examples
    --------
    Generate the integral of a logistic function with coefficients 2, 3, and 5
        >>> integral = logistic_integral(2, 3, 5)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [0.6666666666666666, 3, 5]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        10.00000020393485
    """
    # Handle input errors
    three_scalars(first_constant, second_constant, third_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant])

    # Create constants
    constants = [coefficients[0] / coefficients[1], coefficients[1], coefficients[2]]

    # Create evaluation
    def logistic_evaluation(variable):
        evaluation = constants[0] * log(abs(exp(constants[1] * (variable - constants[2])) + 1))
        return evaluation
    
    # Package constants and evaluation in single dictionary
    results = {
        'constants': constants,
        'evaluation': logistic_evaluation
    }
    return results
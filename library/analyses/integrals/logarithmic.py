from math import log
from library.errors.scalars import two_scalars

def logarithmic_integral(first_constant, second_constant):
    """
    Generates the integral of a logarithmic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the original logarithmic function
    second_constant : int or float
        Coefficient of the constant term of the original logarithmic function

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
    :func:`~library.analyses.equations.logarithmic.logarithmic_equation`, :func:`~library.analyses.derivatives.logarithmic.logarithmic_derivatives`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.models.logarithmic.logarithmic_model`

    Notes
    -----
    - Standard form of a logarithmic function: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - Integral of a logarithmic function: :math:`F(x) = a\\cdot{x}\\cdot(\\ln{x} - 1) + b\\cdot{x}`

    Examples
    --------
    Generate the integral of a logarithmic function with coefficients 2 and 3
        >>> integral = logarithmic_integral(2, 3)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [2, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        56.05170185988092
    """
    two_scalars(first_constant, second_constant)
    constants = [first_constant, second_constant]
    def logarithmic_evaluation(variable):
        evaluation = constants[0] * variable * (log(variable) - 1) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results
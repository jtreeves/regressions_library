from math import log
from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

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
    - |indefinite_integral|
    - |integration_formulas|
    - |integration_by_parts|

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
    # Handle input errors
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])

    # Create constants
    constants = [coefficients[0], coefficients[1]]

    # Create evaluation
    def logarithmic_evaluation(variable):
        # Circumvent logarithm of zero
        if variable == 0:
            variable = 0.0001
        evaluation = constants[0] * variable * (log(abs(variable)) - 1) + constants[1] * variable
        return evaluation
    
    # Create object to return
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results
from math import log
from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

def exponential_integral(first_constant, second_constant):
    """
    Generates the integral of an exponential function

    Parameters
    ----------
    first_constant : int or float
        Constant multiple of the original exponential function
    second_constant : int or float
        Base rate of variable of the original exponential function

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
    :func:`~library.analyses.equations.exponential.exponential_equation`, :func:`~library.analyses.derivatives.exponential.exponential_derivatives`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.models.exponential.exponential_model`

    Notes
    -----
    - Standard form of an exponential function: :math:`f(x) = a\\cdot{b^x}`
    - Integral of an exponential function: :math:`F(x) = \\frac{a}{\\ln{b}}\\cdot{b^x}`
    - |indefinite_integral|
    - |integration_formulas|

    Examples
    --------
    Generate the integral of an exponential function with coefficients 2 and 3
        >>> integral = exponential_integral(2, 3)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [1.8204784532536746, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        107497.43218617623
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])

    # Circumvent division by zero
    if coefficients[1] == 1:
        coefficients[1] = 1.0001
    
    # Create constants
    constants = [coefficients[0] / log(abs(coefficients[1])), coefficients[1]]

    # Create evaluation
    def exponential_evaluation(variable):
        evaluation = constants[0] * constants[1]**variable
        return evaluation
    
    # Create object to return
    results = {
        'constants': constants,
        'evaluation': exponential_evaluation
    }
    return results
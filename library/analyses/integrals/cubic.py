from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

def cubic_integral(first_constant, second_constant, third_constant, fourth_constant):
    """
    Generates the integral of a cubic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the cubic term of the original cubic function
    second_constant : int or float
        Coefficient of the quadratic term of the original cubic function
    third_constant : int or float
        Coefficient of the linear term of the original cubic function
    fourth_constant : int or float
        Coefficient of the constant term of the original cubic function

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
    :func:`~library.analyses.equations.cubic.cubic_equation`, :func:`~library.analyses.derivatives.cubic.cubic_derivatives`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.models.cubic.cubic_model`

    Notes
    -----
    - Standard form of a cubic function: :math:`f(x) = a\\cdot{x^3} + b\\cdot{x^2} + c\\cdot{x} + d`
    - Integral of a cubic function: :math:`F(x) = \\frac{a}{4}\\cdot{x^4} + \\frac{b}{3}\\cdot{x^3} + \\frac{c}{2}\\cdot{x^2} + d\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|

    Examples
    --------
    Generate the integral of a cubic function with coefficients 2, 3, 5, and 7
        >>> integral = cubic_integral(2, 3, 5, 7)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [0.5, 1.0, 2.5, 7]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        6320.0
    """
    # Handle input errors
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])

    # Generate constants
    constants = [(1/4) * coefficients[0], (1/3) * coefficients[1], (1/2) * coefficients[2], coefficients[3]]

    # Create evaluation
    def cubic_evaluation(variable):
        evaluation = constants[0] * variable**4 + constants[1] * variable**3 + constants[2] * variable**2 + constants[3] * variable
        return evaluation
    
    # Create object to return
    results = {
        'constants': constants,
        'evaluation': cubic_evaluation
    }
    return results
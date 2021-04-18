from library.errors.scalars import three_scalars
from library.errors.adjustments import no_zeroes

def quadratic_integral(first_constant, second_constant, third_constant):
    """
    Generates the integral of a quadratic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the quadratic term of the original quadratic function
    second_constant : int or float
        Coefficient of the linear term of the original quadratic function
    third_constant : int or float
        Coefficient of the constant term of the original quadratic function

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
    :func:`~library.analyses.equations.quadratic.quadratic_equation`, :func:`~library.analyses.derivatives.quadratic.quadratic_derivatives`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.models.quadratic.quadratic_model`

    Notes
    -----
    - Standard form of a quadratic function: :math:`f(x) = a\\cdot{x^2} + b\\cdot{x} + c`
    - Integral of a quadratic function: :math:`F(x) = \\frac{a}{3}\\cdot{x^3} + \\frac{b}{2}\\cdot{x^2} + c\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|

    Examples
    --------
    Generate the integral of a quadratic function with coefficients 2, 3, and 5
        >>> integral = quadratic_integral(2, 3, 5)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [0.6666666666666666, 1.5, 5]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        866.6666666666666
    """
    # Handle input errors
    three_scalars(first_constant, second_constant, third_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant])

    # Create constants
    constants = [(1/3) * coefficients[0], (1/2) * coefficients[1], coefficients[2]]

    # Create evaluation
    def quadratic_evaluation(variable):
        evaluation = constants[0] * variable**3 + constants[1] * variable**2 + constants[2] * variable
        return evaluation
    
    # Package constants and evaluation in single dictionary
    results = {
        'constants': constants,
        'evaluation': quadratic_evaluation
    }
    return results
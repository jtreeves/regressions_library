from library.errors.scalars import two_scalars

def linear_integral(first_constant, second_constant):
    """
    Generates the integral of a linear function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the linear term of the original linear function
    second_constant : int or float
        Coefficient of the constant term of the original linear function

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
    :func:`~library.analyses.equations.linear.linear_equation`, :func:`~library.analyses.derivatives.linear.linear_derivatives`, :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.models.linear.linear_model`

    Notes
    -----
    - Standard form of a linear function: :math:`f(x) = a\\cdot{x} + b`
    - Integral of a linear function: :math:`F(x) = \\frac{a}{2}\\cdot{x^2} + b\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|

    Examples
    --------
    Generate the integral of a linear function with coefficients 2 and 3
        >>> integral = linear_integral(2, 3)
    Print the coefficients of the integral
        >>> print(integral['constants'])
        [1.0, 3]
    Print the evaluation of the integral at an input of 10
        >>> print(integral['evaluation'](10))
        130.0
    """
    two_scalars(first_constant, second_constant)
    constants = [(1/2) * first_constant, second_constant]
    def linear_evaluation(variable):
        evaluation = constants[0] * variable**2 + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': linear_evaluation
    }
    return results
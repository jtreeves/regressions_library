from library.errors.scalars import four_scalars
from library.errors.adjustments import no_zeroes

def cubic_derivatives(first_constant, second_constant, third_constant, fourth_constant):
    """
    Calculates the first and second derivatives of a cubic function

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
    :func:`~library.analyses.equations.cubic.cubic_equation`, :func:`~library.analyses.integrals.cubic.cubic_integral`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.models.cubic.cubic_model`

    Notes
    -----
    - Standard form of a cubic function: :math:`f(x) = a\\cdot{x^3} + b\\cdot{x^2} + c\\cdot{x} + d`
    - First derivative of a cubic function: :math:`f'(x) = 3a\\cdot{x^2} + 2b\\cdot{x} + c`
    - Second derivative of a cubic function: :math:`f''(x) = 6a\\cdot{x} + 2b`
    - |differentiation_formulas|

    Examples
    --------
    Generate the derivatives of a cubic function with coefficients 2, 3, 5, and 7
        >>> derivatives = cubic_derivatives(2, 3, 5, 7)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [6, 6, 5]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        126
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    coefficients = no_zeroes([first_constant, second_constant, third_constant, fourth_constant])
    first_constants = [3 * coefficients[0], 2 * coefficients[1], coefficients[2]]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable**2 + first_constants[1] * variable + first_constants[2]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [2 * first_constants[0], first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * variable + second_constants[1]
        return evaluation
    second_object = {
        'constants': second_constants,
        'evaluation': second_derivative
    }
    results = {
        'first': first_object,
        'second': second_object
    }
    return results
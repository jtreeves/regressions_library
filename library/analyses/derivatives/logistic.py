from math import exp
from library.errors.scalars import three_scalars

def logistic_derivatives(first_constant, second_constant, third_constant):
    """
    Calculates the first and second derivatives of a logistic function

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
    :func:`~library.analyses.equations.logistic.logistic_equation`, :func:`~library.analyses.integrals.logistic.logistic_integral`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.models.logistic.logistic_model`

    Notes
    -----
    - Standard form of a logistic function: :math:`f(x) = \\frac{a}{1 + \\text{e}^{-b\\cdot(x - c)}}`
    - First derivative of a logistic function: :math:`f'(x) = \\frac{ab\\cdot{\\text{e}^{-b\\cdot(x - c)}}}{(1 + \\text{e}^{-b\\cdot(x - c)})^2}`
    - Second derivative of a logistic function: :math:`f''(x) = \\frac{2ab^2\\cdot{\\text{e}^{-2b\\cdot(x - c)}}}{(1 + \\text{e}^{-b\\cdot(x - c)})^3} - \\frac{ab^2\\cdot{\\text{e}^{-b\\cdot(x - c)}}}{(1 + \\text{e}^{-b\\cdot(x - c)})^2}`

    Examples
    --------
    Generate the derivatives of a logistic function with coefficients 2, 3, and 5
        >>> derivatives = logistic_derivatives(2, 3, 5)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [6, 3, 5]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        -5.506235031548963e-06
    """
    three_scalars(first_constant, second_constant, third_constant)
    first_constants = [first_constant * second_constant, second_constant, third_constant]
    def first_derivative(variable):
        exponential = exp(-1 * first_constants[1] * (variable - first_constants[2]))
        evaluation = first_constants[0] * exponential * (1 + exponential)**(-2)
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [first_constants[0] * first_constants[1], first_constants[1], first_constants[2]]
    def second_derivative(variable):
        exponential = exp(-1 * second_constants[1] * (variable - second_constants[2]))
        evaluation = second_constants[0] * exponential * (1 + exponential)**(-2) * (2 * exponential / (1 + exponential) - 1)
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
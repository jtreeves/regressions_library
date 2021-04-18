from math import log
from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

def exponential_derivatives(first_constant, second_constant):
    """
    Calculates the first and second derivatives of an exponential function

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
    :func:`~library.analyses.equations.exponential.exponential_equation`, :func:`~library.analyses.integrals.exponential.exponential_integral`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.models.exponential.exponential_model`

    Notes
    -----
    - Standard form of an exponential function: :math:`f(x) = a\\cdot{b^x}`
    - First derivative of an exponential function: :math:`f'(x) = a\\cdot{\\ln{b}\\cdot{b^x}}`
    - Second derivative of an exponential function: :math:`f''(x) = a\\cdot{\\ln^2{b}\\cdot{b^x}}`
    - |differentiation_formulas|
    - |exponential|

    Examples
    --------
    Generate the derivatives of an exponential function with coefficients 2 and 3
        >>> derivatives = exponential_derivatives(2, 3)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [2.1972245773362196, 3]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        142538.25837404432
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])

    # Create first derivative
    first_constants = [coefficients[0] * log(abs(coefficients[1])), coefficients[1]]
    def first_derivative(variable):
        evaluation = first_constants[0] * first_constants[1]**variable
        return evaluation
    first_dictionary = {
        'constants': first_constants,
        'evaluation': first_derivative
    }

    # Create second derivative
    second_constants = [first_constants[0] * log(abs(first_constants[1])), first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * second_constants[1]**variable
        return evaluation
    second_dictionary = {
        'constants': second_constants,
        'evaluation': second_derivative
    }

    # Package both derivatives in single dictionary
    results = {
        'first': first_dictionary,
        'second': second_dictionary
    }
    return results
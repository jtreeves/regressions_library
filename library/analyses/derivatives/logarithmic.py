from library.errors.scalars import two_scalars
from library.errors.adjustments import no_zeroes

def logarithmic_derivatives(first_constant, second_constant):
    """
    Calculates the first and second derivatives of a logarithmic function

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
    :func:`~library.analyses.equations.logarithmic.logarithmic_equation`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.models.logarithmic.logarithmic_model`

    Notes
    -----
    - Standard form of a logarithmic function: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - First derivative of a logarithmic function: :math:`f'(x) = a\\cdot{\\frac{1}{x}}`
    - Second derivative of a logarithmic function: :math:`f''(x) = -a\\cdot{\\frac{1}{x^2}}`
    - |differentiation_formulas|
    - |logarithmic|

    Examples
    --------
    Generate the derivatives of a logarithmic function with coefficients 2 and 3
        >>> derivatives = logarithmic_derivatives(2, 3)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [2]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        -0.02
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    coefficients = no_zeroes([first_constant, second_constant])

    # Create first derivative
    first_constants = [coefficients[0]]
    def first_derivative(variable):
        # Circumvent division by zero
        if variable == 0:
            variable = 0.0001
        evaluation = first_constants[0] / variable
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }

    # Create second derivative
    second_constants = [-1 * first_constants[0]]
    def second_derivative(variable):
        # Circumvent division by zero
        if variable == 0:
            variable = 0.0001
        evaluation = second_constants[0] / variable**2
        return evaluation
    second_object = {
        'constants': second_constants,
        'evaluation': second_derivative
    }

    # Create object to return
    results = {
        'first': first_object,
        'second': second_object
    }
    return results
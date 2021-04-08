from library.errors.scalars import two_scalars

def linear_derivatives(first_constant, second_constant):
    """
    Calculates the first and second derivatives of a linear function

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
    :func:`~library.analyses.equations.linear.linear_equation`, :func:`~library.analyses.integrals.linear.linear_integral`, :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.models.linear.linear_model`

    Notes
    -----
    - Standard form of a linear function: :math:`f(x) = ax + b`
    - First derivative of a linear function: :math:`f'(x) = a`
    - Second derivative of a linear function: :math:`f''(x) = 0`

    Examples
    --------
    Generate the derivatives of a linear function with coefficients 2 and 3
        >>> derivatives = linear_derivatives(2, 3)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [2]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        0
    """
    two_scalars(first_constant, second_constant)
    first_constants = [first_constant]
    def first_derivative(variable):
        evaluation = first_constants[0]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [0]
    def second_derivative(variable):
        evaluation = second_constants[0]
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
def callable_function(function, position):
    """
    Ensures argument at a given position is a callable function

    Parameters
    ----------
    function : function
        Callable function that performs some operation
    position : str
        String representing the position of the vector argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First argument must be a callable function

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm lambda x : x + 1 is a callable function
        >>> confirmation = callable_function(lambda x : x + 1, 'first')
        >>> print(confirmation)
        First argument is a callable function
    Confirm 1 is not a callable function
        >>> failure = callable_function(1, 'first')
        TypeError: First argument must be a callable function
    """
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not callable(function):
        raise TypeError(f'{identifier.capitalize()} must be a callable function')
    else:
        return f'{identifier.capitalize()} is a callable function'

def select_equations(string):
    """
    Ensures argument is one of a select strings representing the key 8 kinds of equations: 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', and 'sinusoidal'

    Parameters
    ----------
    string : str
        String representing a kind of equation (e.g., 'linear', 'quadratic')

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 'hyperbolic' is one of the 8 key types of equations
        >>> confirmation = select_equations('hyperbolic')
        >>> print(confirmation)
        First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    Confirm 'rational' is not one of the 8 key types of equations
        >>> failure = select_equations('rational')
        ValueError: First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    """
    choices = ['linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', 'sinusoidal']
    if string not in choices:
        raise ValueError("First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
    else:
        return "First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'"
def scalar_value(scalar, position):
    """
    Ensures argument at a given position is an integer or a float

    Parameters
    ----------
    scalar : int or float
        Number representing a scalar
    position : str
        String representing the position of the scalar argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First argument must be an integer or a float

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 is a scalar
        >>> confirmation = scalar_value(1, 'first')
        >>> print(confirmation)
        First argument is an integer or a float
    Confirm 'one' is not a scalar
        >>> failure = scalar_value('one', 'first')
        TypeError: First argument must be an integer or a float
    """
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(scalar, (int, float)):
        raise TypeError(f'{identifier.capitalize()} must be an integer or a float')
    else:
        return f'{identifier.capitalize()} is an integer or a float'

def two_scalars(scalar_one, scalar_two):
    """
    Ensures both arguments are integers or floats

    Parameters
    ----------
    scalar_one : int or float
        Number representing a scalar
    scalar_two : int or float
        Number representing a scalar

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 and 2 are both scalar values
        >>> confirmation = two_scalars(1, 2)
        >>> print(confirmation)
        Both first and second arguments are integers or floats
    Confirm 1 and 'two' are not both scalar values
        >>> failure = two_scalars(1, 'two')
        TypeError: Second argument must be an integer or a float
    """
    scalar_value(scalar_one, 'first')
    scalar_value(scalar_two, 'second')
    return 'Both first and second arguments are integers or floats'

def three_scalars(scalar_one, scalar_two, scalar_three):
    """
    Ensures all three arguments are integers or floats

    Parameters
    ----------
    scalar_one : int or float
        Number representing a scalar
    scalar_two : int or float
        Number representing a scalar
    scalar_three : int or float
        Number representing a scalar

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1, 2, and 3 are all scalar values
        >>> confirmation = three_scalars(1, 2, 3)
        >>> print(confirmation)
        First, second, and third arguments are all integers or floats
    Confirm 1, 'two', and 3 are not all scalar values
        >>> failure = three_scalars(1, 'two', 3)
        TypeError: Second argument must be an integer or a float
    """
    two_scalars(scalar_one, scalar_two)
    scalar_value(scalar_three, 'third')
    return 'First, second, and third arguments are all integers or floats'

def four_scalars(scalar_one, scalar_two, scalar_three, scalar_four):
    """
    Ensures all four arguments are integers or floats

    Parameters
    ----------
    scalar_one : int or float
        Number representing a scalar
    scalar_two : int or float
        Number representing a scalar
    scalar_three : int or float
        Number representing a scalar
    scalar_four : int or float
        Number representing a scalar

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1, 2, 3, and 4 are all scalar values
        >>> confirmation = four_scalars(1, 2, 3, 4)
        >>> print(confirmation)
        First, second, third, and fourth arguments are all integers or floats
    Confirm 1, 2, 3, and 'four' are not all scalar values
        >>> failure = four_scalars(1, 2, 3, 'four')
        TypeError: Fourth argument must be an integer or a float
    """
    three_scalars(scalar_one, scalar_two, scalar_three)
    scalar_value(scalar_four, 'fourth')
    return 'First, second, third, and fourth arguments are all integers or floats'

def compare_scalars(scalar_one, scalar_two, position_one, position_two):
    """
    Ensures first argument is less than second argument

    Parameters
    ----------
    scalar_one : int or float
        Number representing a scalar
    scalar_two : int or float
        Number representing a scalar
    position_one : str
        String representing the position of the first scalar argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')
    position_two : str
        String representing the position of the second scalar argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First two arguments must be integers or floats
    ValueError
        First argument must be less than second argument

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 is less than 2
        >>> confirmation = compare_scalars(1, 2, 'first', 'second')
        >>> print(confirmation)
        First argument is less than second argument
    Confirm 2 is not less than 1
        >>> failure = compare_scalars(2, 1, 'first', 'second')
        ValueError: First argument must be less than second argument
    """
    scalar_value(scalar_one, position_one)
    scalar_value(scalar_two, position_two)
    if scalar_one >= scalar_two:
        raise ValueError(f'{position_one.capitalize()} argument must be less than {position_two} argument')
    else:
        return f'{position_one.capitalize()} argument is less than {position_two} argument'

def positive_integer(scalar):
    """
    Ensures argument is a positive integer

    Parameters
    ----------
    scalar : int
        Number representing a scalar

    Raises
    ------
    ValueError
        Argument must be a positive integer

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 is a positive integer
        >>> confirmation = positive_integer(1)
        >>> print(confirmation)
        Last argument is a positive integer
    Confirm 0 is not a positive integer
        >>> failure = positive_integer(0)
        ValueError: Last argument must be a positive integer
    """
    if not isinstance(scalar, int) or not scalar > 0:
        raise ValueError('Last argument must be a positive integer')
    else:
        return 'Last argument is a positive integer'

def whole_number(scalar, position):
    """
    Ensures argument at a given position is a whole number

    Parameters
    ----------
    scalar : int
        Number representing a scalar
    position : str
        String representing the position of the scalar argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    ValueError
        First argument must be a whole number

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 0 is a whole number
        >>> confirmation = whole_number(0, 'first')
        >>> print(confirmation)
        First argument is a whole number
    Confirm -1 is not a whole number
        >>> failure = whole_number(-1, 'first')
        ValueError: First argument must be a whole number
    """
    if not isinstance(scalar, int) or not scalar >= 0:
        raise ValueError(f'{position.capitalize()} argument must be a whole number')
    else:
        return f'{position.capitalize()} argument is a whole number'

def select_integers(scalar, choices):
    """
    Ensures first argument appears as an element in the second argument

    Parameters
    ----------
    scalar : int or float
        Number representing a scalar
    choices : list or tuple
        List of numbers

    Raises
    ------
    ValueError
        First argument must be an integer contained within the second argument

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 is an element of [1, 2]
        >>> confirmation = select_integers(1, [1, 2])
        >>> print(confirmation)
        Second argument is one of the following integers: [1, 2]
    Confirm 3 is not an element of [1, 2]
        >>> failure = select_integers(3, [1, 2])
        ValueError: Second argument must be one of the following integers: [1, 2]
    """
    if scalar not in choices:
        raise ValueError(f'Second argument must be one of the following integers: {choices}')
    else:
        return f'Second argument is one of the following integers: {choices}'

def allow_none_scalar(scalar):
    """
    Ensures argument is an integer, float, or None

    Parameters
    ----------
    scalar : int or float
        Element representing a scalar

    Raises
    ------
    TypeError
        Argument must be an integer, a float, or None

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm 1 is an integer, a float, or None
        >>> confirmation1 = allow_none_scalar(1)
        >>> print(confirmation1)
        First argument is an integer, a float, or None
    Confirm None is an integer, a float, or None
        >>> confirmation2 = allow_none_scalar(None)
        >>> print(confirmation2)
        First argument is an integer, a float, or None
    Confirm 'one' is neither an integer, a float, nor None
        >>> failure = allow_none_scalar('one')
        TypeError: First argument must be an integer, a float, or None
    """
    if not isinstance(scalar, (int, float)) and scalar is not None:
        raise TypeError('First argument must be an integer, a float, or None')
    else:
        return 'First argument is an integer, a float, or None'
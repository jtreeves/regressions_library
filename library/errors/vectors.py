def vector_of_scalars(vector, position):
    """
    Ensures argument at a given position is a vector containing scalar values

    Parameters
    ----------
    vector : list or tuple
        List of numbers representing a vector
    position : str
        String representing the position of the vector argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        Elements of first argument must be integers or floats

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [1, 2, 3] is a vector of scalars
        >>> confirmation = vector_of_scalars([1, 2, 3], 'first')
        >>> print(confirmation)
        First argument is a 1-dimensional list or tuple containing elements that are integers or floats
    Confirm ['one', 2, 3] is not a vector of scalars
        >>> failure = vector_of_scalars(['one', 2, 3], 'first')
        TypeError: Elements of first argument must be integers or floats
    """
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError(f'{identifier.capitalize()} must be a 1-dimensional list or tuple')
    if not isinstance(vector[0], (int, float)):
        raise TypeError(f'Elements of {identifier} must be integers or floats')
    else:
        return f'{identifier.capitalize()} is a 1-dimensional list or tuple containing elements that are integers or floats'

def compare_vectors(vector_one, vector_two):
    """
    Ensures both arguments are vectors with the same number of elements

    Parameters
    ----------
    vector_one : list or tuple
        List of numbers representing a vector
    vector_two : list or tuple
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Arguments must be 1-dimensional lists or tuples
    TypeError
        Elements of arguments must be integers or floats
    ValueError
        Both arguments must contain the same number of elements

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Compare [1, 2, 3] and [4, 5, 6]
        >>> confirmation = compare_vectors([1, 2, 3], [4, 5, 6])
        >>> print(confirmation)
        Both arguments contain the same number of elements
    Compare [1, 2, 3] and [4, 5]
        >>> failure = compare_vectors([1, 2, 3], [4, 5])
        ValueError: Both arguments must contain the same number of elements
    """
    vector_of_scalars(vector_one, 'first')
    vector_of_scalars(vector_two, 'second')
    if len(vector_one) is not len(vector_two):
        raise ValueError('Both arguments must contain the same number of elements')
    else:
        return 'Both arguments contain the same number of elements'

def multitype_vector(vector):
    """
    Ensures argument is a vector containing strings and scalar values

    Parameters
    ----------
    vector : list or tuple
        List of strings and numbers representing a vector

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    ValueError
        First element of argument must be either 'constant', 'positive', or 'negative'
    TypeError
        Second element of argument must be an integer or a float

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm ['positive', 2, 'negative'] is a multitype vector
        >>> confirmation = multitype_vector(['positive', 2, 'negative'])
        >>> print(confirmation)
        Argument is a 1-dimensional list or tuple with an initial element of either 'constant', 'positive', or 'negative'; if it contains a second element, then its second element is an integer or a float
    Confirm ['one', 2, 3] is not a proper multitype vector because of its first element
        >>> failure = multitype_vector(['one', 2, 3])
        ValueError: First element of argument must be either 'constant', 'positive', or 'negative'
    """
    first_options = ['constant', 'positive', 'negative']
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('Argument must be a 1-dimensional list or tuple')
    if vector[0] not in first_options:
        raise ValueError("First element of argument must be either 'constant', 'positive', or 'negative'")
    if len(vector) > 1 and not isinstance(vector[1], (int, float)):
        raise TypeError('Second element of argument must be an integer or a float')
    else:
        return "Argument is a 1-dimensional list or tuple with an initial element of either 'constant', 'positive', or 'negative'; if it contains a second element, then its second element is an integer or a float"

def allow_none_vector(vector, position):
    """
    Ensures argument at a particular position is a vector containing scalar values or possibly `None`

    Parameters
    ----------
    vector : list or tuple
        List of numbers (or possibly `None`) representing a vector
    position : str
        String representing the position of the vector argument within the parent function, expressed as an ordinal (e.g., 'first', 'second')

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        First element of first argument must be either an integer, a float, or `None`
    TypeError
        Second element of first argument must be an integer or a float

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [1, 2, 3] is a vector that may contain `None`
        >>> confirmation1 = allow_none_vector([1, 2, 3], 'first')
        >>> print(confirmation1)
        First argument is a 1-dimensional list or tuple that only contains integers, floats, or None; if it contains a second element, then its second element is an integer or a float
    Confirm [None] is a vector that may contain `None`
        >>> confirmation2 = allow_none_vector([None], 'first')
        >>> print(confirmation2)
        First argument is a 1-dimensional list or tuple that only contains integers, floats, or None; if it contains a second element, then its second element is an integer or a float
    Confirm [1, None] is not a vector that meets the required conditions
        >>> failure = allow_none_vector([1, None], 'first')
        TypeError: Second element of first argument must be an integer or a float
    """
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError(f'{identifier.capitalize()} must be a 1-dimensional list or tuple')
    if not isinstance(vector[0], (int, float)) and vector[0] is not None:
        raise TypeError(f'{identifier.capitalize()} can only contain integers, floats, or None')
    if len(vector) > 1 and not isinstance(vector[1], (int, float)):
        raise TypeError(f'Second element of {identifier} must be an integer or a float')
    else:
        return f'{identifier.capitalize()} is a 1-dimensional list or tuple that only contains integers, floats, or None; if it contains a second element, then its second element is an integer or a float'

def length(vector, size):
    """
    Ensures vector is exactly a certain length

    Parameters
    ----------
    vector : list or tuple
        List of elements representing a vector
    size : int
        Number representing the required length of the vector

    Raises
    ------
    ValueError
        First argument must contain exactly the number of elements specified by the second argument

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [1, 2, 3] is a vector of length 3
        >>> confirmation = length([1, 2, 3], 3)
        >>> print(confirmation)
        Argument contains exactly 3 elements
    Confirm [1, 2, 3] is not a vector of length 2
        >>> failure = length([1, 2, 3], 2)
        ValueError: Argument contains exactly 2 elements
    """
    if not len(vector) == size:
        raise ValueError(f'Argument must contain exactly {size} elements')
    else:
        return f'Argument contains exactly {size} elements'

def long_vector(vector):
    """
    Ensures vector contains at least 10 elements

    Parameters
    ----------
    vector : list or tuple
        List of elements representing a vector

    Raises
    ------
    ValueError
        Argument must contain at least 10 elements

    Returns
    -------
    confirmation : str
        Note declaring that all necessary conditions were met

    Examples
    --------
    Confirm [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is a vector with at least 10 elements
        >>> confirmation = long_vector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> print(confirmation)
        First argument contains at least 10 elements
    Confirm [1, 2, 3] is not a vector with at least 10 elements
        >>> failure = length([1, 2, 3])
        ValueError: First argument must contain at least 10 elements
    """
    if not len(vector) >= 10:
        raise ValueError(f'First argument must contain at least 10 elements')
    else:
        return f'First argument contains at least 10 elements'
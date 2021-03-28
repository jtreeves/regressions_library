def vector_of_scalars(vector, position):
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

def compare_vectors(vector_one, vector_two):
    vector_of_scalars(vector_one, 'first')
    vector_of_scalars(vector_two, 'second')
    if len(vector_one) is not len(vector_two):
        raise ValueError('Both arguments must contain the same number of elements')

def multitype_vector(vector):
    first_options = ['constant', 'positive', 'negative']
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('First argument must be a 1-dimensional list or tuple')
    if vector[0] not in first_options:
        raise ValueError("First element of first argument must be either 'constant', 'positive', or 'negative'")
    if len(vector) > 1:
        if not isinstance(vector[1], (int, float)):
            raise ValueError('Second element of first argument must be an integer or a float')

def allow_none_vector(vector, position):
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
    if len(vector) > 1:
        if not isinstance(vector[1], (int, float)):
            raise ValueError(f'Second element of {identifier} must be an integer or a float')

def length(vector, size):
    if not len(vector) == size:
        raise ValueError(f'Argument must contain exactly {size} elements')
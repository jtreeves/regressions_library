from .positions import argument_position

def confirm_vector(vector, position = 'only'):
    identifier = argument_position(position)
    if not isinstance(vector, list) or isinstance(vector[0], list):
        raise TypeError(f'{identifier.capitalize()} must be a 1-dimensional list')
    else:
        return f'{identifier.capitalize()} is a 1-dimensional list'

def vector_of_scalars(vector, position = 'only'):
    confirm_vector(vector, position)
    identifier = argument_position(position)
    for scalar in vector:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f'Elements of {identifier} must be integers or floats')
    else:
        return f'{identifier.capitalize()} is a 1-dimensional list containing elements that are integers or floats'

def compare_vectors(vector_one, vector_two):
    confirm_vector(vector_one, 'first')
    confirm_vector(vector_two, 'second')
    if len(vector_one) is not len(vector_two):
        raise ValueError('Both arguments must contain the same number of elements')
    else:
        return 'Both arguments contain the same number of elements'

def length(vector, size):
    if not len(vector) == size:
        raise ValueError(f'Argument must contain exactly {size} elements')
    else:
        return f'Argument contains exactly {size} elements'

def long_vector(vector):
    if not len(vector) >= 10:
        raise ValueError(f'First argument must contain at least 10 elements')
    else:
        return f'First argument contains at least 10 elements'
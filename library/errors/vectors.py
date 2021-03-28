def first_vector(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('First argument must be a 1-dimensional list or tuple')
    if not isinstance(vector[0], (int, float)):
        raise TypeError('Elements of first argument must be integers or floats')

def second_vector(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('Last argument must be a 1-dimensional list or tuple')
    if not isinstance(vector[0], (int, float)):
        raise TypeError('Elements of last argument must be integers or floats')

def compare_vectors(vector_one, vector_two):
    first_vector(vector_one)
    second_vector(vector_two)
    if len(vector_one) is not len(vector_two):
        raise ValueError('Both arguments must contain the same number of elements')

def length(vector, size):
    if not len(vector) == size:
        raise ValueError(f'Argument must contain exactly {size} elements')
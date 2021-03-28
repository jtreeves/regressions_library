def callable_function(function):
    if not callable(function):
        raise TypeError('First argument must be a callable function')

def select_equations(string):
    choices = ['linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', 'sinusoidal']
    if string not in choices:
        raise ValueError("First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")

def multitype_vector(vector):
    first_options = ['constant', 'positive', 'negative']
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('First argument must be a 1-dimensional list or tuple')
    if vector[0] not in first_options:
        raise ValueError("First element of first argument must be either 'constant', 'positive', or 'negative'")
    if vector[1] and not isinstance(vector[1], (int, float)):
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
    if not isinstance(vector[0], (int, float, None)):
        raise TypeError(f'{identifier.capitalize()} can only contain integers, floats, or None')
    if vector[1] and not isinstance(vector[1], (int, float)):
        raise ValueError(f'Second element of {identifier} must be an integer or a float')
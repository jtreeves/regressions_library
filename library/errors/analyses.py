def callable_function(function):
    if not callable(function):
        raise TypeError('First argument must be a callable function')

def multitype_vector(vector):
    first_options = ['constant', 'positive', 'negative']
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError('First argument must be a 1-dimensional list or tuple')
    if vector[0] not in first_options:
        raise ValueError("First element of first argument must be either 'constant', 'positive', or 'negative'")
    if vector[1] and not isinstance(vector[1], (int, float)):
        raise ValueError('Second element of first argument must be an integer or a float')

def select_equations(string):
    choices = ['linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', 'sinusoidal']
    if string not in choices:
        raise ValueError("First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
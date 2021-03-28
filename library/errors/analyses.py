def callable_function(function, position):
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
    choices = ['linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', 'sinusoidal']
    if string not in choices:
        raise ValueError("First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
    else:
        return "First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'"
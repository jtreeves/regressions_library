from .linear import linear
from .quadratic import quadratic
from .cubic import cubic
from .hyperbolic import hyperbolic
from .exponential import exponential
from .logarithmic import logarithmic

def best(data):
    errors = {
        'linear': linear(data)['error'],
        'quadratic': quadratic(data)['error'],
        'cubic': cubic(data)['error'],
        'hyperbolic': hyperbolic(data)['error'],
        'exponential': exponential(data)['error'],
        'logarithmic': logarithmic(data)['error']
    }
    minimum = min(errors, key=errors.get)
    choice = {
        'function': minimum,
        'error': errors[minimum]
    }
    return choice
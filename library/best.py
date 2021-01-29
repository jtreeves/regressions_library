from .models.linear import linear
from .models.quadratic import quadratic
from .models.cubic import cubic
from .models.hyperbolic import hyperbolic
from .models.exponential import exponential
from .models.logarithmic import logarithmic

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
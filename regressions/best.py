from .linear import linear
from .quadratic import quadratic
from .cubic import cubic
from .hyperbolic import hyperbolic
from .exponential import exponential
from .logarithmic import logarithmic

def best(data):
    errors = {
        'linear_error': linear(data)['error'],
        'quadratic_error': quadratic(data)['error'],
        'cubic_error': cubic(data)['error'],
        'hyperbolic_error': hyperbolic(data)['error'],
        'exponential_error': exponential(data)['error'],
        'logarithmic_error': logarithmic(data)['error'],
        'shortest': {
            'function': 'linear_error',
            'error': linear(data)['error']
        }
    }
    for evaluation in errors:
        if errors[evaluation] < errors['shortest']['error']:
            errors['shortest']['function'] = evaluation
            errors['shortest']['error'] = errors[evaluation]
    choice = errors['shortest']
    return choice
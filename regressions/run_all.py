from .linear import linear
from .quadratic import quadratic
from .cubic import cubic
from .hyperbolic import hyperbolic
from .exponential import exponential
from .logarithmic import logarithmic
from .best import best

def run_all(data):
    options = {
        'linear': linear(data),
        'quadratic': quadratic(data),
        'cubic': cubic(data),
        'hyperbolic': hyperbolic(data),
        'exponential': exponential(data),
        'logarithmic': logarithmic(data)
    }
    optimal = best(data)
    result = {
        'options': options,
        'optimal': optimal
    }
    return result
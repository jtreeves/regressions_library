from .models.linear import linear
from .models.quadratic import quadratic
from .models.cubic import cubic
from .models.hyperbolic import hyperbolic
from .models.exponential import exponential
from .models.logarithmic import logarithmic

def run_all(data):
    models = {
        'linear': linear(data),
        'quadratic': quadratic(data),
        'cubic': cubic(data),
        'hyperbolic': hyperbolic(data),
        'exponential': exponential(data),
        'logarithmic': logarithmic(data)
    }
    correlations = {
        'linear': models['linear']['correlation'],
        'quadratic': models['quadratic']['correlation'],
        'cubic': models['cubic']['correlation'],
        'hyperbolic': models['hyperbolic']['correlation'],
        'exponential': models['exponential']['correlation'],
        'logarithmic': models['logarithmic']['correlation']
    }
    choices = {
        k: v for k, v in correlations.items() if v is not None
    }
    maximum = max(choices, key=choices.get)
    optimal = {
        'option': maximum,
        'correlation': choices[maximum]
    }
    result = {
        'models': models,
        'optimal': optimal
    }
    return result

test_set = [[3, 4], [5, 11], [10, 13], [15, 5]]
test_eval = run_all(test_set)
print(test_eval)
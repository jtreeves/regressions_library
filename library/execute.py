from .models.linear import linear
from .models.quadratic import quadratic
from .models.cubic import cubic
from .models.hyperbolic import hyperbolic
from .models.exponential import exponential
from .models.logarithmic import logarithmic
from .statistics.minimum import minimum
from .statistics.maximum import maximum
from .statistics.quartiles import quartiles
from .statistics.mean import mean
from .statistics.median import median
from .vectors.dimension import dimension

def run_all(data):
    independent_variable = dimension(data, 1)
    models = {
        'linear': linear(data),
        'quadratic': quadratic(data),
        'cubic': cubic(data),
        'hyperbolic': hyperbolic(data),
        'exponential': exponential(data),
        'logarithmic': logarithmic(data)
    }
    statistics = {
        'minimum': minimum(independent_variable),
        'maximum': maximum(independent_variable),
        'q1': quartiles(independent_variable, 1),
        'q3': quartiles(independent_variable, 3),
        'mean': mean(independent_variable),
        'median': median(independent_variable)
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
    best = max(choices, key=choices.get)
    optimal = {
        'option': best,
        'correlation': choices[best]
    }
    result = {
        'models': models,
        'statistics': statistics,
        'optimal': optimal
    }
    return result

test_set = [[3, 4], [5, 11], [10, 13], [15, 5]]
test_eval = run_all(test_set)
print(test_eval)
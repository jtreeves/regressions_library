from .errors.matrices import matrix_of_scalars
from .errors.scalars import positive_integer
from .models.linear import linear_model
from .models.quadratic import quadratic_model
from .models.cubic import cubic_model
from .models.hyperbolic import hyperbolic_model
from .models.exponential import exponential_model
from .models.logarithmic import logarithmic_model
from .models.logistic import logistic_model
from .models.sinusoidal import sinusoidal_model
from .statistics.minimum import minimum_value
from .statistics.maximum import maximum_value
from .statistics.quartiles import quartile_value
from .statistics.mean import mean_value
from .statistics.median import median_value
from .vectors.dimension import single_dimension

def run_all(data, precision):
    matrix_of_scalars(data, 'first')
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    models = {
        'linear': linear_model(data, precision),
        'quadratic': quadratic_model(data, precision),
        'cubic': cubic_model(data, precision),
        'hyperbolic': hyperbolic_model(data, precision),
        'exponential': exponential_model(data, precision),
        'logarithmic': logarithmic_model(data, precision),
        'logistic': logistic_model(data, precision),
        'sinusoidal': sinusoidal_model(data, precision)
    }
    statistics = {
        'minimum': minimum_value(independent_variable),
        'maximum': maximum_value(independent_variable),
        'q1': quartile_value(independent_variable, 1),
        'q3': quartile_value(independent_variable, 3),
        'mean': mean_value(independent_variable),
        'median': median_value(independent_variable)
    }
    correlations = {
        'linear': models['linear']['correlation'],
        'quadratic': models['quadratic']['correlation'],
        'cubic': models['cubic']['correlation'],
        'hyperbolic': models['hyperbolic']['correlation'],
        'exponential': models['exponential']['correlation'],
        'logarithmic': models['logarithmic']['correlation'],
        'logistic': models['logistic']['correlation'],
        'sinusoidal': models['sinusoidal']['correlation']
    }
    best = max(correlations, key=correlations.get)
    optimal = {
        'option': best,
        'correlation': correlations[best]
    }
    result = {
        'models': models,
        'statistics': statistics,
        'optimal': optimal
    }
    return result
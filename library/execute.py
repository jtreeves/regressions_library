from .errors.matrices import matrix_of_scalars
from .errors.vectors import long_vector
from .errors.scalars import positive_integer
from .models.linear import linear_model
from .models.quadratic import quadratic_model
from .models.cubic import cubic_model
from .models.hyperbolic import hyperbolic_model
from .models.exponential import exponential_model
from .models.logarithmic import logarithmic_model
from .models.logistic import logistic_model
from .models.sinusoidal import sinusoidal_model
from .vectors.dimension import single_dimension
from .statistics.minimum import minimum_value
from .statistics.maximum import maximum_value
from .statistics.quartiles import quartile_value
from .statistics.mean import mean_value
from .statistics.median import median_value

def run_all(data, precision = 4):
    """
    Generates all eight key regression models (linear, quadratic, cubic, hyperbolic, exponential, logarithmic, logistic, and sinusoidal) for a given data set, in addition to determining the best fit based on correlation and providing various statistical measures

    Parameters
    ----------
    data : list of lists of int or float
        List of lists of numbers representing a collection of coordinate pairs
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain at least 10 elements
    ValueError
        Last argument must be a positive integer

    """
    # Handle input errors
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)

    # Grab values of independent variable
    independent_variable = single_dimension(data, 1)

    # Generate all eight key regression models
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

    # Determine key statistical values for independent variable
    statistics = {
        'minimum': minimum_value(independent_variable),
        'maximum': maximum_value(independent_variable),
        'q1': quartile_value(independent_variable, 1),
        'q3': quartile_value(independent_variable, 3),
        'mean': mean_value(independent_variable),
        'median': median_value(independent_variable)
    }

    # Grab correlations of all previously generated models
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

    # Determine model with highest correlation
    best = max(correlations, key=correlations.get)
    optimal = {
        'option': best,
        'correlation': correlations[best]
    }

    # Package preceding results in single dictionary to return
    result = {
        'models': models,
        'statistics': statistics,
        'optimal': optimal
    }
    return result
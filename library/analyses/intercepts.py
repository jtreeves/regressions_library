from .roots.linear import linear_roots
from .roots.quadratic import quadratic_roots
from .roots.cubic import cubic_roots
from .roots.hyperbolic import hyperbolic_roots
from .roots.exponential import exponential_roots
from .roots.logarithmic import logarithmic_roots
from .roots.logistic import logistic_roots
from .roots.sinusoidal import sinusoidal_roots

def intercept_points(equation_type, coefficients, precision):
    result = []
    if equation_type == 'linear':
        result = linear_roots(*coefficients, precision)
    elif equation_type == 'quadratic':
        result = quadratic_roots(*coefficients, precision)
    elif equation_type == 'cubic':
        result = cubic_roots(*coefficients, precision)
    elif equation_type == 'hyperbolic':
        result = hyperbolic_roots(*coefficients, precision)
    elif equation_type == 'exponential':
        result = exponential_roots(*coefficients, precision)
    elif equation_type == 'logarithmic':
        result = logarithmic_roots(*coefficients, precision)
    elif equation_type == 'logistic':
        result = logistic_roots(*coefficients, precision)
    elif equation_type == 'sinusoidal':
        result = sinusoidal_roots(*coefficients, precision)
    return result
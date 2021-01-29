from .roots.linear import linear
from .roots.quadratic import quadratic
from .roots.cubic import cubic
from .roots.hyperbolic import hyperbolic
from .roots.exponential import exponential
from .roots.logarithmic import logarithmic

def critical_points(equation_type, coefficients):
    results = []
    if equation_type == 'linear':
        results.append(linear(coefficients[0], coefficients[1]))
    elif equation_type == 'quadratic':
        results.append(quadratic(coefficients[0], coefficients[1], coefficients[2]))
    elif equation_type == 'cubic':
        results.append(cubic(coefficients[0], coefficients[1], coefficients[2], coefficients[3]))
    elif equation_type == 'hyperbolic':
        results.append(hyperbolic(coefficients[0], coefficients[1]))
    elif equation_type == 'exponential':
        results.append(exponential(coefficients[0], coefficients[1]))
    elif equation_type == 'logarithmic':
        results.append(logarithmic(coefficients[0], coefficients[1]))
    return results
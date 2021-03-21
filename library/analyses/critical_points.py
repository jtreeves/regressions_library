from .roots.linear import linear as linear_roots
from .roots.quadratic import quadratic as quadratic_roots
from .derivatives.quadratic import quadratic as quadratic_derivatives
from .derivatives.cubic import cubic as cubic_derivatives

def critical_points(equation_type, derivative_level, coefficients, precision):
    results = []
    if derivative_level == 1:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            constants = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
            results = quadratic_roots(constants[0], constants[1], constants[2], precision)
        elif equation_type == 'hyperbolic':
            results = [None]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
    elif derivative_level == 2:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            results = [None]
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'hyperbolic':
            results = [None]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
    return results
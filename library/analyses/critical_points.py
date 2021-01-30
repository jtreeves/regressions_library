from .roots.linear import linear as linroots
from .roots.quadratic import quadratic as quadroots
from .derivatives.quadratic import quadratic as quader
from .derivatives.cubic import cubic as cubder

def critical_points(equation_type, derivative_level, coefficients):
    results = []
    if derivative_level == 1:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            results = linroots(quader(coefficients[0], coefficients[1], coefficients[2])['first']['constants'])
        elif equation_type == 'cubic':
            results = quadroots(cubder(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants'])
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
            results = linroots(cubder(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants'])
        elif equation_type == 'hyperbolic':
            results = [None]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
    return results
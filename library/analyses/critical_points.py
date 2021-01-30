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
            constants = quader(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
            results = linroots(constants[0], constants[1])
        elif equation_type == 'cubic':
            constants = cubder(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
            results = quadroots(constants[0], constants[1], constants[2])
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
            constants = cubder(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
            results = linroots(constants[0], constants[1])
        elif equation_type == 'hyperbolic':
            results = [None]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
    return results
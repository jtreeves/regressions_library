from .roots.linear import linear as linroots
from .roots.quadratic import quadratic as quadroots
from .roots.cubic import cubic as cubroots
from .roots.hyperbolic import hyperbolic as hyproots
from .roots.exponential import exponential as exproots
from .roots.logarithmic import logarithmic as logroots
from .derivatives.linear import linear as linder
from .derivatives.quadratic import quadratic as quader
from .derivatives.cubic import cubic as cubder
from .derivatives.hyperbolic import hyperbolic as hypder
from .derivatives.exponential import exponential as expder
from .derivatives.logarithmic import logarithmic as logder

def critical_points(equation_type, derivative_level, coefficients):
    results = []
    if derivative_level == 1:
        if equation_type == 'linear':
            results.append(None)
        elif equation_type == 'quadratic':
            results.append(linroots(quader(coefficients[0], coefficients[1], coefficients[2])['first']['constants']))
        elif equation_type == 'cubic':
            results.append(quadroots())
        elif equation_type == 'hyperbolic':
            results.append(None)
        elif equation_type == 'exponential':
            results.append(exproots(coefficients[0], coefficients[1]))
        elif equation_type == 'logarithmic':
            results.append(hyproots(coefficients[0], coefficients[1]))
    elif derivative_level == 2:
        return
    return results
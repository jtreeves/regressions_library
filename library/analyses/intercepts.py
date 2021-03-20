from .roots.linear import linear as linear_roots
from .roots.quadratic import quadratic as quadratic_roots
from .roots.cubic import cubic as cubic_roots
from .roots.hyperbolic import hyperbolic as hyperbolic_roots
from .roots.exponential import exponential as exponential_roots
from .roots.logarithmic import logarithmic as logarithmic_roots

def intercepts(equation_type, coefficients):
    result = []
    if equation_type == 'linear':
        result = linear_roots(*coefficients)
    elif equation_type == 'quadratic':
        result = quadratic_roots(*coefficients)
    elif equation_type == 'cubic':
        result = cubic_roots(*coefficients)
    elif equation_type == 'hyperbolic':
        result = hyperbolic_roots(*coefficients)
    elif equation_type == 'exponential':
        result = exponential_roots(*coefficients)
    elif equation_type == 'logarithmic':
        result = logarithmic_roots(*coefficients)
    return result
from .equations.linear import linear
from .equations.quadratic import quadratic
from .equations.cubic import cubic
from .equations.hyperbolic import hyperbolic
from .equations.exponential import exponential
from .equations.logarithmic import logarithmic

def critical_values(equation_type, array):
    result = []
    if array[0] == None:
        result = [None]
    else:
        for i in range(len(array)):
            if equation_type == 'linear':
                result.append(linear(array[i]))
            elif equation_type == 'quadratic':
                result.append(quadratic(array[i]))
            elif equation_type == 'cubic':
                result.append(cubic(array[i]))
            elif equation_type == 'hyperbolic':
                result.append(hyperbolic(array[i]))
            elif equation_type == 'exponential':
                result.append(exponential(array[i]))
            elif equation_type == 'logarithmic':
                result.append(logarithmic(array[i]))
    return result
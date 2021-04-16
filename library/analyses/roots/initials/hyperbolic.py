from library.statistics.rounding import rounded_value
from library.analyses.roots.hyperbolic import hyperbolic_roots

def hyperbolic_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = hyperbolic_roots(first_constant, second_constant - initial_value, precision)
    return roots

def hyperbolic_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    root = []
    ratio = -1 * first_constant / initial_value
    if ratio < 0:
        root.append(None)
    else:
        radical = ratio**(1/2)
        rounded_radical = rounded_value(radical, precision)
        root.append(rounded_radical)
    return root
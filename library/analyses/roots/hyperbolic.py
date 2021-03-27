from library.statistics.rounding import rounded_value

def hyperbolic_roots(first_constant, second_constant, precision):
    root = -1 * first_constant / second_constant
    result = [rounded_value(root, precision)]
    return result
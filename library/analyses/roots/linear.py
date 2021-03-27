from library.statistics.rounding import rounded_value

def linear_roots(first_constant, second_constant, precision):
    root = -1 * second_constant / first_constant
    result = [rounded_value(root, precision)]
    return result
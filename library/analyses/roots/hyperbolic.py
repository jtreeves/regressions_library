from library.statistics.rounding import rounded_value
from library.errors.scalars import two_scalars

def hyperbolic_roots(first_constant, second_constant, precision):
    two_scalars(first_constant, second_constant)
    root = -1 * first_constant / second_constant
    result = [rounded_value(root, precision)]
    return result
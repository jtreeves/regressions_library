from math import exp
from library.errors.scalars import two_scalars, positive_integer
from library.statistics.rounding import rounded_value

def logarithmic_roots(first_constant, second_constant, precision):
    two_scalars(first_constant, second_constant)
    positive_integer
    root = exp(-1 * second_constant / first_constant)
    result = [rounded_value(root, precision)]
    return result
from math import exp
from library.statistics.rounding import rounded_value

def logarithmic_roots(first_constant, second_constant, precision):
    root = exp(-1 * second_constant / first_constant)
    result = [rounded_value(root, precision)]
    return result
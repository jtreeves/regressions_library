from math import exp
from library.statistics.rounding import rounding

def logarithmic(first_constant, second_constant, precision):
    root = exp(-1 * second_constant / first_constant)
    result = [rounding(root, precision)]
    return result
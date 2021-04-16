from math import log
from library.statistics.rounding import rounded_value

def exponential_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    denominator = log(abs(second_constant))
    if denominator == 0:
        denominator = 10**(-precision)
    numerator = log(abs(initial_value / first_constant))
    ratio = numerator / denominator
    rounded_ratio = rounded_value(ratio, precision)
    root = [rounded_ratio]
    return root

def exponential_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    denominator = log(abs(second_constant))
    if denominator == 0:
        denominator = 10**(-precision)
    roots = exponential_roots_initial_value(first_constant * denominator, second_constant, initial_value, precision)
    return roots
from math import log

def exponential_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = log(initial_value / first_constant) / log(second_constant)
    return roots

def exponential_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = exponential_roots_initial_value(first_constant * log(second_constant), second_constant, initial_value, precision)
    return roots
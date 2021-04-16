from math import log
from library.analyses.roots.quadratic import quadratic_roots

def logistic_roots_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    numerator = log(first_constant / initial_value - 1)
    denominator = second_constant
    ratio = numerator / denominator
    roots = third_constant - ratio
    return roots

def logistic_roots_derivative_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    intermediary_roots = quadratic_roots(initial_value, 2 * initial_value - first_constant * second_constant, initial_value, precision)
    final_roots = []
    for intermediary in intermediary_root:
        final_roots.append(third_constant - log(intermediary) / second_constant)
    return roots
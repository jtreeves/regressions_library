from math import log
from library.statistics.rounding import rounded_value
from library.statistics.sort import sorted_list
from library.analyses.roots.quadratic import quadratic_roots

def logistic_roots_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    log_argument = first_constant / initial_value - 1
    if log_argument == 0:
        log_argument = 10**(-precision)
    numerator = log(abs(log_argument))
    denominator = second_constant
    ratio = numerator / denominator
    root = third_constant - ratio
    rounded_root = rounded_value(root, precision)
    final_roots = [rounded_root]
    return final_roots

def logistic_roots_derivative_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    intermediary_roots = quadratic_roots(initial_value, 2 * initial_value - first_constant * second_constant, initial_value, precision)
    final_roots = []
    if intermediary_roots[0] == None:
        final_roots.append(None)
    else:
        for intermediary in intermediary_roots:
            if intermediary == 0:
                root = third_constant - log(10**(-precision)) / second_constant
                rounded_root = rounded_value(root, precision)
                final_roots.append(rounded_root)
            else:
                root = third_constant - log(abs(intermediary)) / second_constant
                rounded_root = rounded_value(root, precision)
                final_roots.append(rounded_root)
    sorted_roots = sorted_list(final_roots)
    return sorted_roots
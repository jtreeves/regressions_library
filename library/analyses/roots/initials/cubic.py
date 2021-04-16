from library.analyses.roots.cubic import cubic_roots
from library.analyses.roots.quadratic import quadratic_roots

def cubic_roots_initial_value(first_constant, second_constant, third_constant, fourth_constant, initial_value, precision = 4):
    roots = cubic_roots(first_constant, second_constant, third_constant, fourth_constant - initial_value, precision)
    return roots

def cubic_roots_derivative_initial_value(first_constant, second_constant, third_constant, fourth_constant, initial_value, precision = 4):
    roots = quadratic_roots(3 * first_constant, 2 * second_constant, third_constant - initial_value, precision)
    return roots
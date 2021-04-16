from library.analyses.roots.quadratic import quadratic_roots
from library.analyses.roots.linear import linear_roots

def quadratic_roots_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    roots = quadratic_roots(first_constant, second_constant, third_constant - initial_value, precision)
    return roots

def quadratic_roots_derivative_initial_value(first_constant, second_constant, third_constant, initial_value, precision = 4):
    roots = linear_roots(2 * first_constant, second_constant - initial_value, precision)
    return roots
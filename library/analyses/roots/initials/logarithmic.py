from library.analyses.roots.logarithmic import logarithmic_roots
from library.analyses.roots.hyperbolic import hyperbolic_roots

def logarithmic_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = logarithmic_roots(first_constant, second_constant - initial_value, precision)
    return roots

def logarithmic_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = hyperbolic_roots(first_constant, -1 * initial_value, precision)
    return roots
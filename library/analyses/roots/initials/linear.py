from library.analyses.roots.linear import linear_roots

def linear_roots_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = linear_roots(first_constant, second_constant - initial_value, precision)
    return roots

def linear_roots_derivative_initial_value(first_constant, second_constant, initial_value, precision = 4):
    roots = []
    if initial_value == first_constant:
        roots = ['All']
    else:
        roots = [None]
    return roots
from library.statistics.rounding import rounding

def hyperbolic(first_constant, second_constant, precision):
    root = [-1 * first_constant / second_constant]
    result = rounding(root, precision)
    return result
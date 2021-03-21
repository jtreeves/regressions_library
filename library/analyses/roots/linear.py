from library.statistics.rounding import rounding

def linear(first_constant, second_constant, precision):
    root = [-1 * second_constant / first_constant]
    result = rounding(root, precision)
    return result
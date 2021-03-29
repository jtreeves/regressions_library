from library.errors.scalars import three_scalars, positive_integer
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value

def quadratic_roots(first_constant, second_constant, third_constant, precision):
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    roots = []
    if first_constant == 0:
        first_constant = 10**(-precision)
    discriminant = second_constant**2 - 4 * first_constant * third_constant
    first_root = (-1 * second_constant + discriminant**(1/2)) / (2 * first_constant)
    second_root = (-1 * second_constant - discriminant**(1/2)) / (2 * first_constant)
    if first_root == second_root:
        roots.append(first_root)
    else:
        if not isinstance(first_root, complex):
            roots.append(first_root)
        if not isinstance(second_root, complex):
            roots.append(second_root)
    if not roots:
        roots = [None]
    sorted_roots = sorted_list(roots)
    result = []
    for number in sorted_roots:
        result.append(rounded_value(number, precision))
    return result
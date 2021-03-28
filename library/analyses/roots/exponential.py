from library.errors.scalars import two_scalars, positive_integer

def exponential_roots(first_constant, second_constant, precision):
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    root = [None]
    return root
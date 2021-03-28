from library.errors.scalars import three_scalars, positive_integer

def logistic_roots(first_constant, second_constant, third_constant, precision):
    three_scalars(first_constant, second_constant, third_constant)
    positive_integer(precision)
    root = [None]
    return root
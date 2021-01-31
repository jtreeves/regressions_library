def quadratic(first_constant, second_constant, third_constant):
    discriminant = second_constant**2 - 4 * first_constant * third_constant
    first_root = (-1 * second_constant + discriminant**(1/2)) / (2 * first_constant)
    second_root = (-1 * second_constant - discriminant**(1/2)) / (2 * first_constant)
    roots = [first_root, second_root]
    return roots
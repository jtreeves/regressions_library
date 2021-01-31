def quadratic(first_constant, second_constant, third_constant):
    roots = []
    discriminant = second_constant**2 - 4 * first_constant * third_constant
    first_root = (-1 * second_constant + discriminant**(1/2)) / (2 * first_constant)
    second_root = (-1 * second_constant - discriminant**(1/2)) / (2 * first_constant)
    if not isinstance(first_root, complex):
        roots.append(first_root)
    if not isinstance(second_root, complex):
        roots.append(second_root)
    return roots
def cubic(first_constant, second_constant, third_constant, fourth_constant):
    xi = (-1 + (-3)**(1/2)) / 2
    delta_first = second_constant**2 - 3 * first_constant * third_constant
    delta_second = 2 * second_constant**3 - 9 * first_constant * second_constant * third_constant + 27 * first_constant**2 * fourth_constant
    discriminant = delta_second**2 - 4 * delta_first**3
    zeta_first = ((delta_second + discriminant**(1/2)) / 2)**(1/3)
    zeta_second = ((delta_second - discriminant**(1/2)) / 2)**(1/3)
    zeta = 0
    if zeta_first == 0:
        zeta = zeta_second
    else:
        zeta = zeta_first
    first_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**0 + delta_first / (zeta * xi**0))
    second_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**1 + delta_first / (zeta * xi**1))
    third_root = (-1 / (3 * first_constant)) * (second_constant + zeta * xi**2 + delta_first / (zeta * xi**2))
    roots = [first_root, second_root, third_root]
    return roots
from math import asin, pi
from library.statistics.sort import sort
from library.statistics.rounding import rounding

def sinusoidal(first_constant, second_constant, third_constant, fourth_constant, precision):
    roots = []
    ratio = -1 * fourth_constant / first_constant
    if ratio > 1 or ratio < -1:
        roots = [None]
    else:
        radians = asin(ratio)
        periodic_radians = radians / second_constant
        if ratio == 0:
            periodic_unit = pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        elif ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / second_constant
            initial_value = third_constant + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
            alternative_initial_value = third_constant + pi / second_constant - periodic_radians
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            alternative_general_form = str(alternative_initial_value) + ' + ' + str(periodic_unit) + 'k'
            roots = [initial_value, first_value, second_value, alternative_initial_value, alternative_first_value, alternative_second_value, general_form, alternative_general_form]
    if not roots:
        roots = [None]
    sorted_roots = sort(roots)
    result = []
    for number in sorted_roots:
        try:
            result.append(rounding(number, precision))
        except TypeError:
            result.append(number)
    return result
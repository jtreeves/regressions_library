from math import acos, pi
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from library.analyses.roots.sinusoidal import sinusoidal_roots, sinusoidal_roots_first_derivative

def sinusoidal_roots_initial_value(first_constant, second_constant, third_constant, fourth_constant, initial_value, precision = 4):
    roots = sinusoidal_roots(first_constant, second_constant, third_constant, fourth_constant - initial_value, precision)
    return roots

def sinusoidal_roots_derivative_initial_value(first_constant, second_constant, third_constant, fourth_constant, initial_value, precision = 4):
    ratio = initial_value / (first_constant * second_constant)
    roots = []
    if ratio == 0:
        roots = sinusoidal_roots_first_derivative(first_constant, second_constant, third_constant, fourth_constant, precision)
    else:
        radians = acos(ratio)
        periodic_radians = radians / second_constant
        periodic_unit = 2 * pi / second_constant
        initial = third_constant + periodic_radians
        first_value = initial + 1 * periodic_unit
        second_value = initial + 2 * periodic_unit
        rounded_periodic_unit = rounded_value(periodic_unit, precision)
        rounded_initial = rounded_value(initial, precision)
        general_form = str(rounded_initial) + ' + ' + str(rounded_periodic_unit) + 'k'
        roots = [initial, first_value, second_value, general_form]
        if ratio == 1 or ratio == -1:
            pass
        else:
            alternative_initial = third_constant + periodic_unit - periodic_radians
            alternative_first_value = alternative_initial + 1 * periodic_unit
            alternative_second_value = alternative_initial + 2 * periodic_unit
            rounded_alternative_initial = rounded_value(alternative_initial, precision)
            alternative_general_form = str(rounded_alternative_initial) + ' + ' + str(rounded_periodic_unit) + 'k'
            roots.extend([alternative_initial, alternative_first_value, alternative_second_value, alternative_general_form])
    
    # Separate numerical roots, string roots, and None results
    numerical_roots = []
    other_roots = []
    for item in roots:
        if isinstance(item, (int, float)):
            numerical_roots.append(item)
        else:
            other_roots.append(item)
    
    # Sort numerical roots
    sorted_roots = sorted_list(numerical_roots)

    # Round numerical roots
    rounded_roots = []
    for number in sorted_roots:
        rounded_roots.append(rounded_value(number, precision))
    
    # Sort other_roots
    sorted_other_roots = []
    if len(other_roots) == 1:
        sorted_other_roots = other_roots
    else:
        first_index = other_roots[0].find(' + ') - 1
        first_value = float(other_roots[0][:first_index])
        second_index = other_roots[1].find(' + ') - 1
        second_value = float(other_roots[1][:second_index])
        if first_value < second_value:
            sorted_other_roots = other_roots
        else:
            sorted_other_roots = [other_roots[1], other_roots[0]]

    # Combine numerical and non-numerical roots
    final_roots = rounded_roots + sorted_other_roots
    return final_roots
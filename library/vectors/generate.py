from library.errors.scalars import two_scalars, positive_integer
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value, rounded_list

def generate_elements(initial_value, periodic_unit, precision = 4):
    two_scalars(initial_value, periodic_unit)
    positive_integer(precision)
    first_value = initial_value + 1 * periodic_unit
    second_value = initial_value + 2 * periodic_unit
    third_value = initial_value + 3 * periodic_unit
    fourth_value = initial_value + 4 * periodic_unit
    values = [initial_value, first_value, second_value, third_value, fourth_value]
    sorted_values = sorted_list(values)
    rounded_values = rounded_list(sorted_values, precision)
    rounded_periodic_unit = rounded_value(periodic_unit, precision)
    rounded_initial_value = rounded_value(initial_value, precision)
    general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
    results = [*rounded_values, general_form]
    return results
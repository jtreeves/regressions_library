from math import pi
from library.statistics.rounding import rounding
from library.statistics.sort import sort
from .roots.linear import linear as linear_roots
from .roots.quadratic import quadratic as quadratic_roots
from .derivatives.quadratic import quadratic as quadratic_derivatives
from .derivatives.cubic import cubic as cubic_derivatives

def critical_points(equation_type, derivative_level, coefficients, precision):
    results = []
    if derivative_level == 1:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            constants = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
            results = quadratic_roots(constants[0], constants[1], constants[2], precision)
        elif equation_type == 'hyperbolic':
            results = [0]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
        elif equation_type == 'logistic':
            results = [None]
        elif equation_type == 'sinusoidal':
            periodic_unit = pi / coefficients[1]
            initial_value = coefficients[2] + pi / (2 * coefficients[1])
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            values = [initial_value, first_value, second_value, third_value, fourth_value]
            sorted_values = sort(values)
            rounded_values = []
            for number in sorted_values:
                rounded_values.append(rounding(number, precision))
            rounded_periodic_unit = rounding(periodic_unit, precision)
            rounded_initial_value = rounding(initial_value, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            results = [*rounded_values, general_form]
    elif derivative_level == 2:
        if equation_type == 'linear':
            results = [None]
        elif equation_type == 'quadratic':
            results = [None]
        elif equation_type == 'cubic':
            constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
            results = linear_roots(constants[0], constants[1], precision)
        elif equation_type == 'hyperbolic':
            results = [0]
        elif equation_type == 'exponential':
            results = [None]
        elif equation_type == 'logarithmic':
            results = [None]
        elif equation_type == 'logistic':
            results = [rounding(coefficients[2], precision)]
        elif equation_type == 'sinusoidal':
            periodic_unit = pi / coefficients[1]
            initial_value = coefficients[2]
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            values = [initial_value, first_value, second_value, third_value, fourth_value]
            sorted_values = sort(values)
            rounded_values = []
            for number in sorted_values:
                rounded_values.append(rounding(number, precision))
            rounded_periodic_unit = rounding(periodic_unit, precision)
            rounded_initial_value = rounding(initial_value, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            results = [*rounded_values, general_form]
    return results
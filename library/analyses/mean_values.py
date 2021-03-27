from math import log, exp, acos, pi
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from .roots.linear import linear_roots
from .roots.quadratic import quadratic_roots
from .roots.cubic import cubic_roots
from .roots.hyperbolic import hyperbolic_roots
from .roots.logarithmic import logarithmic_roots
from .roots.sinusoidal import sinusoidal_roots
from .accumulation import accumulated_area

def average_value_derivative(equation, start, end, precision):
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    ratio = vertical_change / horizontal_change
    result = rounded_value(ratio, precision)
    return result

def mean_values_derivative(equation_type, equation, start, end, constants, precision):
    result = []
    average = average_value_derivative(equation, start, end, precision)
    if equation_type == 'linear':
        result.append('All')
        return result
    elif equation_type == 'quadratic':
        value = linear_roots(2 * constants[0], constants[1] -  average, precision)
        result = value
    elif equation_type == 'cubic':
        values = quadratic_roots(3 * constants[0], 2 * constants[1], constants[2] - average, precision)
        result = values
    elif equation_type == 'hyperbolic':
        ratio = -1 * constants[0] / average
        root = ratio ** (1/2)
        first_value = root
        second_value = -1 * root
        result.extend([first_value, second_value])
    elif equation_type == 'exponential':
        base_log = log(constants[1])
        numerator = log(average / (constants[0] * base_log))
        denominator = base_log
        value = numerator / denominator
        result.append(value)
    elif equation_type == 'logarithmic':
        value = hyperbolic_roots(constants[0], -1 * average, precision)
        result = value
    elif equation_type == 'logistic':
        quadratic_values = quadratic_roots(average, 2 * average - constants[0] * constants[1], average, precision)
        if quadratic_values[0] == None:
            result = [None]
            return result
        else:
            values = []
            for i in range(len(quadratic_values)):
                if quadratic_values[i] <= 0:
                    values.append(constants[2] - log(10**(-precision)) / constants[1])
                else:
                    values.append(constants[2] - log(quadratic_values[i]) / constants[1])
            result = values
    elif equation_type == 'sinusoidal':
        ratio = average / (constants[0] * constants[1])
        radians = acos(ratio)
        periodic_radians = radians / constants[1]
        if ratio == 0:
            periodic_unit = pi / constants[1]
            initial_value = constants[2] + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        elif ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / constants[1]
            initial_value = constants[2] + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / constants[1]
            initial_value = constants[2] + periodic_radians
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            alternative_initial_value = constants[2] + pi / constants[1] - periodic_radians
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            rounded_alternative_initial_value = rounded_value(alternative_initial_value, precision)
            alternative_general_form = str(rounded_alternative_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, alternative_initial_value, alternative_first_value, alternative_second_value, general_form, alternative_general_form]
    if not result:
        result = [None]
        return result
    numerical_results = []
    other_results = []
    for item in result:
        if isinstance(item, (int, float)):
            numerical_results.append(item)
        else:
            other_results.append(item)
    selected_results = [x for x in numerical_results if x > start and x < end]
    if not selected_results:
        final = [None]
        return final
    sorted_results = sorted_list(selected_results)
    rounded_results = []
    for number in sorted_results:
        rounded_results.append(rounded_value(number, precision))
    final_result = rounded_results + other_results
    return final_result

def average_value_integral(equation, start, end, precision):
    accumulated_value = accumulated_area(equation, start, end, precision)
    change = end - start
    ratio = accumulated_value / change
    result = rounded_value(ratio, precision)
    return result

def mean_values_integral(equation_type, equation, start, end, constants, precision):
    result = []
    average = average_value_integral(equation, start, end, precision)
    if equation_type == 'linear':
        value = linear_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'quadratic':
        values = quadratic_roots(constants[0], constants[1], constants[2] - average, precision)
        result = values
    elif equation_type == 'cubic':
        values = cubic_roots(constants[0], constants[1], constants[2], constants[3] - average, precision)
        result = values
    elif equation_type == 'hyperbolic':
        value = hyperbolic_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'exponential':
        value = log(average / constants[0]) / log(constants[1])
        result.append(value)
    elif equation_type == 'logarithmic':
        value = logarithmic_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'logistic':
        ratio = constants[0] / average
        if ratio <= 1:
            pass
        else:
            value = constants[2] - log(ratio - 1) / constants[1]
            result.append(value)
    elif equation_type == 'sinusoidal':
        values = sinusoidal_roots(constants[0], constants[1], constants[2], constants[3] - average, precision)
        result = values
    if not result:
        result = [None]
        return result
    numerical_results = []
    other_results = []
    for item in result:
        if isinstance(item, (int, float)):
            numerical_results.append(item)
        else:
            other_results.append(item)
    selected_results = [x for x in numerical_results if x > start and x < end]
    if not selected_results:
        final = [None]
        return final
    sorted_results = sorted_list(selected_results)
    rounded_results = []
    for number in sorted_results:
        rounded_results.append(rounded_value(number, precision))
    final_result = rounded_results + other_results
    return final_result

def average_values(equation_type, equation, integral, start, end, constants, precision):
    derivative_value = average_value_derivative(equation, start, end, precision)
    derivative_inputs = mean_values_derivative(equation_type, equation, start, end, constants, precision)
    integral_value = average_value_integral(integral, start, end, precision)
    integral_inputs = mean_values_integral(equation_type, integral, start, end, constants, precision)
    results = {
        'average_value_derivative': derivative_value,
        'mean_values_derivative': derivative_inputs,
        'average_value_integral': integral_value,
        'mean_values_integral': integral_inputs
    }
    return results
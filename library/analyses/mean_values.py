from math import log, exp
from library.statistics.sort import sort
from library.statistics.rounding import rounding
from .roots.linear import linear as linear_roots
from .roots.quadratic import quadratic as quadratic_roots
from .roots.cubic import cubic as cubic_roots
from .roots.hyperbolic import hyperbolic as hyperbolic_roots
from .roots.logarithmic import logarithmic as logarithmic_roots
from .accumulation import accumulation

def average_value_derivative(equation, start, end, precision):
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    ratio = vertical_change / horizontal_change
    result = rounding(ratio, precision)
    return result

def mean_values_derivative(equation_type, equation, start, end, constants, precision):
    result = []
    average = average_value_derivative(equation, start, end)
    if equation_type == 'linear':
        result.append('All')
        return result
    elif equation_type == 'quadratic':
        value = linear_roots(2 * constants[0], constants[1] -  average)
        result = value
    elif equation_type == 'cubic':
        values = quadratic_roots(3 * constants[0], 2 * constants[1], constants[2] - average)
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
        value = hyperbolic_roots(constants[0], -1 * average)
        result = value
    selected = [x for x in result if x > start and x < end]
    if not selected:
        selected = [None]
    sorted_selected = sort(selected)
    final = []
    for number in sorted_selected:
        result.append(rounding(number, precision))
    return final

def average_value_integral(equation, start, end, precision):
    accumulated_value = accumulation(equation, start, end)
    change = end - start
    ratio = accumulated_value / change
    result = rounding(ratio, precision)
    return result

def mean_values_integral(equation_type, equation, start, end, constants, precision):
    result = []
    average = average_value_integral(equation, start, end)
    if equation_type == 'linear':
        value = linear_roots(constants[0], constants[1] - average)
        result = value
    elif equation_type == 'quadratic':
        values = quadratic_roots(constants[0], constants[1], constants[2] - average)
        result = values
    elif equation_type == 'cubic':
        values = cubic_roots(constants[0], constants[1], constants[2], constants[3] - average)
        result = values
    elif equation_type == 'hyperbolic':
        value = hyperbolic_roots(constants[0], constants[1] - average)
        result = value
    elif equation_type == 'exponential':
        value = log(average / constants[0]) / log(constants[1])
        result.append(value)
    elif equation_type == 'logarithmic':
        value = logarithmic_roots(constants[0], constants[1] - average)
        result = value
    selected = [x for x in result if x > start and x < end]
    if not selected:
        selected = [None]
    sorted_selected = sort(selected)
    final = []
    for number in sorted_selected:
        result.append(rounding(number, precision))
    return final

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
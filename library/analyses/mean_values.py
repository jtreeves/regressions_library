from .accumulation import accumulation
from .roots.linear import linear as linear_roots
from .roots.quadratic import quadratic as quadratic_roots
from .roots.cubic import cubic as cubic_roots
from .roots.hyperbolic import hyperbolic as hyperbolic_roots
from .roots.logarithmic import logarithmic as logarithmic_roots
from math import log, exp

def average_value_derivative(equation, start, end):
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    result = vertical_change / horizontal_change
    return result

def mean_values_derivative(equation_type, equation, start, end, constants):
    result = []
    average = average_value_derivative(equation, start, end)
    if equation_type == 'linear':
        result.append(None)
    elif equation_type == 'quadratic':
        value = linear_roots(2 * constants[0], constants[1] -  average)
        result = value
    elif equation_type == 'cubic':
        values = quadratic_roots(3 * constants[0], 2 * constants[1], constants[2] - average)
        result = values
    elif equation_type == 'hyperbolic':
        ratio = -1 * average / constants[0]
        root = ratio ** (1/2)
        first_value = root
        second_value = -1 * root
        result.extend([first_value, second_value])
    elif equation_type == 'exponential':
        average_log = log(average)
        first_log = log(constants[0])
        second_log = log(constants[1])
        numerator = average_log - first_log - log(second_log)
        denominator = second_log
        value = numerator / denominator
        result.append(value)
    elif equation_type == 'logarithmic':
        value = hyperbolic_roots(constants[1], -1 * average)
        result = value
    print(f'AVERAGE VALUES LIST: {result}')
    for i in range(len(result)):
        if isinstance(result[i], complex):
            result.remove(result[i])
        elif result[i] is not None and (result[i] <= start or result[i] >= end):
            result.remove(result[i])
        else:
            pass
    if len(result) == 0:
        result.append(None)
    return result

def average_value_integral(equation, start, end):
    accumulated_value = accumulation(equation, start, end)
    change = end - start
    result = accumulated_value / change
    return result

def mean_values_integral(equation_type, equation, start, end, constants):
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
        value = logarithmic_roots(constants[0] - average, constants[1])
        result = value
    for i in range(len(result)):
        if isinstance(result[i], complex):
            result.remove(result[i])
        elif result[i] is not None and (result[i] < start or result[i] > end):
            result.remove(result[i])
        else:
            pass
    if len(result) == 0:
        result.append(None)
    return result

def average_values(equation_type, equation, integral, start, end, constants):
    derivative_value = average_value_derivative(equation, start, end)
    derivative_inputs = mean_values_derivative(equation_type, equation, start, end, constants)
    integral_value = average_value_integral(integral, start, end)
    integral_inputs = mean_values_integral(equation_type, integral, start, end, constants)
    results = {
        'average_value_derivative': derivative_value,
        'mean_values_derivative': derivative_inputs,
        'average_value_integral': integral_value,
        'mean_values_integral': integral_inputs
    }
    return results
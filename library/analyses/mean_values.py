from .accumulation import accumulation
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
        value = (average - constants[1]) / constants[0]
        result.append(value)
    elif equation_type == 'cubic':
        discriminant = constants[1]**2 - 4 * constants[0] * (constants[2] - average)
        first_value = (-1 * constants[1] + discriminant**(1/2)) / (2 * constants[0])
        second_value = (-1 * constants[1] - discriminant**(1/2)) / (2 * constants[0])
        result.extend(first_value, second_value)
    elif equation_type == 'hyperbolic':
        first_value = (constants[0] / average)**(1/2)
        second_value = -1 * (constants[0] / average)**(1/2)
        result.extend(first_value, second_value)
    elif equation_type == 'exponential':
        value = log(average / constants[0]) / log(constants[1])
        result.append(value)
    elif equation_type == 'logarithmic':
        value = constants[0] / average
        result.append(value)
    for i in range(len(result)):
        if result[i] <= start or result[i] >= end:
            result.pop([i])
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
        value = (average - constants[1]) / constants[0]
        result.append(value)
    elif equation_type == 'quadratic':
        discriminant = constants[1]**2 - 4 * constants[0] * (constants[2] - average)
        first_value = (-1 * constants[1] + discriminant**(1/2)) / (2 * constants[0])
        second_value = (-1 * constants[1] - discriminant**(1/2)) / (2 * constants[0])
        result.extend(first_value, second_value)
    elif equation_type == 'cubic':
        result.append(None)
    elif equation_type == 'hyperbolic':
        value = constants[0] / (average - constants[1])
        result.append(value)
    elif equation_type == 'exponential':
        value = log(average / constants[0]) / log(constants[1])
        result.append(value)
    elif equation_type == 'logarithmic':
        value = exp((average - constants[0]) / constants[1])
        result.append(value)
    for i in range(len(result)):
        if result[i] < start or result[i] > end:
            result.pop([i])
    if len(result) == 0:
        result.append(None)
    return result
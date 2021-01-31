from .accumulation import accumulation

def average_value_derivative(equation, derivative, start, end):
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    result = vertical_change / horizontal_change
    return result

def average_value_integral(equation, integral, start, end):
    accumulated_value = accumulation(integral, start, end)
    change = end - start
    result = accumulated_value / change
    return result
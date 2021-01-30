from .accumulation import accumulation

def mean_value_derivative(equation, derivative, start, end):
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    average_slope = vertical_change / horizontal_change
    return average_slope

def mean_value_integral(equation, integral, start, end):
    accumulated_value = accumulation(integral, start, end)
    change = end - start
    average_value = accumulated_value / change
    return average_value
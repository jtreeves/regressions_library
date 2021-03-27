from .addition import vector_sum
from .multiplication import scalar_product

def component_form(initial_point, terminal_point):
    if not isinstance(initial_point, (list, tuple)) or not isinstance(terminal_point, (list, tuple)) or isinstance(initial_point[0], (list, tuple)) or isinstance(terminal_point[0], (list, tuple)):
        raise TypeError("Both arguments must be 1-dimensional lists or tuples")
    if not isinstance(initial_point[0], (int, float)) or not isinstance(terminal_point[0], (int, float)):
        raise TypeError("Elements of arguments must be integers or floats")
    if len(initial_point) is not len(terminal_point):
        raise ValueError("Both arguments must contain the same number of elements")
    result = vector_sum(terminal_point, scalar_product(initial_point, -1))
    return result
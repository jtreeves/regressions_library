from .addition import addition
from .scalar import scalar

def component_form(initial_point, terminal_point):
    result = addition(terminal_point, scalar(initial_point, -1))
    return result
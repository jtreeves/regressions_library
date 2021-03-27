from .addition import vector_sum
from .multiplication import scalar_product

def component_form(initial_point, terminal_point):
    result = vector_sum(terminal_point, scalar_product(initial_point, -1))
    return result
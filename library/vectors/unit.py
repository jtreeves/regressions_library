from .magnitude import vector_magnitude
from .multiplication import scalar_product

def unit_vector(vector):
    magnitude = vector_magnitude(vector)
    reciprocal_magnitude = 1 / magnitude
    result = scalar_product(vector, reciprocal_magnitude)
    return result
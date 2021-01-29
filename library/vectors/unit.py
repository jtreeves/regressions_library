from .magnitude import magnitude
from .scalar import scalar

def unit(vector):
    vector_magnitude = magnitude(vector)
    reciprocal_magnitude = 1 / vector_magnitude
    result = scalar(vector, reciprocal_magnitude)
    return result
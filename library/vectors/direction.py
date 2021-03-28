from math import atan, degrees
from library.errors.vectors import first_vector, length

def vector_direction(vector):
    first_vector(vector)
    length(vector, 2)
    ratio = vector[1] / vector[0]
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result
from math import atan, degrees
from .check import check_one, check_length

def vector_direction(vector):
    check_one(vector)
    check_length(vector, 2)
    ratio = vector[1] / vector[0]
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result
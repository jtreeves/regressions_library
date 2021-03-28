from math import atan, degrees
from library.errors.vectors import vector_of_scalars, length

def vector_direction(vector):
    vector_of_scalars(vector, 'only')
    length(vector, 2)
    ratio = vector[1] / vector[0]
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result
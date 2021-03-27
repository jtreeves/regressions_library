from math import atan, degrees

def vector_direction(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("Argument must be a 1-dimensional list or tuple")
    if not len(vector) == 2:
        raise ValueError("Argument must contain exactly two elements")
    if not isinstance(vector[0], (int, float)) or not isinstance(vector[1], (int, float)):
        raise TypeError("Elements of argument must be integers or floats")
    ratio = vector[1] / vector[0]
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result
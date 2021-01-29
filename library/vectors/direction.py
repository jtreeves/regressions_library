from math import atan, degrees

def direction(initial, terminal):
    vertical_change = terminal[1] - initial[1]
    horizontal_change = terminal[0] - initial[0]
    ratio = vertical_change / horizontal_change
    radian_measure = atan(ratio)
    degree_measure = degrees(radian_measure)
    result = {
        'radian': radian_measure,
        'degree': degree_measure
    }
    return result
from .criticals import critical_points
from .intervals import sign_chart

def inflection_points(equation_type, coefficients, derivative, precision):
    points = critical_points(equation_type, 2, coefficients, precision)
    intervals_set = sign_chart(derivative, points)
    result = []
    for i in range(len(intervals_set)):
        try:
            if (intervals_set[i] == 'positive' and intervals_set[i + 2] == 'negative') or (intervals_set[i] == 'negative' and intervals_set[i + 2] == 'positive'):
                try:
                    derivative(intervals_set[i + 1])
                    result.append(intervals_set[i + 1])
                except ZeroDivisionError:
                    break
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    if equation_type == 'sinusoidal':
        result.append(points[-1])
    return result
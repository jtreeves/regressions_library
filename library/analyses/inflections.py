from .critical_points import critical_points
from .intervals import intervals

def inflections(equation_type, coefficients, derivative, precision):
    points = critical_points(equation_type, 2, coefficients, precision)
    intervals_set = intervals(derivative, points)
    result = []
    for i in range(len(intervals_set)):
        try:
            if (intervals_set[i] == 'positive' and intervals_set[i + 2] == 'negative') or (intervals_set[i] == 'negative' and intervals_set[i + 2] == 'positive'):
                result.append(intervals_set[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result
from .critical_points import critical_points
from .intervals import intervals

def inflections(equation_type, coefficients, derivative):
    points = critical_points(equation_type, 2, coefficients)
    intervals_set = intervals(derivative, points)
    result = []
    for i in range(len(intervals_set)):
        try:
            if (intervals_set[i] == 'increasing' and intervals_set[i + 2] == 'decreasing') or (intervals_set[i] == 'decreasing' and intervals_set[i + 2] == 'increasing'):
                result.append(intervals_set[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result
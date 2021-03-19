from .critical_points import critical_points
from .intervals import intervals
from .maxima import maxima
from .minima import minima

def extrema(equation_type, coefficients, derivative):
    points = critical_points(equation_type, 1, coefficients)
    intervals_set = intervals(derivative, points)
    max_points = maxima(intervals_set)
    min_points = minima(intervals_set)
    result = {
        'maxima': max_points,
        'minima': min_points
    }
    return result
from .maxima import maxima
from .minima import minima

def extrema(intervals):
    max_points = maxima(intervals)
    min_points = minima(intervals)
    result = {
        'maxima': max_points,
        'minima': min_points
    }
    return result
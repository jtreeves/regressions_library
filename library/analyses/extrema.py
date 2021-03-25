from .critical_points import critical_points
from .intervals import intervals
from .maxima import maxima
from .minima import minima

def extrema(equation_type, coefficients, derivative, precision):
    points = critical_points(equation_type, 1, coefficients, precision)
    intervals_set = intervals(derivative, points)
    result = {}
    if equation_type == 'sinusoidal':
        general_form = intervals_set[-1]
        periodic_unit_index = general_form.find(' + ') + 3
        periodic_unit = general_form[periodic_unit_index:]
        max_points = maxima(intervals_set)
        min_points = minima(intervals_set)
        max_extended = max_points + [periodic_unit]
        min_extended = min_points + [periodic_unit]
        result = {
            'maxima': max_extended,
            'minima': min_extended
        }
    else:
        max_points = maxima(intervals_set)
        min_points = minima(intervals_set)
        result = {
            'maxima': max_points,
            'minima': min_points
        }
    return result
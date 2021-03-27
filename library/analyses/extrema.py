from .criticals import critical_points
from .intervals import sign_chart
from .maxima import maxima_points
from .minima import minima_points

def extrema_points(equation_type, coefficients, derivative, precision):
    points = critical_points(equation_type, 1, coefficients, precision)
    intervals_set = sign_chart(derivative, points)
    result = {}
    if equation_type == 'sinusoidal':
        general_form = intervals_set[-1]
        periodic_unit_index = general_form.find(' + ') + 3
        periodic_unit = general_form[periodic_unit_index:]
        max_points = maxima_points(intervals_set)
        min_points = minima_points(intervals_set)
        max_extended = max_points + [periodic_unit]
        min_extended = min_points + [periodic_unit]
        result = {
            'maxima': max_extended,
            'minima': min_extended
        }
    else:
        max_points = maxima_points(intervals_set)
        min_points = minima_points(intervals_set)
        result = {
            'maxima': max_points,
            'minima': min_points
        }
    return result
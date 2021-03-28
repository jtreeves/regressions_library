from library.statistics.rounding import rounded_value
from library.errors.analyses import callable_function
from library.errors.scalars import compare_scalars

def accumulated_area(integral, start, end, precision):
    callable_function(integral)
    compare_scalars(start, end)
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result
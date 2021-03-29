from library.errors.scalars import compare_scalars, positive_integer
from library.errors.analyses import callable_function
from library.statistics.rounding import rounded_value

def accumulated_area(integral, start, end, precision):
    callable_function(integral, 'first')
    compare_scalars(start, end, 'second', 'third')
    positive_integer(precision)
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result
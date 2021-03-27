from library.statistics.rounding import rounded_value

def accumulated_area(integral, start, end, precision):
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result
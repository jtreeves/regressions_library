from library.statistics.rounding import rounding

def accumulation(integral, start, end, precision):
    area = integral(end) - integral(start)
    result = rounding(area, precision)
    return result
def accumulation(integral, start, end):
    result = integral(end) - integral(start)
    return result
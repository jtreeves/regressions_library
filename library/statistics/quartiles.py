from .median import median
from .halve import halve

def quartiles(data, q):
    halved_data = halve(data)
    result = ''
    if q == 2:
        result = median(data)
    elif q == 1:
        result = median(halved_data['lower'])
    elif q == 3:
        result = median(halved_data['upper'])
    return result
from library.errors.scalars import integer
from .median import median_value
from .halve import half

def quartile_value(data, q):
    integer(q)
    halved_data = half(data)
    result = ''
    if q == 2:
        result = median_value(data)
    elif q == 1:
        result = median_value(halved_data['lower'])
    elif q == 3:
        result = median_value(halved_data['upper'])
    else:
        raise ValueError('Second argument must be either 1, 2, or 3')
    return result
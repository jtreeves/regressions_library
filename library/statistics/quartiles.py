from library.errors.vectors import vector_of_scalars
from library.errors.scalars import select_integers
from .median import median_value
from .halve import half

def quartile_value(data, q):
    vector_of_scalars(data, 'first')
    select_integers(q, [1, 2, 3])
    halved_data = half(data)
    result = ''
    if q == 2:
        result = median_value(data)
    elif q == 1:
        result = median_value(halved_data['lower'])
    elif q == 3:
        result = median_value(halved_data['upper'])
    return result
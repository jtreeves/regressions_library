from math import floor
from .median import median
from .sort import sort

def halve(data):
    sorted_data = sort(data)
    length = len(sorted_data)
    upper = []
    lower = []
    if length % 2 == 0:
        index = int(length / 2)
        upper = sorted_data[index:]
        lower = sorted_data[:index]
    else:
        index = int(floor(length / 2))
        upper = sorted_data[index + 1:]
        lower = sorted_data[:index]
    result = {
        'upper': upper,
        'lower': lower
    }
    return result

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
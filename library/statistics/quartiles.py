from .median import median
from .sort import sort
from math import floor

def halve(data):
    sorted_data = sort(data)
    length = len(sorted_data)
    upper = []
    lower = []
    if length % 2 == 0:
        upper_index = int(length / 2)
        lower_index = int(upper_index - 1)
        upper = data[upper_index:]
        lower = data[:lower_index]
    else:
        index = int(floor(length / 2))
        upper = data[index:]
        lower = data[:index]
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
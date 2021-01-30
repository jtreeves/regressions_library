from .sort import sort
from math import floor

def median(data):
    sorted_data = sort(data)
    length = len(sorted_data)
    if length % 2 == 0:
        upper_index = int(length / 2)
        lower_index = int(upper_index - 1)
        upper_value = sorted_data[upper_index]
        lower_value = sorted_data[lower_index]
        result = (upper_value + lower_value) / 2
        return result
    else:
        index = int(floor(length / 2))
        result = sorted_data[index]
        return result
from math import floor
from .sort import sorted_list, sorted_dimension

def partition(data):
    length = len(data)
    upper = []
    lower = []
    if length % 2 == 0:
        index = int(length / 2)
        upper = data[index:]
        lower = data[:index]
    else:
        index = int(floor(length / 2))
        upper = data[index + 1:]
        lower = data[:index]
    result = {
        'upper': upper,
        'lower': lower
    }
    return result

def half(data):
    sorted_data = sorted_list(data)
    result = partition(sorted_data)
    return result

def half_dimension(data, dimension):
    sorted_data = sorted_dimension(data, dimension)
    result = partition(sorted_data)
    return result
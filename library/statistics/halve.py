from math import floor
from .sort import sort, sort_dimension

def partitioning(data):
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

def halve(data):
    sorted_data = sort(data)
    result = partitioning(sorted_data)
    return result

def halve_dimension(data, dimension):
    sorted_data = sort_dimension(data, dimension)
    result = partitioning(sorted_data)
    return result
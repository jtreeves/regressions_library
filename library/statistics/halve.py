from math import floor
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from library.errors.matrices import matrix_of_scalars
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
    vector_of_scalars(data, 'only')
    sorted_data = sorted_list(data)
    result = partition(sorted_data)
    return result

def half_dimension(data, dimension):
    matrix_of_scalars(data, 'first')
    positive_integer(dimension)
    sorted_data = sorted_dimension(data, dimension)
    result = partition(sorted_data)
    return result
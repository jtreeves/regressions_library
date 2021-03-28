from library.errors.vectors import vector_of_scalars
from .summation import sum_value

def mean_value(data):
    vector_of_scalars(data, 'only')
    result = sum_value(data) / len(data)
    return result
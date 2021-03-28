from library.errors.vectors import vector_of_scalars
from .sort import sorted_list

def maximum_value(data):
    vector_of_scalars(data, 'only')
    sorted_data = sorted_list(data)
    result = sorted_data[-1]
    return result
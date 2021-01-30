from .sort import sort
from math import floor

def median(data):
    sorted_data = sort(data)
    print(f'SORTED_DATA: {sorted_data}')
    length = len(sorted_data)
    print(f'LENGTH: {length}')
    if length % 2 == 0:
        upper_index = length / 2
        print(f'UPPER_INDEX: {upper_index}')
        lower_index = upper_index - 1
        print(f'LOWER_INDEX: {lower_index}')
        upper_value = sorted_data(upper_index)
        print(f'UPPER_VALUE: {upper_value}')
        lower_value = sorted_data(lower_index)
        print(f'LOWER_VALUE: {lower_value}')
        result = (upper_value + lower_value) / 2
        return result
    else:
        index = floor(length / 2)
        result = sorted_data(index)
        return result
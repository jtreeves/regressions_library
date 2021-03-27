from .sort import sorted_list

def maximum_value(data):
    sorted_data = sorted_list(data)
    result = sorted_data[-1]
    return result
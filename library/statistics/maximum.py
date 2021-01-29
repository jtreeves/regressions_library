from .sort import sort

def maximum(data):
    sorted_data = sort(data)
    result = sorted_data[-1]
    return result
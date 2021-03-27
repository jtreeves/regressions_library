from .summation import sum_value

def mean_value(data):
    result = sum_value(data) / len(data)
    return result
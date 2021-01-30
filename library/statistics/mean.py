from .summation import summation

def mean(data):
    result = summation(data) / len(data)
    return result
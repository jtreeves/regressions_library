from library.statistics.summation import sum_value

def vector_magnitude(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("Argument must be a 1-dimensional list or tuple")
    if not isinstance(vector[0], (int, float)):
        raise TypeError("Elements of argument must be integers or floats")
    squares = []
    for i in range(len(vector)):
        squares.append(vector[i]**2)
    sum_squares = sum_value(squares)
    result = sum_squares**(1/2)
    return result
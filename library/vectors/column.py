def column_conversion(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("Argument must be a 1-dimensional list or tuple")
    if not isinstance(vector[0], (int, float)):
        raise TypeError("Elements of argument must be integers or floats")
    result = []
    for i in vector:
        result.append([i])
    return result
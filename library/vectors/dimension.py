def single_dimension(vector, level):
    if not isinstance(vector, (list, tuple)) or not isinstance(vector[0], (list, tuple)) or isinstance(vector[0][0], (list, tuple)):
        raise TypeError("First argument must be a 2-dimensional list or tuple")
    if not isinstance(vector[0][0], (int, float)):
        raise TypeError("Elements nested within first argument must be integers or floats")
    if not isinstance(level, int) or not level <= len(vector[0]):
        raise ValueError("Second argument must be an integer less than or equal to the length of the nested lists")
    result = []
    for i in range(len(vector)):
        result.append(vector[i][level - 1])
    return result
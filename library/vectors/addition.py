def vector_sum(first_vector, second_vector):
    if not isinstance(first_vector, (list, tuple)) or not isinstance(second_vector, (list, tuple)) or isinstance(first_vector[0], (list, tuple)) or isinstance(second_vector[0], (list, tuple)):
        raise TypeError("Both arguments must be 1-dimensional lists or tuples")
    if not isinstance(first_vector[0], (int, float)) or not isinstance(second_vector[0], (int, float)):
        raise TypeError("Elements of arguments must be integers or floats")
    if len(first_vector) is not len(second_vector):
        raise ValueError("Both arguments must contain the same number of elements")
    result = []
    for i in range(len(first_vector)):
        result.append(first_vector[i] + second_vector[i])
    return result
def scalar_product(vector, number):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("First argument must be a 1-dimensional list or tuple")
    if not isinstance(vector[0], (int, float)):
        raise TypeError("Elements of first argument must be integers or floats")
    if not isinstance(number, (int, float)):
        raise TypeError("Second argument must be an integer or float")
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * number)
    return result

def dot_product(first_vector, second_vector):
    if not isinstance(first_vector, (list, tuple)) or not isinstance(second_vector, (list, tuple)) or isinstance(first_vector[0], (list, tuple)) or isinstance(second_vector[0], (list, tuple)):
        raise TypeError("Both arguments must be 1-dimensional lists or tuples")
    if not isinstance(first_vector[0], (int, float)) or not isinstance(second_vector[0], (int, float)):
        raise TypeError("Elements of both arguments must be integers or floats")
    if len(first_vector) is not len(second_vector):
        raise ValueError("Both arguments must contain the same number of elements")
    result = 0
    for i in range(len(first_vector)):
        result += first_vector[i] * second_vector[i]
    return result
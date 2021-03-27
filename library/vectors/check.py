def check_one(vector):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("Argument must be a 1-dimensional list or tuple")
    if not isinstance(vector[0], (int, float)):
        raise TypeError("Elements of argument must be integers or floats")

def check_two(first_vector, second_vector):
    if not isinstance(first_vector, (list, tuple)) or not isinstance(second_vector, (list, tuple)) or isinstance(first_vector[0], (list, tuple)) or isinstance(second_vector[0], (list, tuple)):
        raise TypeError("Both arguments must be 1-dimensional lists or tuples")
    if not isinstance(first_vector[0], (int, float)) or not isinstance(second_vector[0], (int, float)):
        raise TypeError("Elements of both arguments must be integers or floats")
    if len(first_vector) is not len(second_vector):
        raise ValueError("Both arguments must contain the same number of elements")

def check_nested(vector):
    if not isinstance(vector, (list, tuple)) or not isinstance(vector[0], (list, tuple)) or isinstance(vector[0][0], (list, tuple)):
        raise TypeError("First argument must be a 2-dimensional list or tuple")
    if not isinstance(vector[0][0], (int, float)):
        raise TypeError("Elements nested within first argument must be integers or floats")

def check_dimension(vector, level):
    if not isinstance(level, int) or not level <= len(vector[0]):
        raise ValueError("Second argument must be an integer less than or equal to the length of the nested lists within the first argument")

def check_length(vector, size):
    if not len(vector) == size:
        raise ValueError(f"Argument must contain exactly {size} elements")

def check_scalar_product(vector, scalar):
    if not isinstance(vector, (list, tuple)) or isinstance(vector[0], (list, tuple)):
        raise TypeError("First argument must be a 1-dimensional list or tuple")
    if not isinstance(vector[0], (int, float)):
        raise TypeError("Elements of first argument must be integers or floats")
    if not isinstance(scalar, (int, float)):
        raise TypeError("Second argument must be an integer or float")
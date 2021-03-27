from .check import check_scalar_product, check_two

def scalar_product(vector, scalar):
    check_scalar_product(vector, scalar)
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
    return result

def dot_product(first_vector, second_vector):
    check_two(first_vector, second_vector)
    result = 0
    for i in range(len(first_vector)):
        result += first_vector[i] * second_vector[i]
    return result
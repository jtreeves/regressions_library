from library.errors.scalars import last_scalar
from library.errors.vectors import first_vector, compare_vectors

def scalar_product(vector, scalar):
    first_vector(vector)
    last_scalar(scalar)
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
    return result

def dot_product(vector_one, vector_two):
    compare_vectors(vector_one, vector_two)
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
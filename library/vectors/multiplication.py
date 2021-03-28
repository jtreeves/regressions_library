from library.errors.scalars import scalar_value
from library.errors.vectors import vector_of_scalars, compare_vectors

def scalar_product(vector, scalar):
    vector_of_scalars(vector, 'first')
    scalar_value(scalar, 'second')
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
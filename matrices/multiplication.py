from .columns import columns, columns_vector
from .dot_product import dot_product

def multiplication(matrix_one, matrix_two):
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_two[0])):
            result[m].append(dot_product(matrix_one[m], columns(matrix_two)[n]))
    return result

def multiplication_vector(matrix, vector):
    r1c1 = dot_product(matrix[0], columns_vector(vector))
    r2c1 = dot_product(matrix[1], columns_vector(vector))
    result = [
        [r1c1],
        [r2c1]
    ]
    return result

def multiplication_vector_3d(matrix, vector):
    r1c1 = dot_product(matrix[0], columns_vector(vector))
    r2c1 = dot_product(matrix[1], columns_vector(vector))
    r3c1 = dot_product(matrix[2], columns_vector(vector))
    result = [
        [r1c1],
        [r2c1],
        [r3c1]
    ]
    return result
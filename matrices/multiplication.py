from .columns import columns, columns_vector
from .dot_product import dot_product

def multiplication(matrix_one, matrix_two):
    r1c1 = dot_product(matrix_one[0], columns(matrix_two)[0])
    r1c2 = dot_product(matrix_one[0], columns(matrix_two)[1])
    r2c1 = dot_product(matrix_one[1], columns(matrix_two)[0])
    r2c2 = dot_product(matrix_one[1], columns(matrix_two)[1])
    result = [
        [r1c1, r1c2],
        [r2c1, r2c2]
    ]
    return result

def multiplication_vector(matrix, vector):
    r1c1 = dot_product(matrix[0], columns_vector(vector))
    r2c1 = dot_product(matrix[1], columns_vector(vector))
    result = [
        [r1c1],
        [r2c1]
    ]
    return result

def multiplication_3d(matrix_one, matrix_two):
    r1c1 = dot_product(matrix_one[0], columns(matrix_two)[0])
    r1c2 = dot_product(matrix_one[0], columns(matrix_two)[1])
    r1c3 = dot_product(matrix_one[0], columns(matrix_two)[2])
    r2c1 = dot_product(matrix_one[1], columns(matrix_two)[0])
    r2c2 = dot_product(matrix_one[1], columns(matrix_two)[1])
    r2c3 = dot_product(matrix_one[1], columns(matrix_two)[2])
    r3c1 = dot_product(matrix_one[2], columns(matrix_two)[0])
    r3c2 = dot_product(matrix_one[2], columns(matrix_two)[1])
    r3c3 = dot_product(matrix_one[2], columns(matrix_two)[2])
    result = [
        [r1c1, r1c2, r1c3],
        [r2c1, r2c2, r2c3],
        [r3c1, r3c2, r3c3]
    ]
    return result

def multiplication_all(matrix_one, matrix_two):
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_two[0])):
            result[m].append(dot_product(matrix_one[m], matrix_two[n]))
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
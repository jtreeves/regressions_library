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
    result = []
    for m in range(len(matrix)):
        result.append([dot_product(matrix[m], columns_vector(vector))])
    return result
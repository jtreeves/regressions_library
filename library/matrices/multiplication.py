from library.errors.scalars import last_scalar
from library.errors.matrices import first_matrix, columns_rows
from library.vectors.multiplication import dot_product
from .transpose import adjugate

def scalar_product(matrix, scalar):
    first_matrix(matrix)
    last_scalar(scalar)
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(matrix[m][n] * scalar)
    return result

def matrix_product(matrix_one, matrix_two):
    columns_rows(matrix_one, matrix_two)
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_two[0])):
            result[m].append(dot_product(matrix_one[m], adjugate(matrix_two)[n]))
    return result
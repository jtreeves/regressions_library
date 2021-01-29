from .column import column
from .transpose import transpose
from .dot_product import dot_product

def multiplication(matrix_one, matrix_two):
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_two[0])):
            result[m].append(dot_product(matrix_one[m], transpose(matrix_two)[n]))
    return result
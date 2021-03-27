from .determinant import linear_determinant, inner_determinant

def matrix_of_minors(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(linear_determinant(inner_determinant(matrix, m, n)))
    return result
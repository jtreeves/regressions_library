from .determinant import determinant, diminished

def minors(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(determinant(diminished(matrix, m, n)))
    return result
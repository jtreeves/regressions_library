from library.errors.matrices import matrix_of_scalars

def adjugate(matrix):
    matrix_of_scalars(matrix, 'only')
    result = []
    for m in range(len(matrix[0])):
        result.append([])
        for n in range(len(matrix)):
            result[m].append(matrix[n][m])
    return result
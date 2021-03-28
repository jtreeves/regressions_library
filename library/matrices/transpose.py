from library.errors.matrices import first_matrix

def adjugate(matrix):
    first_matrix(matrix)
    result = []
    for m in range(len(matrix[0])):
        result.append([])
        for n in range(len(matrix)):
            result[m].append(matrix[n][m])
    return result
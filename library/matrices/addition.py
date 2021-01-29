def addition(first_matrix, second_matrix):
    result = []
    for m in range(len(first_matrix)):
        result.append([])
        for n in range(len(first_matrix[0])):
            result[m].append(first_matrix[m][n] + second_matrix[m][n])
    return result
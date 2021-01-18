def cofactors(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        if m % 2 == 0:
            for n in range(len(matrix[0])):
                if n % 2 == 0:
                    result[m].append(matrix[m][n])
                else:
                    result[m].append(-1 * matrix[m][n])
        else:
            for n in range(len(matrix[0])):
                if n % 2 == 0:
                    result[m].append(-1 * matrix[m][n])
                else:
                    result[m].append(matrix[m][n])
    return result
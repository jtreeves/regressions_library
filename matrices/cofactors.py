def cofactors(matrix):
    r1c1 = matrix[0][0]
    r1c2 = -1 * matrix[0][1]
    r1c3 = matrix[0][2]
    r2c1 = -1 * matrix[1][0]
    r2c2 = matrix[1][1]
    r2c3 = -1 * matrix[1][2]
    r3c1 = matrix[2][0]
    r3c2 = -1 * matrix[2][1]
    r3c3 = matrix[2][2]
    result = [
        [r1c1, r1c2, r1c3],
        [r2c1, r2c2, r2c3],
        [r3c1, r3c2, r3c3]
    ]
    return result

def cofactors_all(matrix):
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
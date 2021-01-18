def determinant(matrix):
    result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return result

def determinant_3d(matrix):
    right_determinant = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    spread_determinant = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    left_determinant = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    result = matrix[0][0] * right_determinant - matrix[0][1] * spread_determinant + matrix[0][2] * left_determinant
    return result

def determinant_all(matrix):
    result = []
    leads = []
    return leads

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
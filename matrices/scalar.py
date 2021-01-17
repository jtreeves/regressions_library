def scalar(matrix, number):
    r1c1 = matrix[0][0] * number
    r1c2 = matrix[0][1] * number
    r2c1 = matrix[1][0] * number
    r2c2 = matrix[1][1] * number
    result = [
        [r1c1, r1c2],
        [r2c1, r2c2]
    ]
    return result

def scalar_3d(matrix, number):
    r1c1 = matrix[0][0] * number
    r1c2 = matrix[0][1] * number
    r1c3 = matrix[0][2] * number
    r2c1 = matrix[1][0] * number
    r2c2 = matrix[1][1] * number
    r2c3 = matrix[1][2] * number
    r3c1 = matrix[2][0] * number
    r3c2 = matrix[2][1] * number
    r3c3 = matrix[2][2] * number
    result = [
        [r1c1, r1c2, r1c3],
        [r2c1, r2c2, r2c3],
        [r3c1, r3c2, r3c3]
    ]
    return result
def transpose(matrix):
    r1c1 = matrix[0][0]
    r1c2 = matrix[1][0]
    r2c1 = matrix[0][1]
    r2c2 = matrix[1][1]
    result = [
        [r1c1, r1c2],
        [r2c1, r2c2]
    ]
    return result
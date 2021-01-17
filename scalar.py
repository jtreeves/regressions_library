def scalar(matrix, number):
    r1c1 = matrix[0][0] * number
    r1c2 = matrix[0][1] * number
    r2c1 = matrix[1][0] * number
    r2c2 = matrix[1][1] * number
    result = [
        [r1c1,r1c2],
        [r2c1,r2c2]
    ]
    return result

A = [
    [3,-5],
    [2,9]
]

b = -3

C = scalar(A, b)

print(C) # => [[-9, 15], [-6, -27]]
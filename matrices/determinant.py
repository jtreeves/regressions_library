def determinant(matrix):
    result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return result

def determinant_3d(matrix):
    right_determinant = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    spread_determinant = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    left_determinant = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    result = matrix[0][0] * right_determinant - matrix[0][1] * spread_determinant + matrix[0][2] * left_determinant
    return result

A = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

det_A = determinant_3d(A)
print(det_A) # => -306
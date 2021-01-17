from matrix import columns

def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result

def multiplication(matrix_one, matrix_two):
    r1c1 = dot_product(matrix_one[0], columns(matrix_two)[0])
    r1c2 = dot_product(matrix_one[0], columns(matrix_two)[1])
    r2c1 = dot_product(matrix_one[1], columns(matrix_two)[0])
    r2c2 = dot_product(matrix_one[1], columns(matrix_two)[1])
    result = [
        [r1c1, r1c2],
        [r2c1, r2c2]
    ]
    return result

A = [
    [5, 8],
    [2, 3]
]

B = [
    [4, 1],
    [7, 3]
]

C = multiplication(A, B)

print(C) # => [[76, 29], [29, 11]]
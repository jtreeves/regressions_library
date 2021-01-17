def columns(matrix):
    column_one = []
    column_two = []
    for row in matrix:
        column_one.append(row[0])
        column_two.append(row[1])
    return [column_one, column_two]

def dot_product(vector_one, vector_two):
    result = 0
    for i in vector_one:
        for j in vector_two:
            result += i * j
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
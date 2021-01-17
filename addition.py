def addition(first_matrix, second_matrix):
    r1c1 = first_matrix[0][0] + second_matrix[0][0]
    r1c2 = first_matrix[0][1] + second_matrix[0][1]
    r2c1 = first_matrix[1][0] + second_matrix[1][0]
    r2c2 = first_matrix[1][1] + second_matrix[1][1]
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

C = addition(A,B)

print(C) # => [[9, 9], [9, 6]]
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

def addition_all(first_matrix, second_matrix):
    result = []
    for m in range(len(first_matrix)):
        for n in range(len(first_matrix[0])):
            result.append(first_matrix[m][n] + second_matrix[m][n])
    return result

A = [
    [2, 6, -9],
    [4, 5, 1]
]

B = [
    [7, 1, 3],
    [-8, 2, 5]
]

C = addition_all(A, B)
print(C) # => [[9, 7, -6], [-4, 7, 6]]
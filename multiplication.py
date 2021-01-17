A = [
    [5,8],
    [2,3]
]

B = [
    [4,1],
    [7,3]
]

rows_and_columns = {
    'first_matrix_first_row': A[0],
    'first_matrix_second_row': A[1],
    'second_matrix_first_row': B[0],
    'second_matrix_second_row': B[1],
    'first_matrix_first_column': [A[0][0],A[1][0]],
    'first_matrix_second_column': [A[0][1],A[1][1]],
    'second_matrix_first_column': [B[0][0],B[1][0]],
    'second_matrix_second_column': [B[1][0],B[1][1]]
}

def dot_product(array_one, array_two):
    for term in array_one:
        product = array_one[0]*array_two[0] + array_one[1]*array_two[1]
        return product

def matrix_product(matrix_one, matrix_two):
    r1c1 = dot_product(rows_and_columns['first_matrix_first_row'], rows_and_columns['second_matrix_first_column'])
    r1c2 = dot_product(rows_and_columns['first_matrix_first_row'], rows_and_columns['second_matrix_second_column'])
    r2c1 = dot_product(rows_and_columns['first_matrix_second_row'], rows_and_columns['second_matrix_first_column'])
    r2c2 = dot_product(rows_and_columns['first_matrix_second_row'], rows_and_columns['second_matrix_second_column'])
    product = [
        [r1c1,r1c2],
        [r2c1,r2c2]
    ]
    return product

C = matrix_product(A, B)

print(C)
from library.errors.matrices import compare_matrices

def matrix_sum(matrix_one, matrix_two):
    compare_matrices(matrix_one, matrix_two)
    result = []
    for m in range(len(matrix_one)):
        result.append([])
        for n in range(len(matrix_one[0])):
            result[m].append(matrix_one[m][n] + matrix_two[m][n])
    return result
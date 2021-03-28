def first_matrix(matrix):
    if not isinstance(matrix, (list, tuple)) or not isinstance(matrix[0], (list, tuple)) or isinstance(matrix[0][0], (list, tuple)):
        raise TypeError('First argument must be a 2-dimensional list or tuple')
    if not isinstance(matrix[0][0], (int, float)):
        raise TypeError('Elements nested within first argument must be integers or floats')

def second_matrix(matrix):
    if not isinstance(matrix, (list, tuple)) or not isinstance(matrix[0], (list, tuple)) or isinstance(matrix[0][0], (list, tuple)):
        raise TypeError('Second argument must be a 2-dimensional list or tuple')
    if not isinstance(matrix[0][0], (int, float)):
        raise TypeError('Elements nested within second argument must be integers or floats')

def square_matrix(matrix):
    first_matrix(matrix)
    if len(matrix) is not len(matrix[0]):
        raise ValueError('First argument must contain the same amount of lists as the amount of elements contained within its first list')

def compare_matrices(matrix_one, matrix_two):
    first_matrix(matrix_one)
    second_matrix(matrix_two)
    if len(matrix_one) is not len(matrix_two) or len(matrix_one[0]) is not len(matrix_two[0]):
        raise ValueError('Both arguments must have the same dimensions')

def columns_rows(matrix_one, matrix_two):
    first_matrix(matrix_one)
    second_matrix(matrix_two)
    if len(matrix_one[0]) is not len(matrix_two):
        raise ValueError('First list within first argument must contain the same amount of elements as the amount of lists contained within second argument')

def level(matrix, scalar):
    if not scalar <= len(matrix[0]):
        raise ValueError('Last argument must be less than or equal to the length of the nested lists within the first argument')
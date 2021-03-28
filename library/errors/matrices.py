def matrix_of_scalars(matrix, position):
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(matrix, (list, tuple)) or not isinstance(matrix[0], (list, tuple)) or isinstance(matrix[0][0], (list, tuple)):
        raise TypeError(f'{identifier.capitalize()} must be a 2-dimensional list or tuple')
    if not isinstance(matrix[0][0], (int, float)):
        raise TypeError(f'Elements nested within {identifier} must be integers or floats')
    else:
        return f'{identifier.capitalize()} is a 2-dimensional list or tuple containing elements that are integers or floats'

def square_matrix(matrix):
    matrix_of_scalars(matrix, 'first')
    if len(matrix) is not len(matrix[0]):
        raise ValueError('First argument must contain the same amount of lists as the amount of elements contained within its first list')
    else:
        return 'First argument contains the same amount of lists as the amount of elements contained within its first list'

def compare_rows(matrix_one, matrix_two):
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one) is not len(matrix_two):
        raise ValueError('First argument and second argument must contain the same amount of lists')
    else:
        return 'First argument and second argument contain the same amount of lists'

def compare_columns(matrix_one, matrix_two):
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one[0]) is not len(matrix_two[0]):
        raise ValueError('First list within first argument and first list within second argument must contain the same amount of elements')
    else:
        return 'First list within first argument and first list within second argument contain the same amount of elements'

def compare_matrices(matrix_one, matrix_two):
    compare_rows(matrix_one, matrix_two)
    compare_columns(matrix_one, matrix_two)
    return 'First argument and second argument contain the same amount of lists; first list within first argument and first list within second argument contain the same amount of elements'

def columns_rows(matrix_one, matrix_two):
    matrix_of_scalars(matrix_one, 'first')
    matrix_of_scalars(matrix_two, 'second')
    if len(matrix_one[0]) is not len(matrix_two):
        raise ValueError('First list within first argument must contain the same amount of elements as the amount of lists contained within second argument')
    else:
        return 'First list within first argument contains the same amount of elements as the amount of lists contained within second argument'

def level(matrix, scalar):
    if not scalar <= len(matrix[0]):
        raise ValueError('Last argument must be less than or equal to the length of the nested lists within the first argument')
    else:
        return 'Last argument is less than or equal to the length of the nested lists within the first argument'
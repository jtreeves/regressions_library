def nested(matrix):
    if not isinstance(matrix, (list, tuple)) or not isinstance(matrix[0], (list, tuple)) or isinstance(matrix[0][0], (list, tuple)):
        raise TypeError('First argument must be a 2-dimensional list or tuple')
    if not isinstance(matrix[0][0], (int, float)):
        raise TypeError('Elements nested within first argument must be integers or floats')

def level(matrix, scalar):
    if not scalar <= len(matrix[0]):
        raise ValueError('Last argument must be less than or equal to the length of the nested lists within the first argument')
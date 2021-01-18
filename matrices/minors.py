from .determinant import determinant

def diminished(matrix, row, column):
    result = []
    storage = {}
    for m in range(len(matrix)):
        if m != row:
            storage[m] = []
            for n in range(len(matrix[0])):
                if n!= column:
                    storage[m].append(matrix[m][n])
    for key in storage:
        result.append(storage[key])
    return result

def minors(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(determinant(diminished(matrix, m, n)))
    return result
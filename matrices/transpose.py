def transpose(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(matrix[n][m])
    return result

def transpose_all(matrix):
    result = []
    return result

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
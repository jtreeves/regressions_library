def transpose(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(matrix[n][m])
    return result

def transpose_all(matrix):
    result = []
    rows = len(matrix[0])
    columns = len(matrix)
    for row in range(rows):
        result.append([])
        for column in range(columns):
            result[row].append(matrix[column][row])
    return result
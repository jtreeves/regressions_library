def columns(matrix):
    result = []
    for m in range(len(matrix)):
        result.append([])
        for n in range(len(matrix[0])):
            result[m].append(matrix[n][m])
    return result

def columns_vector(vector):
    column_one = []
    for row in vector:
        column_one.append(row[0])
    return column_one
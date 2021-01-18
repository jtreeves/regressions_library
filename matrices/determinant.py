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

def determinant(matrix, result = 0):
    if len(matrix) == 1:
        result += matrix[0][0]
        return result
    else:
        alternating = []
        minors = []
        leads = matrix[0]
        for i in range(len(leads)):
            minors.append(diminished(matrix, 0, i))
            if i % 2 == 0:
                alternating.append(leads[i])
            else:
                alternating.append(-1 * leads[i])
        for j in range(len(alternating)):
            result += alternating[j] * determinant(minors[j])
    return result
def determinant(matrix):
    result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return result

def determinant_3d(matrix):
    right_determinant = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    spread_determinant = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    left_determinant = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    result = matrix[0][0] * right_determinant - matrix[0][1] * spread_determinant + matrix[0][2] * left_determinant
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

def determinant_all(matrix):
    print(matrix)
    result = 0
    alternating = []
    minors = []
    leads = matrix[0]
    print(leads)
    for i in range(len(leads)):
        minors.append(diminished(matrix, 0, i))
        if i % 2 == 0:
            alternating.append(leads[i])
        else:
            alternating.append(-1 * leads[i])
    print(alternating)
    print(minors)
    for j in range(len(alternating)):
        result += alternating[j] * determinant(minors[j])
    return result
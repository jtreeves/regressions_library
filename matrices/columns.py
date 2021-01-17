def columns(matrix):
    column_one = []
    column_two = []
    for row in matrix:
        column_one.append(row[0])
        column_two.append(row[1])
    return [column_one, column_two]

def columns_vector(vector):
    column_one = []
    for row in vector:
        column_one.append(row[0])
    return column_one

def columns_3d(matrix):
    column_one = []
    column_two = []
    column_three = []
    for row in matrix:
        column_one.append(row[0])
        column_two.append(row[1])
        column_three.append(row[2])
    return [column_one, column_two, column_three]
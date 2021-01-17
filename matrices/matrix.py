def columns(matrix):
    column_one = []
    column_two = []
    for row in matrix:
        column_one.append(row[0])
        column_two.append(row[1])
    return [column_one, column_two]
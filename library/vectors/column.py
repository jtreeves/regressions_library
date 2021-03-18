def column(vector):
    result = []
    for i in vector:
        result.append([i])
    return result

test_v = [1, 2, 3]
test_c = column(test_v)
print(f'ROW: {test_v}')
print(f'COLUMN: {test_c}')
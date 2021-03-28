from library.errors.vectors import vector_of_scalars

def sum_value(data):
    vector_of_scalars(data, 'only')
    result = 0
    for i in range(len(data)):
        result += data[i]
    return result
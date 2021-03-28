from library.errors.vectors import vector_of_scalars

def column_conversion(vector):
    vector_of_scalars(vector, 'only')
    result = []
    for i in vector:
        result.append([i])
    return result
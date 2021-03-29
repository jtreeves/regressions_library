from library.errors.vectors import vector_of_scalars

def column_conversion(vector):
    vector_of_scalars(vector, 'only')
    result = []
    for element in vector:
        result.append([element])
    return result
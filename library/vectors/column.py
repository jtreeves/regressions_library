from library.errors.vectors import first_vector

def column_conversion(vector):
    first_vector(vector)
    result = []
    for i in vector:
        result.append([i])
    return result
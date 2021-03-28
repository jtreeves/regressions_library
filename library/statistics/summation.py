from library.errors.vectors import first_vector

def sum_value(data):
    first_vector(data)
    result = 0
    for i in range(len(data)):
        result += data[i]
    return result
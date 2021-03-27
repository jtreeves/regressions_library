from .check import check_one

def column_conversion(vector):
    check_one(vector)
    result = []
    for i in vector:
        result.append([i])
    return result
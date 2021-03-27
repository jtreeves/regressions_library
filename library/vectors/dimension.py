from .check import check_nested, check_dimension

def single_dimension(vector, level):
    check_nested(vector)
    check_dimension(vector, level)
    result = []
    for i in range(len(vector)):
        result.append(vector[i][level - 1])
    return result
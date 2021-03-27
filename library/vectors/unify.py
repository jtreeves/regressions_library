from .check import check_two

def unite_vectors(first_vector, second_vector):
    check_two(first_vector, second_vector)
    result = []
    if first_vector[0] == None:
        result.append(None)
    else:
        for i in range(len(first_vector)):
            result.append([first_vector[i], second_vector[i]])
    return result
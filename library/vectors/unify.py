from library.errors.vectors import compare_vectors

def unite_vectors(vector_one, vector_two):
    compare_vectors(vector_one, vector_two)
    result = []
    if vector_one[0] == None:
        result.append(None)
    else:
        for i in range(len(vector_one)):
            result.append([vector_one[i], vector_two[i]])
    return result
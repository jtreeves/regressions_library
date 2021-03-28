from library.errors.vectors import compare_vectors

def vector_sum(vector_one, vector_two):
    compare_vectors(vector_one, vector_two)
    result = []
    for i in range(len(vector_one)):
        result.append(vector_one[i] + vector_two[i])
    return result
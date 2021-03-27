def scalar_product(vector, number):
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * number)
    return result

def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
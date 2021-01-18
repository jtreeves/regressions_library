from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def quadratic(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([data[i][0]**2, data[i][0], 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication_vector(second_product, dependent_matrix)
    result = [
        [solution[2][0]],
        [solution[1][0]],
        [solution[0][0]]
    ]
    return result
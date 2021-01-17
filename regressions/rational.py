from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def rational(data):
    independent_matrix = [
        [1 / data[0][0], 1],
        [1 / data[1][0], 1]
    ]
    dependent_matrix = [
        [1 / data[0][1]],
        [1 / data[1][1]]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication_vector(second_product, dependent_matrix)
    result = [
        [solution[1][0]],
        [solution[0][0]]
    ]
    return result
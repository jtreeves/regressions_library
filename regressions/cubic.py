from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def cubic(data):
    independent_matrix = [
        [data[0][0]**3, data[0][0]**2, data[0][0], 1],
        [data[1][0]**3, data[1][0]**2, data[1][0], 1],
        [data[2][0]**3, data[2][0]**2, data[2][0], 1],
        [data[3][0]**3, data[3][0]**2, data[3][0], 1]
    ]
    dependent_matrix = [
        [data[0][1]],
        [data[1][1]],
        [data[2][1]],
        [data[3][1]]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    result = multiplication_vector(second_product, dependent_matrix)
    return result
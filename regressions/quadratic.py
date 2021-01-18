from matrices.multiplication import multiplication_3d, multiplication_vector_3d
from matrices.transpose import transpose
from matrices.inverse import inverse_3d

def quadratic(data):
    independent_matrix = [
        [data[0][0]**2, data[0][0], 1],
        [data[1][0]**2, data[1][0], 1],
        [data[2][0]**2, data[2][0], 1]
    ]
    dependent_matrix = [
        [data[0][1]],
        [data[1][1]],
        [data[2][1]]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication_3d(transposition, independent_matrix)
    inversion = inverse_3d(product)
    second_product = multiplication_3d(inversion, transposition)
    result = multiplication_vector_3d(second_product, dependent_matrix)
    return result
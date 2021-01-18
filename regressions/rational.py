from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

def rational(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([1 / data[i][0], 1])
        dependent_matrix.append([1 / data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constants = [
        [solution[1][0]],
        [solution[0][0]]
    ]
    inaccuracy = error(independent_matrix, dependent_matrix, solution)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
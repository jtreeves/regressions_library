from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

def linear(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([data[i][0], 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication(second_product, dependent_matrix)
    def linear_equation(value):
        return solution[0][0]*value + solution[1][0]
    inaccuracy = error(data, linear_equation)
    result = {
        'constants': solution,
        'error': inaccuracy,
        'equation': linear_equation
    }
    return result
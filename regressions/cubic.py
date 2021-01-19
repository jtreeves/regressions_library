from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

def cubic(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([data[i][0]**3, data[i][0]**2, data[i][0], 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication(second_product, dependent_matrix)
    def equation(x):
        return solution[0][0]*x**3 + solution[1][0]*x**2 + solution[2][0]*x + solution[3][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        'error': inaccuracy,
        'equation': equation
    }
    return result
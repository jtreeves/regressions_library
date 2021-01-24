from math import sin, cos, atan, factorial
from numpy import matrix
from numpy.linalg import inv
from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose

# REGRESSION MODEL DOES NOT PRODUCE USEFUL RESULTS
# FUTURE VERSION SHOULD USE MACHINE LEARNING INSTEAD OF POWER EXPANSIONS
def sinusoidal(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([
            sin(data[i][0]),
            cos(data[i][0]),
            1
        ])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constants = [
        [solution[0][0]],
        [solution[1][0]],
        [solution[2][0]]
    ]
    equation = lambda x: constants[0][0] * sin(x) + constants[1][0] * cos(x) + constants[2][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
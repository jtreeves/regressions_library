from math import sin, cos, atan, factorial
from numpy import matrix
from numpy.linalg import inv
from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose

def sinusoidal(data):
    independent_matrix = []
    dependent_matrix = []
    dependent_sum = 0
    for i in range(len(data)):
        independent_matrix.append([
            data[i][0]**19,
            data[i][0]**18,
            data[i][0]**17,
            data[i][0]**16,
            data[i][0]**15,
            data[i][0]**14,
            data[i][0]**13,
            data[i][0]**12,
            data[i][0]**11,
            data[i][0]**10,
            data[i][0]**9,
            data[i][0]**8,
            data[i][0]**7,
            data[i][0]**6,
            data[i][0]**5,
            data[i][0]**4,
            data[i][0]**3,
            data[i][0]**2,
            data[i][0],
            1
        ])
        dependent_matrix.append([data[i][1]])
        dependent_sum += data[i][1]
    dependent_average = dependent_sum / len(data)
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constant_d = dependent_average
    constant_b = ((factorial(4)*solution[15][0])/(solution[19][0] - constant_d))**(1/4)
    constant_c = atan((-2 * solution[17][0]) / (constant_b * solution[18][0]))
    constant_a = (solution[19][0] - constant_d) / sin(constant_c)
    constants = [
        [constant_a],
        [constant_b],
        [constant_c],
        [constant_d]
    ]
    equation = lambda x: constants[0][0] * sin(constants[1][0]*x + constants[2][0]) + constants[3][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
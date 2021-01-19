from math import sin, cos, atan
from numpy import matrix
from numpy.linalg import inv
from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose

def sinusoidal(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([
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
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constant_b = (
        ((362880 * solution[0][0] / solution[8][0])**(1/8)) + 
        (((362880 * solution[0][0]) / (120 * solution[4][0]))**(1/4)) + 
        (((120 * solution[4][0]) / (solution[8][0]))**(1/4)) + 
        (((40320 * solution[1][0]) / (24 * solution[5][0]))**(1/4)) + 
        (((5040 * solution[2][0]) / (6 * solution[6][0]))**(1/4)) + 
        (((720 * solution[3][0]) / (2 * solution[7][0]))**(1/4))
    ) / 6
    constant_c = (
        atan((40320 * constant_b * solution[1][0]) / (362880 * solution[0][0])) +
        atan((-720 * constant_b**3 * solution[3][0]) / (362880 * solution[0][0])) +
        atan((24 * constant_b**5 * solution[5][0]) / (362880 * solution[0][0])) +
        atan((-2 * constant_b**7 * solution[7][0]) / (362880 * solution[0][0])) +
        atan((-40320 * solution[1][0]) / (5040 * constant_b * solution[2][0])) +
        atan((40320 * solution[1][0]) / (120 * constant_b**3 * solution[4][0])) +
        atan((-40320 * solution[1][0]) / (6 * constant_b**5 * solution[6][0])) +
        atan((40320 * solution[1][0]) / (constant_b**7 * solution[8][0])) +
        atan((720 * constant_b * solution[3][0]) / (5040 * solution[2][0])) +
        atan((-24 * constant_b**3 * solution[5][0]) / (5040 * solution[2][0])) +
        atan((2 * constant_b**5 * solution[7][0]) / (5040 * solution[2][0])) +
        atan((-720 * solution[3][0]) / (120 * constant_b * solution[4][0])) +
        atan((720 * solution[3][0]) / (6 * constant_b**3 * solution[6][0])) +
        atan((-720 * solution[3][0]) / (constant_b**5 * solution[8][0])) +
        atan((24 * constant_b * solution[5][0]) / (120 * solution[4][0])) +
        atan((-2 * constant_b**3 * solution[7][0]) / (120 * solution[4][0])) +
        atan((-24 * solution[5][0]) / (6 * constant_b * solution[6][0])) +
        atan((24 * solution[5][0]) / (constant_b**3 * solution[8][0])) +
        atan((2 * constant_b * solution[7][0]) / (6 * solution[6][0])) +
        atan((-2 * solution[7][0]) / (constant_b * solution[8][0])) +
        atan((-40320 * constant_b * solution[1][0]) / (362880 * solution[0][0])) +
        atan((720 * constant_b**3 * solution[3][0]) / (362880 * solution[0][0])) +
        atan((-24 * constant_b**5 * solution[5][0]) / (362880 * solution[0][0])) +
        atan((2 * constant_b**7 * solution[7][0]) / (362880 * solution[0][0])) +
        atan((40320 * solution[1][0]) / (5040 * constant_b * solution[2][0])) +
        atan((-40320 * solution[1][0]) / (120 * constant_b**3 * solution[4][0])) +
        atan((40320 * solution[1][0]) / (6 * constant_b**5 * solution[6][0])) +
        atan((-40320 * solution[1][0]) / (constant_b**7 * solution[8][0])) +
        atan((-720 * constant_b * solution[3][0]) / (5040 * solution[2][0])) +
        atan((24 * constant_b**3 * solution[5][0]) / (5040 * solution[2][0])) +
        atan((-2 * constant_b**5 * solution[7][0]) / (5040 * solution[2][0])) +
        atan((720 * solution[3][0]) / (120 * constant_b * solution[4][0])) +
        atan((-720 * solution[3][0]) / (6 * constant_b**3 * solution[6][0])) +
        atan((720 * solution[3][0]) / (constant_b**5 * solution[8][0])) +
        atan((-24 * constant_b * solution[5][0]) / (120 * solution[4][0])) +
        atan((2 * constant_b**3 * solution[7][0]) / (120 * solution[4][0])) +
        atan((24 * solution[5][0]) / (6 * constant_b * solution[6][0])) +
        atan((-24 * solution[5][0]) / (constant_b**3 * solution[8][0])) +
        atan((-2 * constant_b * solution[7][0]) / (6 * solution[6][0])) +
        atan((2 * solution[7][0]) / (constant_b * solution[8][0]))
    ) / 40
    constant_a = (
        (362880 * solution[0][0]) / ((constant_b**9) * cos(constant_c)) + 
        (40320 * solution[1][0]) / ((constant_b**8) * cos(constant_c)) + 
        (-5040 * solution[2][0]) / ((constant_b**7) * cos(constant_c)) + 
        (-720 * solution[3][0]) / ((constant_b**6) * cos(constant_c)) + 
        (120 * solution[4][0]) / ((constant_b**5) * cos(constant_c)) + 
        (24 * solution[5][0]) / ((constant_b**4) * cos(constant_c)) + 
        (-6 * solution[6][0]) / ((constant_b**3) * cos(constant_c)) + 
        (-2 * solution[7][0]) / ((constant_b**2) * cos(constant_c)) + 
        (solution[8][0]) / ((constant_b) * cos(constant_c))
    ) / 9
    constant_d = solution[9][0] - (constant_a * sin(constant_c))
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
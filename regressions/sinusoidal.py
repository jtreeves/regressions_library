from math import sin, cos, atan, factorial
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
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    b_low_close = ((factorial(5)*solution[14][0])/(solution[18][0]))**(1/4)
    b_high_close = ((factorial(19)*solution[0][0])/factorial(15)*(solution[4][0]))**(1/4)
    b_med_close = ((factorial(11)*solution[8][0])/factorial(7)*(solution[12][0]))**(1/4)
    b_far_spread = ((factorial(17)*solution[2][0])/(solution[18][0]))**(1/16)
    b_medium_spread = ((factorial(11)*solution[8][0])/(factorial(3)*solution[16][0]))**(1/8)
    b_alt_medium_spread = ((factorial(13)*solution[6][0])/(factorial(5)*solution[14][0]))**(1/8)
    print(f'b_low_close: {b_low_close}')
    print(f'b_high_close: {b_high_close}')
    print(f'b_med_close: {b_med_close}')
    print(f'b_far_spread: {b_far_spread}')
    print(f'b_medium_spread: {b_medium_spread}')
    print(f'b_alt_medium_spread: {b_alt_medium_spread}')
    constant_b = b_alt_medium_spread
    constant_c = atan((-2 * solution[17][0]) / (constant_b * solution[18][0]))
    constant_a = solution[18][0] / (constant_b * cos(constant_c))
    constant_d = solution[19][0] - (constant_a * sin(constant_c))
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
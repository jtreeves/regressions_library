from math import sin, cos, atan
from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

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
        print(f'SINUSOIDAL Independent Matrix: {independent_matrix}')
        print(f'SINUSOIDAL Dependent Matrix: {dependent_matrix}')
    transposition = transpose(independent_matrix)
    print(f'SINUSOIDAL Transposition: {transposition}')
    product = multiplication(transposition, independent_matrix)
    print(f'SINUSOIDAL Product: {product}')
    inversion = inverse(product)
    print(f'SINUSOIDAL Inversion: {inversion}')
    second_product = multiplication(inversion, transposition)
    print(f'SINUSOIDAL Second Product: {second_product}')
    solution = multiplication(second_product, dependent_matrix)
    print(f'SINUSOIDAL Solution: {solution}')
    constant_b = (
        ((362880 * solution[0][0] / solution[8][0])**(1/8)) + 
        (((362880 * solution[0][0]) / (120 * solution[4][0]))**(1/4)) + 
        (((120 * solution[4][0]) / (solution[8][0]))**(1/4)) + 
        (((40320 * solution[1][0]) / (24 * solution[5][0]))**(1/4)) + 
        (((5040 * solution[2][0]) / (6 * solution[6][0]))**(1/4)) + 
        (((720 * solution[3][0]) / (2 * solution[7][0]))**(1/4))
    ) / 6
    constant_c = (
        atan((-6720 * solution[1][0]) / ((constant_b**5) * solution[6][0]))
    ) / 20
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
    print(f'SINUSOIDAL Constants: {constants}')
    equation = lambda x: constants[0][0] * sin(constants[1][0]*x + constants[2][0]) + constants[3][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
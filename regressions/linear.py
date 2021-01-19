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
        print(f'LINEAR Independent Matrix: {independent_matrix}')
        print(f'LINEAR Dependent Matrix: {dependent_matrix}')
    transposition = transpose(independent_matrix)
    print(f'LINEAR Transposition: {transposition}')
    product = multiplication(transposition, independent_matrix)
    print(f'LINEAR Product: {product}')
    inversion = inverse(product)
    print(f'LINEAR Inversion: {inversion}')
    second_product = multiplication(inversion, transposition)
    print(f'LINEAR Second Product: {second_product}')
    solution = multiplication(second_product, dependent_matrix)
    print(f'LINEAR Solution: {solution}')
    equation = lambda x: solution[0][0]*x + solution[1][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        'error': inaccuracy
    }
    return result
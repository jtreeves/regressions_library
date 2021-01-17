from math import log, exp

from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def exponential(data):
    independent_matrix = [
        [data[0][0], 1],
        [data[1][0], 1]
    ]
    dependent_matrix = [
        [log(data[0][1])],
        [log(data[1][1])]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication_vector(second_product, dependent_matrix)
    result = [
        [exp(solution[1][0])],
        [exp(solution[0][0])]
    ]
    return result
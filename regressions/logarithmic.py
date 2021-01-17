from math import log
from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def logarithmic(data):
    independent_matrix = [
        [log(data[0][0]), 1],
        [log(data[1][0]), 1]
    ]
    dependent_matrix = [
        [data[0][1]],
        [data[1][1]]
    ]
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    inversion = inverse(product)
    second_product = multiplication(inversion, transposition)
    solution = multiplication_vector(second_product, dependent_matrix)
    result = [
        [solution[1][0]],
        [solution[0][0]]
    ]
    return result

logarithmic_set = [[1, 5], [9, 20]]
logarithmic_solution = logarithmic(logarithmic_set)
print(logarithmic_solution) # => [[5.0], [6.8268]]
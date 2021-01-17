from matrices.multiplication import multiplication, multiplication_vector
from matrices.transpose import transpose
from matrices.inverse import inverse

def linear(data):
    independent_matrix = [
        [data[0][0], 1],
        [data[1][0], 1]
    ]
    print(independent_matrix)
    dependent_matrix = [
        [data[0][1]],
        [data[1][1]]
    ]
    print(dependent_matrix)
    transposition = transpose(independent_matrix)
    print(transposition)
    product = multiplication(transposition, independent_matrix)
    print(product)
    inversion = inverse(product)
    print(inversion)
    second_product = multiplication(inversion, transposition)
    print(second_product)
    result = multiplication_vector(second_product, dependent_matrix)
    print(result)
    return result

solution = linear([[2, 5], [7, 6]])
print(solution)

# data = [[2, 5], [7, 6]]

# independent_matrix = [
#     [data[0][0], 1],
#     [data[1][0], 1]
# ]

# dependent_matrix = [
#     [data[0][1]],
#     [data[1][1]]
# ]

# transposition = transpose(independent_matrix)
# product = multiplication(transposition, independent_matrix)
# inversion = inverse(product)
# second_product = multiplication(inversion, transposition)
# solution = multiplication_vector(second_product, dependent_matrix)

# print(f'Independent: {independent_matrix}')
# print(f'Dependent: {dependent_matrix}')
# print(f'Transpose: {transposition}')
# print(f'Product of Independent and Transpose: {product}')
# print(f'Inverse of Product of Independent and Transpose: {inversion}')
# print(f'Product of Inverse of Product of Independent and Transpose and the Transpose Again: {second_product}')
# print(f'Solution: {solution}')
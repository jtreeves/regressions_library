from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

data = [[3, 4], [-4, 7]]

independent_matrix = [
    [data[0][0], 1],
    [data[1][0], 1]
]

dependent_matrix = [
    data[0][1],
    data[1][1]
]

transposition = transpose(independent_matrix)

product = multiplication(transposition, independent_matrix)

inversion = inverse(product)

second_product = multiplication(inversion, transposition)

solution = multiplication(second_product, dependent_matrix)

# solution_matrix = multiplication(multiplication(inverse(multiplication(transpose(independent_matrix), independent_matrix)), transpose(independent_matrix)), dependent_matrix)

# print(solution_matrix)

print(f'Independent: {independent_matrix}')
print(f'Transpose: {transposition}')
print(f'Product of Independent and Transpose: {product}')
print(f'Inverse of Product of Independent and Transpose: {inversion}')
print(f'Product of Inverse of Product of Independent and Transpose and the Transpose Again: {second_product}')
print(f'Solution: {solution}')
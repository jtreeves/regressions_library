from .addition import addition
from .multiplication import multiplication
from .scalar import scalar
from .transpose import transpose
from .determinant import determinant, determinant_3d
from .dot_product import dot_product
from .columns import columns
from .inverse import inverse, inverse_3d

first_input_matrix = [
    [5, 8],
    [2, 3]
]

second_input_matrix = [
    [4, 1],
    [7, 3]
]

first_3d_input_matrix = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

second_3d_input_matrix = [
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
]

first_2x3 = [
    [2, 6, -9],
    [4, 5, 1]
]

second_2x3 = [
    [7, 1, 3],
    [-8, 2, 5]
]

scalar_number = -7

columns_first = columns(first_input_matrix)
addition_output_matrix = addition(first_input_matrix, second_input_matrix)
result_2x3 = addition(first_2x3, second_2x3)
multiplication_output_matrix = multiplication(first_input_matrix, second_input_matrix)
scalar_output_matrix = scalar(first_input_matrix, scalar_number)
scalar_2x3 = scalar(first_2x3, scalar_number)
transpose_output_matrix = transpose(first_input_matrix)
transpose_3d = transpose(first_3d_input_matrix)
determinant_output = determinant(first_input_matrix)
dot_product_output = dot_product(first_input_matrix[0], columns(second_input_matrix)[0])
inverse_output = inverse(first_input_matrix)
determinant_output_3d = determinant_3d(first_3d_input_matrix)
inverse_output_3d = inverse_3d(second_3d_input_matrix)

print(f'Columns: {columns_first}')
print(f'Addition: {addition_output_matrix}') # => [[9, 9], [9, 6]]
print(f'Non-Square Addition: {result_2x3}') # => [[9, 7, -6], [-4, 7, 6]]
print(f'Multiplication: {multiplication_output_matrix}') # => [[76, 29], [29, 11]]
print(f'Scalar: {scalar_output_matrix}') # => [[-35, -56], [-14, -21]]
print(f'Non-Square Scalar: {scalar_2x3}') # => [[-14, -42, 63], [-28, -35, -7]]
print(f'Transpose Reg: {transpose_output_matrix}') # => [[5, 2], [8, 3]]
print(f'Transpose 3-D Reg: {transpose_3d}') # => [[6, 4, 2], [1, -2, 8], [1, 5, 7]]
print(f'Determinant: {determinant_output}') # => -1
print(f'Dot Product: {dot_product_output}') # => 76
print(f'Inverse: {inverse_output}') # => [[-3, 8], [2, -5]]
print(f'3-D Determinant: {determinant_output_3d}') # => -306
print(f'3-D Inverse: {inverse_output_3d}') # => [[0.2, 0.2, 0], [-0.2, 0.3, 1], [0.2, -0.3, 0]]
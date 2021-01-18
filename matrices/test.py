from .addition import addition
from .multiplication import multiplication, multiplication_vector
from .scalar import scalar
from .transpose import transpose
from .determinant import determinant, diminished
from .dot_product import dot_product
from .columns import columns
from .inverse import inverse, inverse_3d
from .cofactors import cofactors
from .minors import minors

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

first_vector = [
    [2],
    [3]
]

second_vector = [
    [2],
    [3],
    [5]
]

scalar_number = -7

columns_first = columns(first_input_matrix)
addition_output_matrix = addition(first_input_matrix, second_input_matrix)
result_2x3 = addition(first_2x3, second_2x3)
multiplication_output_matrix = multiplication(first_input_matrix, second_input_matrix)
multiplication_2x2_vector = multiplication_vector(first_input_matrix, first_vector)
multiplication_3x3_vector = multiplication_vector(first_3d_input_matrix, second_vector)
scalar_output_matrix = scalar(first_input_matrix, scalar_number)
scalar_2x3 = scalar(first_2x3, scalar_number)
transpose_output_matrix = transpose(first_input_matrix)
transpose_3d = transpose(first_3d_input_matrix)
determinant_output = determinant(first_input_matrix)
dot_product_output = dot_product(first_input_matrix[0], columns(second_input_matrix)[0])
inverse_output = inverse(first_input_matrix)
determinant_output_3d = determinant(first_3d_input_matrix)
inverse_output_3d = inverse_3d(second_3d_input_matrix)
cofactors_3d = cofactors(first_3d_input_matrix)
diminished_matrix = diminished(first_3d_input_matrix, 1, 2)
minors_3d = minors(first_3d_input_matrix)

print(f'Columns: {columns_first}')
print(f'Addition: {addition_output_matrix}') # => [[9, 9], [9, 6]]
print(f'Non-Square Addition: {result_2x3}') # => [[9, 7, -6], [-4, 7, 6]]
print(f'Multiplication: {multiplication_output_matrix}') # => [[76, 29], [29, 11]]
print(f'Multiplication Vector 2x2: {multiplication_2x2_vector}') # => [[34], [13]]
print(f'Multiplication Vector 3x3: {multiplication_3x3_vector}') # => [[20], [27], [63]]
print(f'Scalar: {scalar_output_matrix}') # => [[-35, -56], [-14, -21]]
print(f'Non-Square Scalar: {scalar_2x3}') # => [[-14, -42, 63], [-28, -35, -7]]
print(f'Transpose Reg: {transpose_output_matrix}') # => [[5, 2], [8, 3]]
print(f'Transpose 3-D Reg: {transpose_3d}') # => [[6, 4, 2], [1, -2, 8], [1, 5, 7]]
print(f'Determinant 2x2: {determinant_output}') # => -1
print(f'Dot Product: {dot_product_output}') # => 76
print(f'Inverse: {inverse_output}') # => [[-3, 8], [2, -5]]
print(f'Determinant 3x3: {determinant_output_3d}') # => -306
print(f'3-D Inverse: {inverse_output_3d}') # => [[0.2, 0.2, 0], [-0.2, 0.3, 1], [0.2, -0.3, 0]]
print(f'Cofactors 3-D: {cofactors_3d}') # => [[6, -1, 1], [-4, -2, -5], [2, -8, 7]]
print(f'Diminished: {diminished_matrix}') # =>  [[6, 1], [2, 8]]
print(f'Minors 3-D: {minors_3d}') # => [[-54, 18, 36], [-1, 40, 46], [7, 26, -16]]
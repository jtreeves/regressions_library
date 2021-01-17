from addition import addition
from multiplication import multiplication
from scalar import scalar
from transpose import transpose

first_input_matrix = [
    [5, 8],
    [2, 3]
]

second_input_matrix = [
    [4, 1],
    [7, 3]
]

scalar_number = -7

addition_output_matrix = addition(first_input_matrix, second_input_matrix)
multiplication_output_matrix = multiplication(first_input_matrix, second_input_matrix)
scalar_output_matrix = scalar(first_input_matrix, scalar_number)
transpose_output_matrix = transpose(first_input_matrix)

print(f'Addition: {addition_output_matrix}') # => [[9, 9], [9, 6]]
print(f'Multiplication: {multiplication_output_matrix}') # => [[76, 29], [29, 11]]
print(f'Scalar: {scalar_output_matrix}') # => [[-35, -56], [-14, -21]]
print(f'Transpose: {transpose_output_matrix}') # => [[5, 2], [8, 3]]
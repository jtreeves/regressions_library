from library.matrices.addition import addition
from library.matrices.scalar import scalar
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.cofactors import cofactors
from library.matrices.determinant import determinant, diminished
from library.matrices.minors import minors
from library.matrices.inverse import inverse
from library.matrices.solve import solve

first_2d = [
    [5, 8],
    [2, 3]
]

second_2d = [
    [4, 1],
    [7, 3]
]

first_3d = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

second_3d = [
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
]

first_4d = [
    [5, 2, -6, 2],
    [3, 4, 1, -5],
    [9, -8, 7, 1],
    [-2, 5, 0, 11]
]

second_4d = [
    [13, -7, 1, -12],
    [5, -16, 14, 5],
    [-8, 6, 2, 11],
    [3, 0, 8, -2]
]

first_2x3 = [
    [2, 6, -9],
    [4, 5, 1]
]

second_2x3 = [
    [7, 1, 3],
    [-8, 2, 5]
]

column_2d = [
    [3],
    [-4]
]

column_3d = [
    [5],
    [-1],
    [7]
]

scalar_number = -7

addition_2d = addition(first_2d, second_2d)
addition_3d = addition(first_3d, second_3d)
addition_4d = addition(first_4d, second_4d)
addition_2x3 = addition(first_2x3, second_2x3)

scalar_2d = scalar(first_2d)
scalar_3d = scalar(first_3d)
scalar_4d = scalar(first_4d)
scalar_2x3 = scalar(first_2x3)

multiplication_2d_first = multiplication(first_2d, second_2d)
multiplication_2d_second = multiplication(second_2d, first_2d)
multiplication_3d_first = multiplication(first_3d, second_3d)
multiplication_3d_second = multiplication(second_3d, first_3d)
multiplication_4d_first = multiplication(first_4d, second_4d)
multiplication_4d_second = multiplication(second_4d, first_4d)

transpose_2d = transpose(first_2d)
transpose_3d = transpose(first_3d)
transpose_4d = transpose(first_4d)
transpose_2x3 = transpose(first_2x3)

cofactors_2d = cofactors(first_2d)
cofactors_3d = cofactors(first_3d)
cofactors_4d = cofactors(first_4d)

determinant_2d = determinant(first_2d)
determinant_3d = determinant(first_3d)
determinant_4d = determinant(first_4d)

minors_2d = minors(first_2d)
minors_3d = minors(first_3d)
minors_4d = minors(first_4d)

inverse_2d = inverse(first_2d)
inverse_3d = inverse(first_3d)
inverse_4d = inverse(first_4d)

solve_2d = solve(first_2d, column_2d)
solve_3d = solve(first_3d, column_3d)

print(f'ADDITION 2D: {addition_2d}')
print(f'ADDITION 3D: {addition_3d}')
print(f'ADDITION 4D: {addition_4d}')
print(f'ADDITION 2X3: {addition_2x3}')

print(f'SCALAR 2D: {scalar_2d}')
print(f'SCALAR 3D: {scalar_3d}')
print(f'SCALAR 4D: {scalar_4d}')
print(f'SCALAR 2X3: {scalar_2x3}')

print(f'MULTIPLICATION 2D FIRST: {multiplication_2d_first}')
print(f'MULTIPLICATION 2D SECOND: {multiplication_2d_second}')
print(f'MULTIPLICATION 3D FIRST: {multiplication_3d_first}')
print(f'MULTIPLICATION 3D SECOND: {multiplication_3d_second}')
print(f'MULTIPLICATION 4D FIRST: {multiplication_4d_first}')
print(f'MULTIPLICATION 4D SECOND: {multiplication_4d_second}')

print(f'TRANSPOSE 2D: {transpose_2d}')
print(f'TRANSPOSE 3D: {transpose_3d}')
print(f'TRANSPOSE 4D: {transpose_4d}')
print(f'TRANSPOSE 2X3: {transpose_2x3}')

print(f'COFACTORS 2D: {cofactors_2d}')
print(f'COFACTORS 3D: {cofactors_3d}')
print(f'COFACTORS 4D: {cofactors_4d}')

print(f'DETERMINANT 2D: {determinant_2d}')
print(f'DETERMINANT 3D: {determinant_3d}')
print(f'DETERMINANT 4D: {determinant_4d}')

print(f'MINORS 2D: {minors_2d}')
print(f'MINORS 3D: {minors_3d}')
print(f'MINORS 4D: {minors_4d}')

print(f'INVERSE 2D: {inverse_2d}')
print(f'INVERSE 3D: {inverse_3d}')
print(f'INVERSE 4D: {inverse_4d}')

print(f'SOLVE 2D: {solve_2d}')
print(f'SOLVE 3D: {solve_3d}')
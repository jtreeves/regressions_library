from library.matrices.addition import addition
from library.matrices.scalar import scalar
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.cofactors import cofactors
from library.matrices.determinant import determinant
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

scalar_2d = scalar(first_2d, scalar_number)
scalar_3d = scalar(first_3d, scalar_number)
scalar_4d = scalar(first_4d, scalar_number)
scalar_2x3 = scalar(first_2x3, scalar_number)

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

print(f'ADDITION 2D: {addition_2d}') # [[9, 9], [9, 6]]
print(f'ADDITION 3D: {addition_3d}') # [[9, 1, 3], [6, -2, 3], [2, 9, 8]]
print(f'ADDITION 4D: {addition_4d}') # [[18, -5, -5, -10], [8, -12, 15, 0], [1, -2, 9, 12], [1, 5, 8, 9]]
print(f'ADDITION 2X3: {addition_2x3}') # [[9, 7, -6], [-4, 7, 6]]

print(f'SCALAR 2D: {scalar_2d}') # [[-35, -56], [-14, -21]]
print(f'SCALAR 3D: {scalar_3d}') # [[-42, -7, -7], [-28, 14, -35], [-14, -56, -49]]
print(f'SCALAR 4D: {scalar_4d}') # [[-35, -14, 42, -14], [-21, -28, -7, 35], [-63, 56, -49, -7], [14, -35, 0, -77]]
print(f'SCALAR 2X3: {scalar_2x3}') # [[-14, -42, 63], [-28, -35, -7]]

print(f'MULTIPLICATION 2D FIRST: {multiplication_2d_first}') # [[76, 29], [29, 11]]
print(f'MULTIPLICATION 2D SECOND: {multiplication_2d_second}') # [[22, 35], [41, 65]]
print(f'MULTIPLICATION 3D FIRST: {multiplication_3d_first}') # [[20, 1, 11], [8, 5, 17], [22, 7, -5]]
print(f'MULTIPLICATION 3D SECOND: {multiplication_3d_second}') # [[22, 19, 17], [8, -14, -12], [6, 6, 12]]
print(f'MULTIPLICATION 4D FIRST: {multiplication_4d_first}') # [[129, -103, 37, -120], [36, -79, 21, 5], [24, 107, -81, -73], [32, -66, 156, 27]]
print(f'MULTIPLICATION 4D SECOND: {multiplication_4d_second}') # [[77, -70, -78, -70], [93, -141, 52, 159], [-26, 47, 68, 77], [91, -68, 38, -8]]

print(f'TRANSPOSE 2D: {transpose_2d}') # [[5, 2], [8, 3]]
print(f'TRANSPOSE 3D: {transpose_3d}') # [[6, 4, 2], [1, -2, 8], [1, 5, 7]]
print(f'TRANSPOSE 4D: {transpose_4d}') # [[5, 3, 9, -2], [2, 4, -8, 5], [-6, 1, 7, 0], [2, -5, 1, 11]]
print(f'TRANSPOSE 2X3: {transpose_2x3}') # [[2, 4], [6, 5], [-9, 1]]

print(f'COFACTORS 2D: {cofactors_2d}') # [[5, -8], [-2, 3]]
print(f'COFACTORS 3D: {cofactors_3d}') # [[6, -1, 1], [-4, -2, -5], [2, -8, 7]]
print(f'COFACTORS 4D: {cofactors_4d}') # [[5, -2, -6, -2], [-3, 4, -1, -5], [9, 8, 7, -1], [2, 5, 0, 11]]

print(f'DETERMINANT 2D: {determinant_2d}') # -1
print(f'DETERMINANT 3D: {determinant_3d}') # -306
print(f'DETERMINANT 4D: {determinant_4d}') # 7992

print(f'MINORS 2D: {minors_2d}') # [[3, 2], [8, 5]]
print(f'MINORS 3D: {minors_3d}') # [[-54, 18, 36], [-1, 40, 46], [7, 26, -16]]
print(f'MINORS 4D: {minors_4d}') # [[576, 60, -828, -132], [-474, 1019, -609, -377], [426, 197, 345, -167], [-72, 492, -396, 516]]

print(f'INVERSE 2D: {inverse_2d}') # [[-3.0, 8.0], [2.0, -5.0]]
print(f'INVERSE 3D: {inverse_3d}') # [[0.17647058823529413, -0.0032679738562091504, -0.022875816993464054], [0.058823529411764705, -0.13071895424836602, 0.08496732026143791], [-0.11764705882352941, 0.1503267973856209, 0.05228758169934641]]
print(f'INVERSE 4D: {inverse_4d}') # [[0.07207207207207207, 0.05930930930930931, 0.0533033033033033, 0.009009009009009009], [-0.0075075075075075074, 0.1275025025025025, -0.02464964964964965, 0.06156156156156156], [-0.1036036036036036, 0.0762012012012012, 0.04316816816816817, 0.04954954954954955], [0.016516516516516516, -0.04717217217217217, 0.020895895895895897, 0.06456456456456457]]

print(f'SOLVE 2D: {solve_2d}') # [-41.00000000000239, 26.000000000001478]
print(f'SOLVE 3D: {solve_3d}') # [0.7254901960784309, 1.0196078431372546, -0.3725490196078431]
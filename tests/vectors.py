from library.vectors.direction import direction
from library.vectors.magnitude import magnitude
from library.vectors.unit import unit
from library.vectors.column import column
from library.vectors.dimension import dimension
from library.vectors.unify import unify
from library.vectors.addition import addition
from library.vectors.scalar import scalar
from library.vectors.dot_product import dot_product

first_point = [2, -3]
second_point = [5, 7]

first_vector = [2, 5, 9, 13]
second_vector = [1, -7, 23, -2]

nested_vector = [
    [3, 4], 
    [5, 9], 
    [2, 8]
]

scalar_number = -3

direction_vector = direction(first_point, second_point)
magnitude_vector = magnitude(first_point)
unit_vector = unit(first_point)

column_first = column(first_vector)
column_second = column(second_vector)

dimension_first = dimension(nested_vector, 1)
dimension_second = dimension(nested_vector, 2)

unify_first = unify(first_vector, second_vector)
unify_second = unify(second_vector, first_vector)

addition_first = addition(first_point, second_point)
addition_second = addition(first_vector, second_vector)

scalar_first = scalar(first_vector, scalar_number)
scalar_second = scalar(second_vector, scalar_number)

dot_product_first = dot_product(first_point, second_point)
dot_product_second = dot_product(first_vector, second_vector)

print(f'DIRECTION VECTOR: {direction_vector}') # {'radian': 1.2793395323170296, 'degree': 73.30075576600639}
print(f'MAGNITUDE VECTOR: {magnitude_vector}') # 3.605551275463989
print(f'UNIT VECTOR: {unit_vector}') # [0.5547001962252291, -0.8320502943378437]

print(f'COLUMN FIRST: {column_first}') # [[2], [5], [9], [13]]
print(f'COLUMN SECOND: {column_second}') # [[1], [-7], [23], [-2]]

print(f'DIMENSION FIRST: {dimension_first}') # [3, 5, 2]
print(f'DIMENSION SECOND: {dimension_second}') # [4, 9, 8]

print(f'UNIFY FIRST: {unify_first}') # [[2, 1], [5, -7], [9, 23], [13, -2]]
print(f'UNIFY SECOND: {unify_second}') # [[1, 2], [-7, 5], [23, 9], [-2, 13]]

print(f'ADDITION FIRST: {addition_first}') # [7, 4]
print(f'ADDITION SECOND: {addition_second}') # [3, -2, 32, 11]

print(f'SCALAR FIRST: {scalar_first}') # [-6, -15, -27, -39]
print(f'SCALAR SECOND: {scalar_second}') # [-3, 21, -69, 6]

print(f'DOT PRODUCT FIRST: {dot_product_first}') # -11
print(f'DOT PRODUCT SECOND: {dot_product_second}') # 148
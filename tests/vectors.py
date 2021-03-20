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

print(f'DIRECTION VECTOR: {direction_vector}')
print(f'MAGNITUDE VECTOR: {magnitude_vector}')
print(f'UNIT VECTOR: {unit_vector}')

print(f'COLUMN FIRST: {column_first}')
print(f'COLUMN SECOND: {column_second}')

print(f'DIMENSION FIRST: {dimension_first}')
print(f'DIMENSION SECOND: {dimension_second}')

print(f'UNIFY FIRST: {unify_first}')
print(f'UNIFY SECOND: {unify_second}')

print(f'ADDITION FIRST: {addition_first}')
print(f'ADDITION SECOND: {addition_second}')

print(f'SCALAR FIRST: {scalar_first}')
print(f'SCALAR SECOND: {scalar_second}')

print(f'DOT PRODUCT FIRST: {dot_product_first}')
print(f'DOT PRODUCT SECOND: {dot_product_second}')
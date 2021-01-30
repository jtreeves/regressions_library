from library.vectors.addition import addition
from library.vectors.dimension import dimension
from library.vectors.direction import direction
from library.vectors.dot_product import dot_product
from library.vectors.magnitude import magnitude
from library.vectors.scalar import scalar
from library.vectors.unit import unit

vec1 = [2, 5, 9, 13]
vec2 = [1, -7, 23, -2]
vec3 = [[3, 4], [5, 9], [2, 8]]

vecadd = addition(vec1, vec2)
vecdim1 = dimension(vec3, 1)
vecdim2 = dimension(vec3, 2)
vecdir = direction(vec1, vec2)
vecdot = dot_product(vec1, vec2)
vecmag = magnitude(vec1)
vecscal = scalar(vec1, 5)
vecunit = unit(vec1)

print(f'VECADD: {vecadd}') # => [3, -2, 32, 11]
print(f'VECDIM1: {vecdim1}') # => [3, 5, 2]
print(f'VECDIM1: {vecdim2}') # => [4, 9, 8]
print(f'VECDIR: {vecdir}') # => {'radian': 1.4876550949064553, 'degree': 85.23635830927383}
print(f'VECDOT: {vecdot}') # => 148
print(f'VECMAG: {vecmag}') # => 16.703293088490067
print(f'VECSCAL: {vecscal}') # => [10, 25, 45, 65]
print(f'VECUNIT: {vecunit}') # => [0.11973686801784993, 0.2993421700446248, 0.5388159060803247, 0.7782896421160245]
from library.vectors.addition import addition
from library.vectors.direction import direction
from library.vectors.dot_product import dot_product
from library.vectors.magnitude import magnitude
from library.vectors.scalar import scalar
from library.vectors.unit import unit

vec1 = [2, 5, 9, 13]
vec2 = [1, -7, 23, -2]

vecadd = addition(vec1, vec2)
vecdir = direction(vec1, vec2)
vecdot = dot_product(vec1, vec2)
# vecmag = magnitude(vec1)
vecscal = scalar(vec1, 5)
# vecunit = unit(vec1)

print(f'VECADD: {vecadd}') # => [3, -2, 32, 11]
print(f'VECDIR: {vecdir}') # => {'radian': 1.4876550949064553, 'degree': 85.23635830927383}
print(f'VECDOT: {vecdot}') # => 148
# print(f'VECMAG: {vecmag}')
print(f'VECSCAL: {vecscal}') # => [10, 25, 45, 65]
# print(f'VECUNIT: {vecunit}')
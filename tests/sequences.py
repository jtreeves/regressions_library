from library.sequences.summation import summation
from library.sequences.dimension import dimension

test_set1 = [2, 4, 8, 11]
test_set2 = [[3, 4], [5, 9], [2, 8]]

sum1 = summation(test_set1)
dim1 = dimension(test_set2, 1)
dim2 = dimension(test_set2, 2)

print(f'SUM1: {sum1}') # => 25
print(f'DIM1: {dim1}') # => [3, 5, 2]
print(f'DIM2: {dim2}') # => [4, 9, 8]
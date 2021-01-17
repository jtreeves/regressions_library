from .linear import linear
from .quadratic import quadratic

linear_set = [[2, 5], [7, 6]]
quadratic_set = [[1, 4], [2, 9], [3, 16]]

linear_solution = linear(linear_set)
quadratic_solution = quadratic(quadratic_set)

print(f'Linear: {linear_solution}') # => [[0.2], [4.6]]
print(f'Quadratic: {quadratic_solution}') # => [[1.0], [2.0], [1.0]]
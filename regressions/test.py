from .linear import linear
from .quadratic import quadratic
from .exponential import exponential
from .logarithmic import logarithmic

linear_set = [[2, 5], [7, 6]]
quadratic_set = [[1, 4], [2, 9], [3, 16]]
exponential_set = [[1, 6], [2, 12]]
logarithmic_set = [[1, 5], [9, 20]]

linear_solution = linear(linear_set)
quadratic_solution = quadratic(quadratic_set)
exponential_solution = exponential(exponential_set)
logarithmic_solution = logarithmic(logarithmic_set)

print(f'Linear: {linear_solution}') # => [[0.2], [4.6]]
print(f'Quadratic: {quadratic_solution}') # => [[1.0], [2.0], [1.0]]
print(f'Exponential: {exponential_solution}') # => [[3.0], [2.0]]
print(f'Logarithmic: {logarithmic_solution}') # => [[5.0], [6.8268]]
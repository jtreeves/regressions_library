from .linear import linear
from .quadratic import quadratic
from .exponential import exponential
from .logarithmic import logarithmic
from .rational import rational

linear_set = [[2, 5], [7, 6]]
quadratic_set = [[1, 4], [2, 9], [3, 16]]
exponential_set = [[1, 6], [2, 12]]
logarithmic_set = [[1, 5], [9, 20]]
rational_set = [[2, 2], [3, 1]]

linear_solution = linear(linear_set)
quadratic_solution = quadratic(quadratic_set)
exponential_solution = exponential(exponential_set)
logarithmic_solution = logarithmic(logarithmic_set)
rational_solution = rational(rational_set)

print(f'Linear Matrix: {linear_solution}') # => [[0.2], [4.6]]
print(f'Linear Equation: y = {linear_solution[0][0]}x + {linear_solution[1][0]}') # => y = 0.2x + 4.6
print(f'Quadratic Matrix: {quadratic_solution}') # => [[1.0], [2.0], [1.0]]
print(f'Quadratic Equation: y = {quadratic_solution[0][0]}x^2 + {quadratic_solution[1][0]}x + {quadratic_solution[2][0]}') # => y = 1.0x^2 + 2.0x + 1.0
print(f'Exponential Matrix: {exponential_solution}') # => [[3.0], [2.0]]
print(f'Exponential Equation: y = {exponential_solution[0][0]}*{exponential_solution[1][0]}^x') # => y = 3.0*2.0^x
print(f'Logarithmic Matrix: {logarithmic_solution}') # => [[5.0], [6.8268]]
print(f'Logarithmic Equation: y = {logarithmic_solution[0][0]} + {logarithmic_solution[1][0]}*lnx') # => y = 5.0 + 6.8268*lnx
print(f'Rational Matrix: {rational_solution}') # => [[2.0], [-3.0]]
print(f'Rational Equation: y = x / ({rational_solution[0][0]}x + {rational_solution[1][0]})') # => [[2.0], [-3.0]]
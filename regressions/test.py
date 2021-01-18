from .linear import linear
from .quadratic import quadratic
from .cubic import cubic
from .rational import rational
from .exponential import exponential
from .logarithmic import logarithmic

linear_set = [[2, 5], [7, 6]]
linear_set_3 = [[1, 5], [2, 7], [3, 9]]
linear_set_10 = [[1, 2], [2, 1], [3, 4], [4, 6], [5, 5], [6, 8], [7, 8], [8, 7], [9, 11], [10, 14]]
quadratic_set = [[1, 4], [2, 9], [3, 16]]
cubic_set = [[1, 6], [2, 16], [3, 58], [4, 150]]
rational_set = [[2, 2], [3, 1]]
exponential_set = [[1, 6], [2, 12]]
logarithmic_set = [[1, 5], [9, 20]]

linear_solution = linear(linear_set)
linear_solution_3 = linear(linear_set_3)
linear_solution_10 = linear(linear_set_10)
quadratic_solution = quadratic(quadratic_set)
cubic_solution = cubic(cubic_set)
rational_solution = rational(rational_set)
exponential_solution = exponential(exponential_set)
logarithmic_solution = logarithmic(logarithmic_set)

print(f'Linear Matrix: {linear_solution}') # => [[0.2], [4.6]]
print(f'Linear Equation: y = {linear_solution[0][0]}x + {linear_solution[1][0]}') # => y = 0.2x + 4.6
print(f'Linear Matrix 3: {linear_solution_3}') # => [[2.0], [3.0]]
print(f'Linear Equation 3: y = {linear_solution_3[0][0]}x + {linear_solution_3[1][0]}') # => y = 2.0x + 3.0
print(f'Linear Matrix 10: {linear_solution_10}') # => [[1.2242], [-0.1333]]
print(f'Linear Equation 10: y = {linear_solution_10[0][0]}x + {linear_solution_10[1][0]}') # => y = 1.2242x + -0.1333
print(f'Quadratic Matrix: {quadratic_solution}') # => [[1.0], [2.0], [1.0]]
print(f'Quadratic Equation: y = {quadratic_solution[0][0]}x^2 + {quadratic_solution[1][0]}x + {quadratic_solution[2][0]}') # => y = 1.0x^2 + 2.0x + 1.0
print(f'Cubic Matrix: {cubic_solution}') # => [[3.0], [-2.0], [-5.0], [10.0]]
print(f'Cubic Equation: y = {cubic_solution[0][0]}x^3 + {cubic_solution[1][0]}x^2 + {cubic_solution[2][0]}x + {cubic_solution[3][0]}') # => y = 3.0x^3 + -2.0x^2 + -5.0x + 10.0
print(f'Rational Matrix: {rational_solution}') # => [[2.0], [-3.0]]
print(f'Rational Equation: y = x / ({rational_solution[0][0]}x + {rational_solution[1][0]})') # => y = x / (2.0x + -3.0)
print(f'Exponential Matrix: {exponential_solution}') # => [[3.0], [2.0]]
print(f'Exponential Equation: y = {exponential_solution[0][0]}*{exponential_solution[1][0]}^x') # => y = 3.0*2.0^x
print(f'Logarithmic Matrix: {logarithmic_solution}') # => [[5.0], [6.8268]]
print(f'Logarithmic Equation: y = {logarithmic_solution[0][0]} + {logarithmic_solution[1][0]}*lnx') # => y = 5.0 + 6.8268*lnx
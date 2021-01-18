from .linear import linear
from .quadratic import quadratic
from .cubic import cubic
from .rational import rational
from .hyperbolic import hyperbolic
from .exponential import exponential
from .logarithmic import logarithmic

linear_set = [[2, 5], [7, 6]]
linear_set_3 = [[1, 5], [2, 7], [3, 9]]
linear_set_error = [[0, 6], [1, 0], [2, 0]]
linear_set_10 = [[1, 2], [2, 1], [3, 4], [4, 6], [5, 5], [6, 8], [7, 8], [8, 7], [9, 11], [10, 14]]
quadratic_set = [[1, 4], [2, 9], [3, 16]]
quadratic_set_5 = [[1, 5], [2, 12], [3, 34], [4, 23], [5, 2]]
quadratic_set_10 = [[83, 183], [71, 168], [64, 171], [69, 178], [69, 176], [64, 172], [68, 165], [59, 158], [81, 183], [91, 182]]
cubic_set = [[1, 6], [2, 16], [3, 58], [4, 150]]
cubic_set_10 = [[1, 3], [2, 29], [3, 40], [4, 73], [5, 56], [6, 22], [7, 10], [8, 17], [9, 51], [10, 89]]
rational_set = [[2, 2], [3, 1]]
exponential_set = [[1, 6], [2, 12]]
logarithmic_set = [[1, 5], [9, 20]]
agnostic_set = [[1, 3], [2, 147], [3, 286], [4, 352], [5, 423], [6, 510], [7, 591], [8, 451], [9, 689], [10, 862]]

linear_solution = linear(linear_set)
linear_solution_3 = linear(linear_set_3)
linear_solution_error = linear(linear_set_error)
linear_solution_10 = linear(linear_set_10)
linear_solution_agnostic = linear(agnostic_set)
quadratic_solution = quadratic(quadratic_set)
quadratic_solution_5 = quadratic(quadratic_set_5)
quadratic_solution_10 = quadratic(quadratic_set_10)
quadratic_solution_agnostic = quadratic(agnostic_set)
cubic_solution = cubic(cubic_set)
cubic_solution_10 = cubic(cubic_set_10)
cubic_solution_agnostic = cubic(agnostic_set)
rational_solution = rational(rational_set)
hyperbolic_solution = hyperbolic(rational_set)
hyperbolic_solution_agnostic = hyperbolic(agnostic_set)
exponential_solution = exponential(exponential_set)
exponential_solution_agnostic = exponential(agnostic_set)
logarithmic_solution = logarithmic(logarithmic_set)
logarithmic_solution_agnostic = logarithmic(agnostic_set)

# print(f'Linear Matrix: {linear_solution}') # => [[0.2], [4.6]]
# print(f'Linear Equation: y = {linear_solution[0][0]}x + {linear_solution[1][0]}') # => y = 0.2x + 4.6
# print(f'Linear Matrix 3: {linear_solution_3}') # => [[2.0], [3.0]]
# print(f'Linear Equation 3: y = {linear_solution_3[0][0]}x + {linear_solution_3[1][0]}') # => y = 2.0x + 3.0
# print(f'Linear Matrix 10: {linear_solution_10}') # => [[1.2242], [-0.1333]]
# print(f'Linear Equation 10: y = {linear_solution_10[0][0]}x + {linear_solution_10[1][0]}') # => y = 1.2242x + -0.1333
print(f"Linear Matrix Agnostic: {linear_solution_agnostic['solution']}") # => [[79.7212], [−7.0667]]
print(f"Linear Error Agnostic: {linear_solution_agnostic['weakness']}") # => [[79.7212], [−7.0667]]
print(f"Linear Matrix 3: {linear_solution_error['solution']}") # => [[79.7212], [−7.0667]]
print(f"Linear Error 3: {linear_solution_error['weakness']}") # => [[79.7212], [−7.0667]]
# print(f'Linear Equation Agnostic: y = {linear_solution_agnostic[0][0]}x + {linear_solution_agnostic[1][0]}') # => y = 79.7212x + −7.0667
print(f'Quadratic Matrix: {quadratic_solution}') # => [[1.0], [2.0], [1.0]]
print(f'Quadratic Equation: y = {quadratic_solution[0][0]}x^2 + {quadratic_solution[1][0]}x + {quadratic_solution[2][0]}') # => y = 1.0x^2 + 2.0x + 1.0
print(f'Quadratic Matrix 5: {quadratic_solution_5}') # => [[−6.3571], [38.6429], [−30.8000]]
print(f'Quadratic Equation 5: y = {quadratic_solution_5[0][0]}x^2 + {quadratic_solution_5[1][0]}x + {quadratic_solution_5[2][0]}') # => y = −6.3571x^2 + 38.6429x + −30.8000
print(f'Quadratic Matrix 10: {quadratic_solution_10}') # => [[-0.0259], [4.5614], [-18.3907]]
print(f'Quadratic Equation 10: y = {quadratic_solution_10[0][0]}x^2 + {quadratic_solution_10[1][0]}x + {quadratic_solution_10[2][0]}') # => y = -0.0259x^2 + 4.5614x + -18.3907
print(f'Quadratic Matrix Agnostic: {quadratic_solution_agnostic}') # => [[−1.6515], [97.8879], [−43.4000]]
print(f'Quadratic Equation Agnostic: y = {quadratic_solution_agnostic[0][0]}x^2 + {quadratic_solution_agnostic[1][0]}x + {quadratic_solution_agnostic[2][0]}') # => y = −1.6515x^2 + 97.8879x + −43.4000
print(f'Cubic Matrix: {cubic_solution}') # => [[3.0], [-2.0], [-5.0], [10.0]]
print(f'Cubic Equation: y = {cubic_solution[0][0]}x^3 + {cubic_solution[1][0]}x^2 + {cubic_solution[2][0]}x + {cubic_solution[3][0]}') # => y = 3.0x^3 + -2.0x^2 + -5.0x + 10.0
print(f'Cubic Matrix 10: {cubic_solution_10}') # => [[1.2568], [-20.3811], [95.3015], [-80.6667]]
print(f'Cubic Equation 10: y = {cubic_solution_10[0][0]}x^3 + {cubic_solution_10[1][0]}x^2 + {cubic_solution_10[2][0]}x + {cubic_solution_10[3][0]}') # => y = 1.2568x^3 + -20.3811x^2 + 95.3015x + -80.6667
print(f'Cubic Matrix Agnostic: {cubic_solution_agnostic}') # => [[2.7704], [−47.3631], [308.7150], [−281.1000]]
print(f'Cubic Equation Agnostic: y = {cubic_solution_agnostic[0][0]}x^3 + {cubic_solution_agnostic[1][0]}x^2 + {cubic_solution_agnostic[2][0]}x + {cubic_solution_agnostic[3][0]}') # => y = 2.7704x^3 + −47.3631x^2 + 308.7150x + −281.1000
print(f'Rational Matrix: {rational_solution}') # => [[2.0], [-3.0]]
print(f'Rational Equation: y = x / ({rational_solution[0][0]}x + {rational_solution[1][0]})') # => y = x / (2.0x + -3.0)
print(f'Hyperbolic Matrix: {hyperbolic_solution}') # => [[6.0], [-1.0]]
print(f'Hyperbolic Equation: y = {hyperbolic_solution[0][0]}*(1/x) + {hyperbolic_solution[1][0]}') # => y = 6.0*(1/x) + -1.0
print(f'Hyperbolic Matrix Agnostic: {hyperbolic_solution_agnostic}') # => [[-766.8421], [656.0056]]
print(f'Hyperbolic Equation Agnostic: y = {hyperbolic_solution_agnostic[0][0]}*(1/x) + {hyperbolic_solution_agnostic[1][0]}') # => y = -766.8421*(1/x) + 656.0056
print(f'Exponential Matrix: {exponential_solution}') # => [[3.0], [2.0]]
print(f'Exponential Equation: y = {exponential_solution[0][0]}*{exponential_solution[1][0]}^x') # => y = 3.0*2.0^x
print(f'Exponential Matrix Agnostic: {exponential_solution_agnostic}') # => [[29.2304], [1.4898]]
print(f'Exponential Equation Agnostic: y = {exponential_solution_agnostic[0][0]}*{exponential_solution_agnostic[1][0]}^x') # => y = 29.2304*1.4898^x
print(f'Logarithmic Matrix: {logarithmic_solution}') # => [[5.0], [6.8268]]
print(f'Logarithmic Equation: y = {logarithmic_solution[0][0]} + {logarithmic_solution[1][0]}*lnx') # => y = 5.0 + 6.8268*lnx
print(f'Logarithmic Matrix Agnostic: {logarithmic_solution_agnostic}') # => [[−58.7194], [324.4875]]
print(f'Logarithmic Equation Agnostic: y = {logarithmic_solution_agnostic[0][0]} + {logarithmic_solution_agnostic[1][0]}*lnx') # => y = −58.7194 + 324.4875*lnx
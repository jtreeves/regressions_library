from math import log
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.logarithmic import logarithmic as logarithmic_equation
from library.analyses.derivatives.logarithmic import logarithmic as logarithmic_derivative
from library.analyses.integrals.logarithmic import logarithmic as logarithmic_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def logarithmic(data):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([log(independent_variable[i]), 1])
    solution = solve(independent_matrix, dependent_matrix)
    equation = logarithmic_equation(*solution)
    derivative = logarithmic_derivative(*solution)
    integral = logarithmic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('logarithmic', solution, equation, first_derivative, second_derivative)
    five_numbers = five_number_summary(independent_variable)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    averages_range = average_values('logarithmic', equation, integral, min_value, max_value, solution)
    averages_iqr = average_values('logarithmic', equation, integral, q1, q3, solution)
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted)
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    points = {
        'roots': points['roots'],
        'maxima': points['maxima'],
        'minima': points['minima'],
        'inflections': points['inflections']
    }
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    averages = {
        'range': averages_range,
        'iqr': averages_iqr
    }
    result = {
        'constants': solution,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result

test_set = [[3, 4], [5, 5], [10, 7], [15, 10]]
test_eval = logarithmic(test_set)
print(test_eval)

# {'constants': [3.5554345374844885, -0.36082024840229643], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x1089bf820>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x1089bf8b0>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x1089bf9d0>}, 'points': {'roots': [[1.1068123741825462, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 85.71123855966133, 'iqr': 63.328232989362206}, 'averages': {'range': {'average_value_derivative': 0.47685426165042805, 'mean_values_derivative': [7.456019214715341], 'average_value_integral': 7.142603213305111, 'mean_values_integral': [8.251621109880897]}, 'iqr': {'average_value_derivative': 0.5341072399844179, 'mean_values_derivative': [6.65678027054682], 'average_value_integral': 6.666129788353916, 'mean_values_integral': [7.216694099878332]}}, 'correlation': 0.9622367701056326}
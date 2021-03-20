from math import log, exp
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.derivatives.exponential import exponential as exponential_derivative
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def exponential(data):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i], 1])
        dependent_matrix.append([log(dependent_variable[i])])
    solution = solve(independent_matrix, dependent_matrix)
    constants = [exp(solution[1]), exp(solution[0])]
    equation = exponential_equation(*constants)
    derivative = exponential_derivative(*constants)
    integral = exponential_integral(*constants)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('exponential', solution, equation, first_derivative, second_derivative)
    five_numbers = five_number_summary(independent_variable)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    averages_range = average_values('exponential', equation, integral, min_value, max_value, constants)
    averages_iqr = average_values('exponential', equation, integral, q1, q3, constants)
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
        'constants': constants,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result

test_set = [[3, 7], [5, 19], [10, 84], [15, 231]]
test_eval = exponential(test_set)
print(test_eval)

# RESULT: {'constants': [3.8245799466028427, 1.329471489298669], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x1132a08b0>, 'derivative': <function exponential.<locals>.first_derivative at 0x1132a0940>, 'integral': <function exponential.<locals>.exponential_integral at 0x1132a0a60>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 930.6244416670079, 'iqr': 440.57012267343765}, 'averages': {'range': {'average_value_derivative': 22.085384345206858, 'mean_values_derivative': [10.567753347434644], 'average_value_integral': 77.552036805584, 'mean_values_integral': [10.567753347434644]}, 'iqr': {'average_value_derivative': 13.20696995482896, 'mean_values_derivative': [8.762259118959479], 'average_value_integral': 46.37580238667765, 'mean_values_integral': [8.762259118959477]}}, 'correlation': 0.9649262015080358}
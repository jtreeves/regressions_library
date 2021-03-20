from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.linear import linear as linear_equation
from library.analyses.derivatives.linear import linear as linear_derivative
from library.analyses.integrals.linear import linear as linear_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def linear(data):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i], 1])
    solution = solve(independent_matrix, dependent_matrix)
    equation = linear_equation(*solution)
    derivative = linear_derivative(*solution)
    integral = linear_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('linear', solution, equation, first_derivative, second_derivative)
    five_numbers = five_number_summary(independent_variable)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    averages_range = average_values('linear', equation, integral, min_value, max_value, solution)
    averages_iqr = average_values('linear', equation, integral, q1, q3, solution)
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

test_set = [[3, 7], [5, 11], [10, 17], [15, 22]]
test_eval = linear(test_set)
print(test_eval)

# {'constants': [1.219020172910662, 4.193083573487032], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x118f55820>, 'derivative': <function linear.<locals>.first_derivative at 0x118f558b0>, 'integral': <function linear.<locals>.linear_integral at 0x118f559d0>}, 'points': {'roots': [[-3.4397163120567398, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 181.9711815561959, 'iqr': 129.5846541786743}, 'averages': {'range': {'average_value_derivative': 1.2190201729106622, 'mean_values_derivative': ['All'], 'average_value_integral': 15.16426512968299, 'mean_values_integral': [9.0]}, 'iqr': {'average_value_derivative': 1.219020172910662, 'mean_values_derivative': ['All'], 'average_value_integral': 13.640489913544663, 'mean_values_integral': [7.75]}}, 'correlation': 0.9929440678487984}
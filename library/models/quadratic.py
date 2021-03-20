from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.quadratic import quadratic as quadratic_equation
from library.analyses.derivatives.quadratic import quadratic as quadratic_derivative
from library.analyses.integrals.quadratic import quadratic as quadratic_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def quadratic(data):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i]**2, independent_variable[i], 1])
    solution = solve(independent_matrix, dependent_matrix)
    equation = quadratic_equation(*solution)
    derivative = quadratic_derivative(*solution)
    integral = quadratic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('quadratic', solution, equation, first_derivative, second_derivative)
    five_numbers = five_number_summary(independent_variable)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value)
    accumulated_iqr = accumulation(integral, q1, q3)
    averages_range = average_values('quadratic', equation, integral, min_value, max_value, solution)
    averages_iqr = average_values('quadratic', equation, integral, q1, q3, solution)
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

test_set = [[3, 4], [5, 11], [10, 13], [15, 5]]
test_eval = quadratic(test_set)
print(test_eval)

# {'constants': [-0.25471134704711385, 4.592932979429327, -6.7813536828135454], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x114ad1790>, 'derivative': <function quadratic.<locals>.first_derivative at 0x114ad1820>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x114ad1940>}, 'points': {'roots': [[1.6224599450221975, 0], [16.40945356285845, 0]], 'maxima': [[9.015956753940323, 13.923488875326996]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 130.40265428002579, 'iqr': 110.19653284671479}, 'averages': {'range': {'average_value_derivative': 0.008128732581278738, 'mean_values_derivative': [9.0], 'average_value_integral': 10.866887856668816, 'mean_values_integral': [5.55181838805534, 12.480095119825306]}, 'iqr': {'average_value_derivative': 0.6449071001990628, 'mean_values_derivative': [7.75], 'average_value_integral': 11.599635036496293, 'mean_values_integral': [5.995446890327815, 12.036466617552831]}}, 'correlation': 0.9793862893911137}
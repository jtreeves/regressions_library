from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.hyperbolic import hyperbolic as hyperbolic_equation
from library.analyses.derivatives.hyperbolic import hyperbolic as hyperbolic_derivative
from library.analyses.integrals.hyperbolic import hyperbolic as hyperbolic_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def hyperbolic(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([1 / independent_variable[i], 1])
    solution = solve(independent_matrix, dependent_matrix, precision)
    equation = hyperbolic_equation(*solution)
    derivative = hyperbolic_derivative(*solution)
    integral = hyperbolic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('hyperbolic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value, precision)
    accumulated_iqr = accumulation(integral, q1, q3, precision)
    averages_range = average_values('hyperbolic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('hyperbolic', equation, integral, q1, q3, solution, precision)
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted, precision)
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
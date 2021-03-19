from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.vectors.unify import unify
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.hyperbolic import hyperbolic as hyperbolic_equation
from library.analyses.roots.hyperbolic import hyperbolic as hyperbolic_roots
from library.analyses.derivatives.hyperbolic import hyperbolic as hyperbolic_derivative
from library.analyses.integrals.hyperbolic import hyperbolic as hyperbolic_integral
from library.analyses.extrema import extrema as extrema_independent
from library.analyses.inflections import inflections as inflections_independent
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.maximum import maximum
from library.statistics.minimum import minimum
from library.statistics.quartiles import quartiles
from library.statistics.correlation import correlation

def hyperbolic(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([1 / data[i][0], 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    equation = lambda x: solution[0][0]*(1/x) + solution[1][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        'error': inaccuracy
    }
    return result
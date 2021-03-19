from math import log, exp
from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.vectors.unify import unify
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.roots.exponential import exponential as exponential_roots
from library.analyses.derivatives.exponential import exponential as exponential_derivative
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.extrema import extrema as extrema_independent
from library.analyses.inflections import inflections as inflections_independent
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.maximum import maximum
from library.statistics.minimum import minimum
from library.statistics.quartiles import quartiles
from library.statistics.correlation import correlation

def exponential(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([data[i][0], 1])
        dependent_matrix.append([log(data[i][1])])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constants = [
        [exp(solution[1][0])],
        [exp(solution[0][0])]
    ]
    equation = lambda x: constants[0][0]*constants[1][0]**x
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
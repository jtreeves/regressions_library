from math import log
from numpy import matrix
from numpy.linalg import inv
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.vectors.unify import unify
from library.matrices.multiplication import multiplication
from library.matrices.transpose import transpose
from library.matrices.inverse import inverse
from library.analyses.equations.logarithmic import logarithmic as logarithmic_equation
from library.analyses.roots.logarithmic import logarithmic as logarithmic_roots
from library.analyses.derivatives.logarithmic import logarithmic as logarithmic_derivative
from library.analyses.integrals.logarithmic import logarithmic as logarithmic_integral
from library.analyses.extrema import extrema as extrema_independent
from library.analyses.inflections import inflections as inflections_independent
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.maximum import maximum
from library.statistics.minimum import minimum
from library.statistics.quartiles import quartiles
from library.statistics.correlation import correlation

def logarithmic(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([log(data[i][0]), 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constants = [
        [solution[1][0]],
        [solution[0][0]]
    ]
    equation = lambda x: constants[0][0] + constants[1][0]*log(x)
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result
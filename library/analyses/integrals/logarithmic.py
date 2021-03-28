from math import log
from library.errors.scalars import two_scalars

def logarithmic_integral(first_constant, second_constant):
    two_scalars(first_constant, second_constant)
    constants = [first_constant, second_constant]
    def logarithmic_evaluation(variable):
        evaluation = constants[0] * variable * (log(variable) - 1) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results
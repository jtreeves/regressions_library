from math import log
from library.errors.scalars import two_scalars

def hyperbolic_integral(first_constant, second_constant):
    two_scalars(first_constant, second_constant)
    constants = [first_constant, second_constant]
    def hyperbolic_evaluation(variable):
        evaluation = constants[0] * log(abs(variable)) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': hyperbolic_evaluation
    }
    return results
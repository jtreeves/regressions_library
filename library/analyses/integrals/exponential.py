from math import log
from library.errors.scalars import two_scalars

def exponential_integral(first_constant, second_constant):
    two_scalars(first_constant, second_constant)
    constants = [first_constant / log(second_constant), second_constant]
    def exponential_evaluation(variable):
        evaluation = constants[0] * constants[1]**variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': exponential_evaluation
    }
    return results
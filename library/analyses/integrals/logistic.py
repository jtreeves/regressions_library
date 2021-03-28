from math import exp, log
from library.errors.scalars import three_scalars

def logistic_integral(first_constant, second_constant, third_constant):
    three_scalars(first_constant, second_constant, third_constant)
    constants = [first_constant / second_constant, second_constant, third_constant]
    def logistic_evaluation(variable):
        evaluation = constants[0] * log(abs(exp(constants[1] * (variable - constants[2])) + 1))
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logistic_evaluation
    }
    return results
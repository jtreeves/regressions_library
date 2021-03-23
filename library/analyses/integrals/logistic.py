from math import exp
from math import log

def logistic(first_constant, second_constant, third_constant):
    constants = [first_constant / second_constant, second_constant, third_constant]
    def logistic_integral(variable):
        evaluation = constants[0] * log(abs(exp(constants[1] * (variable - constants[2])) + 1))
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logistic_integral
    }
    return results
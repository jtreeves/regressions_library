from math import log

def exponential(first_constant, second_constant):
    constants = [first_constant / log(second_constant), second_constant]
    def exponential_integral(variable):
        evaluation = constants[0] * constants[1]**variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': exponential_integral
    }
    return results
from math import log

def exponential_integral(first_constant, second_constant):
    constants = [first_constant / log(second_constant), second_constant]
    def exponential_evaluation(variable):
        evaluation = constants[0] * constants[1]**variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': exponential_evaluation
    }
    return results
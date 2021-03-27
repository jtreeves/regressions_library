from math import log

def logarithmic_integral(first_constant, second_constant):
    constants = [first_constant, second_constant]
    def logarithmic_evaluation(variable):
        evaluation = constants[0] * variable * (log(variable) - 1) + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results
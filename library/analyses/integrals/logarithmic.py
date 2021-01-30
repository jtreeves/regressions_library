from math import log

def logarithmic(first_constant, second_constant):
    constants = [first_constant, second_constant]
    def logarithmic_integral(variable):
        evaluation = constants[0] * variable + constants[1] * variable * (log(variable) - 1)
        return evaluation
    results = {
        'constants': constants,
        'evaluation': logarithmic_integral
    }
    return results
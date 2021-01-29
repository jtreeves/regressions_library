from math import log

def logarithmic(first_constant, second_constant):
    def logarithmic_integral(variable):
        evaluation = first_constant * variable + second_constant * variable * (log(variable) - 1)
        return evaluation
    return logarithmic_integral
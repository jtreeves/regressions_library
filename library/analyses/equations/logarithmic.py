from math import log

def logarithmic(first_constant, second_constant):
    def logarithmic_equation(variable):
        evaluation = first_constant + second_constant * log(variable)
        return evaluation
    return logarithmic_equation
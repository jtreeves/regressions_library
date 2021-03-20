from math import log

def logarithmic(first_constant, second_constant):
    def logarithmic_equation(variable):
        evaluation = first_constant * log(variable) + second_constant 
        return evaluation
    return logarithmic_equation
from math import log

def logarithmic_equation(first_constant, second_constant):
    def logarithmic_evaluation(variable):
        result = first_constant * log(variable) + second_constant 
        return result
    return logarithmic_evaluation
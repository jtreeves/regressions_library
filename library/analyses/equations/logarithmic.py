from math import log
from library.errors.scalars import two_scalars

def logarithmic_equation(first_constant, second_constant):
    two_scalars(first_constant, second_constant)
    def logarithmic_evaluation(variable):
        result = first_constant * log(variable) + second_constant 
        return result
    return logarithmic_evaluation
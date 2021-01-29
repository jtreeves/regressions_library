from math import log

def exponential(first_constant, second_constant):
    def exponential_equation(variable):
        evaluation = first_constant * second_constant**variable * log(second_constant)
        return evaluation
    return exponential_equation
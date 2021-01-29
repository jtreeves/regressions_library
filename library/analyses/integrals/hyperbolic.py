from math import log

def hyperbolic(first_constant, second_constant):
    def hyperbolic_integral(variable):
        evaluation = first_constant * log(variable) + second_constant * variable
        return evaluation
    return hyperbolic_integral
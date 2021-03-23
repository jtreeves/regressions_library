from math import exp

def logistic(first_constant, second_constant, third_constant):
    def logistic_equation(variable):
        evaluation = first_constant * (1 + exp(-1 * second_constant * (variable - third_constant)))**(-1)
        return evaluation
    return logistic_equation
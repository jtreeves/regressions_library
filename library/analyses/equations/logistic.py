from math import exp

def logistic_equation(first_constant, second_constant, third_constant):
    def logistic_evaluation(variable):
        result = first_constant * (1 + exp(-1 * second_constant * (variable - third_constant)))**(-1)
        return result
    return logistic_evaluation
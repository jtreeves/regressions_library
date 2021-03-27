from math import sin

def sinusoidal_equation(first_constant, second_constant, third_constant, fourth_constant):
    def sinusoidal_evaluation(variable):
        result = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return result
    return sinusoidal_evaluation
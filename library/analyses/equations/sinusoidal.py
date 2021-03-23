from math import sin

def sinusoidal(first_constant, second_constant, third_constant, fourth_constant):
    def sinusoidal_equation(variable):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    return sinusoidal_equation
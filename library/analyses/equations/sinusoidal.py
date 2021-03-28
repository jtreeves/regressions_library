from math import sin
from library.errors.scalars import four_scalars

def sinusoidal_equation(first_constant, second_constant, third_constant, fourth_constant):
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    def sinusoidal_evaluation(variable):
        result = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return result
    return sinusoidal_evaluation
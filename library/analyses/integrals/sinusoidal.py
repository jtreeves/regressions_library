from math import cos

def sinusoidal(first_constant, second_constant, third_constant, fourth_constant):
    constants = [-1 * first_constant / second_constant, second_constant, third_constant, fourth_constant]
    def sinusoidal_integral(variable):
        evaluation = constants[0] * cos(constants[1] * (variable - constants[2])) + constants[3] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': sinusoidal_integral
    }
    return results
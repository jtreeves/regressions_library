def cubic(first_constant, second_constant, third_constant, fourth_constant):
    constants = [(1/4) * first_constant, (1/3) * second_constant, (1/2) * third_constant, fourth_constant, 0]
    def cubic_integral(variable):
        evaluation = constants[0] * variable**4 + constants[1] * variable**3 + constants[2] * variable**2 + constants[3] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': cubic_integral
    }
    return results
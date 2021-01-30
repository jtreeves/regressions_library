def quadratic(first_constant, second_constant, third_constant):
    constants = [(1/3) * first_constant, (1/2) * second_constant, third_constant, 0]
    def quadratic_integral(variable):
        evaluation = constants[0] * variable**3 + constants[1] * variable**2 + constants[2] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': quadratic_integral
    }
    return results
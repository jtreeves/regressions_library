def linear(first_constant, second_constant):
    constants = [(1/2) * first_constant, second_constant, 0]
    def linear_integral(variable):
        evaluation = constants[0] * variable**2 + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': linear_integral
    }
    return results
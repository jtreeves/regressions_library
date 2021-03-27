def linear_integral(first_constant, second_constant):
    constants = [(1/2) * first_constant, second_constant]
    def linear_evaluation(variable):
        evaluation = constants[0] * variable**2 + constants[1] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': linear_evaluation
    }
    return results
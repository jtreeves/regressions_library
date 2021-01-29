def logarithmic(first_constant, second_constant):
    constants = [second_constant, 0]
    def logarithmic_derivative(variable):
        evaluation = constants[0] / variable
        return evaluation
    results = {
        'constants': constants,
        'derivative': logarithmic_derivative
    }
    return results
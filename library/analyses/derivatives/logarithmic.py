def logarithmic(second_constant):
    def logarithmic_derivative(variable):
        evaluation = second_constant / variable
        return evaluation
    return logarithmic_derivative
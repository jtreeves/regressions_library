def exponential(first_constant, second_constant):
    def exponential_equation(variable):
        evaluation = first_constant * second_constant**variable
        return evaluation
    return exponential_equation
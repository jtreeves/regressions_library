def linear_equation(first_constant, second_constant):
    def linear_evaluation(variable):
        result = first_constant * variable + second_constant
        return result
    return linear_evaluation
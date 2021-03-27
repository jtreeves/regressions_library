def quadratic_equation(first_constant, second_constant, third_constant):
    def quadratic_evaluation(variable):
        result = first_constant * variable**2 + second_constant * variable + third_constant
        return result
    return quadratic_evaluation
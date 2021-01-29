def quadratic(first_constant, second_constant, third_constant):
    def quadratic_equation(variable):
        evaluation = first_constant * variable**2 + second_constant * variable + third_constant
        return evaluation
    return quadratic_equation
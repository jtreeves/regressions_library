def linear(first_constant, second_constant):
    def linear_integral(variable):
        evaluation = (1/2) * first_constant * variable**2 + second_constant * variable
        return evaluation
    return linear_integral
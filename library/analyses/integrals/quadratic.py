def quadratic(first_constant, second_constant, third_constant):
    def quadratic_integral(variable):
        evaluation = (1/3) * first_constant * variable**3 + (1/2) * second_constant * variable**2 + third_constant * variable
        return evaluation
    return quadratic_integral
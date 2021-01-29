def cubic(first_constant, second_constant, third_constant, fourth_constant):
    def cubic_integral(variable):
        evaluation = (1/4) * first_constant * variable**4 + (1/3) * second_constant * variable**3 + (1/2) * third_constant * variable**2 + fourth_constant * variable
        return evaluation
    return cubic_integral
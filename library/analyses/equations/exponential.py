from library.errors.scalars import two_scalars

def exponential_equation(first_constant, second_constant):
    two_scalars(first_constant, second_constant)
    def exponential_evaluation(variable):
        result = first_constant * second_constant**variable
        return result
    return exponential_evaluation 
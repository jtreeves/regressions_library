from library.errors.scalars import three_scalars

def quadratic_integral(first_constant, second_constant, third_constant):
    three_scalars(first_constant, second_constant, third_constant)
    constants = [(1/3) * first_constant, (1/2) * second_constant, third_constant]
    def quadratic_evaluation(variable):
        evaluation = constants[0] * variable**3 + constants[1] * variable**2 + constants[2] * variable
        return evaluation
    results = {
        'constants': constants,
        'evaluation': quadratic_evaluation
    }
    return results
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .residuals import multiple_residuals
from .deviations import multiple_deviations
from .summation import sum_value
from .rounding import rounded_value

def correlation_coefficient(actuals, expecteds, precision):
    vector_of_scalars(actuals, 'first')
    vector_of_scalars(expecteds, 'second')
    positive_integer(precision)
    residual_array = multiple_residuals(actuals, expecteds)
    deviation_array = multiple_deviations(actuals)
    squared_residuals = []
    for i in range(len(residual_array)):
        squared_residuals.append(residual_array[i]**2)
    squared_deviations = []
    for i in range(len(deviation_array)):
        squared_deviations.append(deviation_array[i]**2)
    residual_sum = sum_value(squared_residuals)
    deviation_sum = sum_value(squared_deviations)
    ratio = residual_sum / deviation_sum
    if ratio >= 1:
        return 0.0
    else:
        result = (1 - ratio)**(1/2)
        return rounded_value(result, precision)
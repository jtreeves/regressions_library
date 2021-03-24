from .residuals import residuals
from .deviations import deviations
from .summation import summation
from .rounding import rounding

def correlation(actuals, expecteds, precision):
    residual_array = residuals(actuals, expecteds)
    deviation_array = deviations(actuals)
    squared_residuals = []
    for i in range(len(residual_array)):
        squared_residuals.append(residual_array[i]**2)
    squared_deviations = []
    for i in range(len(deviation_array)):
        squared_deviations.append(deviation_array[i]**2)
    residual_sum = summation(squared_residuals)
    deviation_sum = summation(squared_deviations)
    ratio = residual_sum / deviation_sum
    if ratio >= 1:
        return 0.0
    else:
        result = (1 - ratio)**(1/2)
        return rounding(result, precision)
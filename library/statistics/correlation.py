from .residuals import residuals
from .deviations import deviations
from .summation import summation

def correlation(actuals, expecteds):
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
    result = (1 - residual_sum / deviation_sum)**(1/2)
    if not isinstance(result, complex):
        return result
    else:
        return 0.0
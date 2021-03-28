from library.errors.scalars import first_scalar, last_scalar
from library.errors.vectors import first_vector
from .mean import mean_value

def single_deviation(actual, mean): 
    first_scalar(actual)
    last_scalar(mean)
    result = actual - mean
    return result

def multiple_deviations(actual_array):
    first_vector(actual_array)
    results = []
    average = mean_value(actual_array)
    for i in range(len(actual_array)):
        results.append(single_deviation(actual_array[i], average))
    return results
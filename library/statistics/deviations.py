from library.errors.scalars import scalar_value
from library.errors.vectors import vector_of_scalars
from .mean import mean_value

def single_deviation(actual, mean): 
    scalar_value(actual, 'first')
    scalar_value(mean, 'second')
    result = actual - mean
    return result

def multiple_deviations(actual_array):
    vector_of_scalars(actual_array, 'only')
    results = []
    average = mean_value(actual_array)
    for element in actual_array:
        results.append(single_deviation(element, average))
    return results
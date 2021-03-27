from .mean import mean_value

def single_deviation(actual, mean): 
    result = actual - mean
    return result

def multiple_deviations(actual_array):
    results = []
    average = mean_value(actual_array)
    for i in range(len(actual_array)):
        results.append(single_deviation(actual_array[i], average))
    return results
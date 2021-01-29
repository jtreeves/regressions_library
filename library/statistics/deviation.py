from .mean import mean

def deviation(actual, mean): 
    result = actual - mean
    return result

def deviation_array(actual_array):
    results = []
    average = mean(actual_array)
    for i in range(len(actual_array)):
        results.append(deviation(actual_array[i], average))
    return results
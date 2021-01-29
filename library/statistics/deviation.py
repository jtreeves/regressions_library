def deviation(actual, mean): 
    result = actual - mean
    return result

def deviation_array(actual_array, expected_array):
    results = []
    for i in range(len(actual_array)):
        results.append(deviation(actual_array[i], expected_array[i]))
    return results
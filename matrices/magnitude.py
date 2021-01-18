def magnitude(vector):
    summation = 0
    for i in range(len(vector)):
        summation += vector[i][0]**2
    result = summation**(1/2)
    return result
def dimension(sequence, level):
    result = []
    for i in range(len(sequence)):
        result.append(sequence[i][level - 1])
    return result
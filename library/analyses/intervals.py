def intervals(equation, points):
    result = []
    if points[0] == None:
        if equation(10) > 0:
            result = ['increasing']
        elif equation(10) < 0:
            result = ['decreasing']
        else:
            result = ['constant']
    elif len(points) == 1:
        turning_point = points[0]
        before = turning_point - 1
        after = turning_point + 1
        if equation(before) > 0:
            before = 'increasing'
        elif equation(before) < 0:
            before = 'decreasing'
        if equation(after) > 0 :
            after = 'increasing'
        elif equation(after) < 0:
            after = 'decreasing'
        result = [before, turning_point, after]
    elif len(points) == 2:
        first_point = points[0]
        second_point = points[1]
        middle = (first_point + second_point) / 2
        if first_point > second_point:
            first_point = second_point
        before = first_point - 1
        after = second_point + 1
        if equation(before) > 0:
            before = 'increasing'
        elif equation(before) < 0:
            before = 'decreasing'
        if equation(middle) > 0 :
            middle = 'increasing'
        elif equation(middle) < 0:
            middle = 'decreasing'
        if equation(after) > 0:
            after = 'increasing'
        elif equation(after) < 0:
            after = 'decreasing'
        result = [before, first_point, middle, second_point, after]
    return result
def intervals(equation, points):
    result = []
    if points[0] == None:
        if equation(10) > 0:
            result = ['increasing everywhere']
        elif equation(10) < 0:
            result = ['decreasing everywhere']
        else:
            result = ['constant everywhere']
    elif len(points) == 1:
        turning_point = points[0]
        before = turning_point - 1
        after = turning_point + 1
        if equation(before) > 0:
            before = f'increasing up until {turning_point}'
        elif equation(before) < 0:
            before = f'decreaseing up until {turning_point}'
        if equation(after) > 0 :
            after = f'increasing from {turning_point} to infinity'
        elif equation(after) < 0:
            after = f'decreasing from {turning_point} to infinity'
        result = [before, after]
    elif len(points) == 2:
        first_point = points[0]
        second_point = points[1]
        middle = (first_point + second_point) / 2
        if first_point > second_point:
            first_point = second_point
        before = first_point - 1
        after = second_point + 1
        if equation(before) > 0:
            before = f'increasing up until {first_point}'
        elif equation(before) < 0:
            before = f'decreasing up until {first_point}'
        if equation(middle) > 0 :
            middle = f'increasing between {first_point} and {second_point}'
        elif equation(middle) < 0:
            middle = f'decreasing between {first_point} and {second_point}'
        if equation(after) > 0:
            after = f'increasing after {second_point}'
        elif equation(after) < 0:
            after = f'decreasing after {second_point}'
        result = [before, middle, after]
    return result
        
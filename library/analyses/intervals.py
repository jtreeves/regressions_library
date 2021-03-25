from library.statistics.sort import sort

def intervals(derivative, points):
    result = []
    if points[0] == None:
        if derivative(10) > 0:
            result = ['positive']
        elif derivative(10) < 0:
            result = ['negative']
        else:
            result = ['constant']
    elif len(points) == 1:
        turning_point = points[0]
        before = turning_point - 1
        after = turning_point + 1
        if derivative(before) > 0:
            before = 'positive'
        elif derivative(before) < 0:
            before = 'negative'
        if derivative(after) > 0 :
            after = 'positive'
        elif derivative(after) < 0:
            after = 'negative'
        result = [before, turning_point, after]
    elif len(points) == 2:
        sorted_points = sort(points)
        first_point = sorted_points[0]
        second_point = sorted_points[1]
        middle = (first_point + second_point) / 2
        before = first_point - 1
        after = second_point + 1
        if derivative(before) > 0:
            before = 'positive'
        elif derivative(before) < 0:
            before = 'negative'
        if derivative(middle) > 0 :
            middle = 'positive'
        elif derivative(middle) < 0:
            middle = 'negative'
        if derivative(after) > 0:
            after = 'positive'
        elif derivative(after) < 0:
            after = 'negative'
        result = [before, first_point, middle, second_point, after]
    else:
        numerical_points = []
        for item in points:
            if isinstance(item, (int, float)):
                numerical_points.append(item)
        sorted_points = sort(numerical_points)
        difference = sorted_points[1] - sorted_points[0]
        halved_difference = difference / 2
        detailed_points = {}
        for point in sorted_points:
            detailed_points[point] = {}
            before_point = point - halved_difference
            after_point = point + halved_difference
            if derivative(before_point) > 0:
                before_point = 'positive'
            elif derivative(before_point) < 0:
                before_point = 'negative'
            if derivative(after_point) > 0:
                after_point = 'positive'
            elif derivative(after_point) < 0:
                after_point = 'negative'
            detailed_points[point]['point'] = point
            detailed_points[point]['before'] = before_point
            detailed_points[point]['after'] = after_point
        return
    return result
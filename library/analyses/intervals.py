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
        other_points = []
        for item in points:
            if isinstance(item, (int, float)):
                numerical_points.append(item)
            else:
                other_points.append(item)
        sorted_points = sort(numerical_points)
        difference = sorted_points[1] - sorted_points[0]
        halved_difference = difference / 2
        before_first = sorted_points[0] - halved_difference
        between_first_second = sorted_points[0] + halved_difference
        between_second_third = sorted_points[1] + halved_difference
        between_third_fourth = sorted_points[2] + halved_difference
        between_fourth_last = sorted_points[3] + halved_difference
        after_last = sorted_points[4] + halved_difference
        test_points = [before_first, between_first_second, between_second_third, between_third_fourth, between_fourth_last, after_last]
        for point in test_points:
            if derivative(point) > 0:
                point = 'positive'
            elif derivative(point) < 0:
                point = 'negative'
        result = [before_first, sorted_points[0], between_first_second, sorted_points[1], between_second_third, sorted_points[2], between_third_fourth, sorted_points[3], between_fourth_last, sorted_points[4], after_last, *other_points]
    return result
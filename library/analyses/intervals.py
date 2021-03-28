from library.statistics.sort import sorted_list
from library.errors.analyses import callable_function
from library.errors.vectors import allow_none_vector

def sign_chart(derivative, points):
    callable_function(derivative, 'first')
    allow_none_vector(points, 'second')
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
        sorted_points = sorted_list(points)
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
        sorted_points = sorted_list(numerical_points)
        difference = sorted_points[1] - sorted_points[0]
        halved_difference = difference / 2
        before_first = sorted_points[0] - halved_difference
        between_first_second = sorted_points[0] + halved_difference
        between_second_third = sorted_points[1] + halved_difference
        between_third_fourth = sorted_points[2] + halved_difference
        between_fourth_last = sorted_points[3] + halved_difference
        after_last = sorted_points[4] + halved_difference
        test_points = [before_first, between_first_second, between_second_third, between_third_fourth, between_fourth_last, after_last]
        sign_chart = []
        for point in test_points:
            if derivative(point) > 0:
                sign_chart.append('positive')
            elif derivative(point) < 0:
                sign_chart.append('negative')
        result = [sign_chart[0], sorted_points[0], sign_chart[1], sorted_points[1], sign_chart[2], sorted_points[2], sign_chart[3], sorted_points[3], sign_chart[4], sorted_points[4], sign_chart[5], *other_points]
    return result
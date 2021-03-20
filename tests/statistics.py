from library.statistics.summation import summation
from library.statistics.sort import sort
from library.statistics.minimum import minimum
from library.statistics.maximum import maximum
from library.statistics.quartiles import quartiles
from library.statistics.median import median
from library.statistics.mean import mean
from library.statistics.five_number_summary import five_number_summary
from library.statistics.ranges import ranges
from library.statistics.deviations import deviations
from library.statistics.residuals import residuals
from library.statistics.correlation import correlation

first_set = [8, 2, 5, 9, 1, 3, 22, 11, 9, 13]
second_set = [7, 4, 6, 8, 2, 5, 21, 14, 8, 13]

sum_first = summation(first_set)
sum_second = summation(second_set)

sort_first = sort(first_set)
sort_second = sort(second_set)

min_first = minimum(first_set)
min_second = minimum(second_set)

max_first = maximum(first_set)
max_second = maximum(second_set)

q1_first = quartiles(first_set, 1)
q1_second = quartiles(second_set, 1)

q3_first = quartiles(first_set, 3)
q3_second = quartiles(second_set, 3)

median_first = median(first_set)
median_second = median(second_set)

mean_first = mean(first_set)
mean_second = mean(second_set)

five_first = five_number_summary(first_set)
five_second = five_number_summary(second_set)

range_first = ranges(first_set)
range_second = ranges(second_set)

deviations_first = deviations(first_set)
deviations_second = deviations(second_set)

residuals_compare = residuals(first_set, second_set)

correlation_compare = correlation(first_set, second_set)

print(f'SUM FIRST: {sum_first}') # 83
print(f'SUM SECOND: {sum_second}') # 88

print(f'SORT FIRST: {sort_first}') # [1, 2, 3, 5, 8, 9, 9, 11, 13, 22]
print(f'SORT SECOND: {sort_second}') # [2, 4, 5, 6, 7, 8, 8, 13, 14, 21]

print(f'MIN FIRST: {min_first}') # 1
print(f'MIN SECOND: {min_second}') # 2

print(f'MAX FIRST: {max_first}') # 22
print(f'MAX SECOND: {max_second}') # 21

print(f'Q1 FIRST: {q1_first}') # 6.5
print(f'Q1 SECOND: {q1_second}') # 6.5

print(f'Q3 FIRST: {q3_first}') # 11
print(f'Q3 SECOND: {q3_second}') # 13

print(f'MEDIAN FIRST: {median_first}') # 8.5
print(f'MEDIAN SECOND: {median_second}') # 7.5

print(f'MEAN FIRST: {mean_first}') # 8.3
print(f'MEAN SECOND: {mean_second}') # 8.8

print(f'FIVE NUMBERS FIRST: {five_first}') # {'minimum': 1, 'q1': 6.5, 'median': 8.5, 'q3': 11, 'maximum': 22}
print(f'FIVE NUMBERS SECOND: {five_second}') # {'minimum': 2, 'q1': 6.5, 'median': 7.5, 'q3': 13, 'maximum': 21}

print(f'RANGE FIRST: {range_first}') # 21
print(f'RANGE SECOND: {range_second}') # 19

print(f'DEVIATIONS FIRST: {deviations_first}') # [-0.3000000000000007, -6.300000000000001, -3.3000000000000007, 0.6999999999999993, -7.300000000000001, -5.300000000000001, 13.7, 2.6999999999999993, 0.6999999999999993, 4.699999999999999]
print(f'DEVIATIONS SECOND: {deviations_second}') # [-1.8000000000000007, -4.800000000000001, -2.8000000000000007, -0.8000000000000007, -6.800000000000001, -3.8000000000000007, 12.2, 5.199999999999999, -0.8000000000000007, 4.199999999999999]

print(f'RESIDUALS COMPARE: {residuals_compare}') # [1, -2, -1, 1, -1, -2, 1, -3, 1, 0]

print(f'CORRELATION COMPARE: {correlation_compare}') # 0.9665942708463666
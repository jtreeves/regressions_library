from library.statistics.rounding import rounding
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

even_set = [8, 2, 5, 9, 1, 3, 22, 11, 9, 13]
odd_set = [7, 4, 6, 8, 2, 5, 25, 14, 8]
compare_set = [5, 5, 5, 10, 1, 7, 22, 13, 8]

normal_decimal = 6.817239833721
extreme_decimal = 0.000000000000000000005782016894

precision = 4
high_precision = 8

round_normal = rounding(normal_decimal, precision)
round_normal_high = rounding(normal_decimal, high_precision)
round_extreme = rounding(extreme_decimal, precision)
round_extreme_high = rounding(extreme_decimal, high_precision)

sum_even = summation(even_set)
sum_odd = summation(odd_set)

sort_even = sort(even_set)
sort_odd = sort(odd_set)

min_even = minimum(even_set)
min_odd = minimum(odd_set)

max_even = maximum(even_set)
max_odd = maximum(odd_set)

q1_even = quartiles(even_set, 1)
q1_odd = quartiles(odd_set, 1)

q3_even = quartiles(even_set, 3)
q3_odd = quartiles(odd_set, 3)

median_even = median(even_set)
median_odd = median(odd_set)

mean_even = mean(even_set)
mean_odd = mean(odd_set)

five_even = five_number_summary(even_set, precision)
five_odd = five_number_summary(odd_set, precision)

range_even = ranges(even_set)
range_odd = ranges(odd_set)

deviations_even = deviations(even_set)
deviations_odd = deviations(odd_set)

residuals_compare = residuals(odd_set, compare_set)

correlation_compare = correlation(odd_set, compare_set, precision)

print(f'ROUND NORMAL: {round_normal}')
print(f'ROUND NORMAL HIGH: {round_normal_high}')
print(f'ROUND EXTREME: {round_extreme}')
print(f'ROUND EXTREME HIGH: {round_extreme_high}')

print(f'SUM EVEN: {sum_even}') # 83
print(f'SUM ODD: {sum_odd}') # 79

print(f'SORT EVEN: {sort_even}') # [1, 2, 3, 5, 8, 9, 9, 11, 13, 22]
print(f'SORT ODD: {sort_odd}') # [2, 4, 5, 6, 7, 8, 8, 14, 25]

print(f'MIN EVEN: {min_even}') # 1
print(f'MIN ODD: {min_odd}') # 2

print(f'MAX EVEN: {max_even}') # 22
print(f'MAX ODD: {max_odd}') # 25

print(f'Q1 EVEN: {q1_even}') # 3
print(f'Q1 ODD: {q1_odd}') # 4.5

print(f'Q3 EVEN: {q3_even}') # 11
print(f'Q3 ODD: {q3_odd}') # 11.0

print(f'MEDIAN EVEN: {median_even}') # 8.5
print(f'MEDIAN ODD: {median_odd}') # 7

print(f'MEAN EVEN: {mean_even}') # 8.3
print(f'MEAN ODD: {mean_odd}') # 8.777777777777779

print(f'FIVE NUMBERS EVEN: {five_even}') # {'minimum': 1, 'q1': 3, 'median': 8.5, 'q3': 11, 'maximum': 22}
print(f'FIVE NUMBERS ODD: {five_odd}') # {'minimum': 2, 'q1': 4.5, 'median': 7, 'q3': 11.0, 'maximum': 25}

print(f'RANGE EVEN: {range_even}') # 21
print(f'RANGE ODD: {range_odd}') # 23

print(f'DEVIATIONS EVEN: {deviations_even}') # [-0.3000000000000007, -6.300000000000001, -3.3000000000000007, 0.6999999999999993, -7.300000000000001, -5.300000000000001, 13.7, 2.6999999999999993, 0.6999999999999993, 4.699999999999999]
print(f'DEVIATIONS ODD: {deviations_odd}') # [-1.7777777777777786, -4.777777777777779, -2.7777777777777786, -0.7777777777777786, -6.777777777777779, -3.7777777777777786, 16.22222222222222, 5.222222222222221, -0.7777777777777786]

print(f'RESIDUALS COMPARE: {residuals_compare}') # [2, -1, 1, -2, 1, -2, 3, 1, 0]

print(f'CORRELATION COMPARE: {correlation_compare}') # 0.9670359359614937
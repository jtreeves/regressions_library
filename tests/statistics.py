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

print(f'SUM FIRST: {sum_first}')
print(f'SUM SECOND: {sum_second}')

print(f'SORT FIRST: {sort_first}')
print(f'SORT SECOND: {sort_second}')

print(f'MIN FIRST: {min_first}')
print(f'MIN SECOND: {min_second}')

print(f'MAX FIRST: {max_first}')
print(f'MAX SECOND: {max_second}')

print(f'Q1 FIRST: {q1_first}')
print(f'Q1 SECOND: {q1_second}')

print(f'Q3 FIRST: {q3_first}')
print(f'Q3 SECOND: {q3_second}')

print(f'MEDIAN FIRST: {median_first}')
print(f'MEDIAN SECOND: {median_second}')

print(f'MEAN FIRST: {mean_first}')
print(f'MEAN SECOND: {mean_second}')

print(f'FIVE NUMBERS FIRST: {five_first}')
print(f'FIVE NUMBERS SECOND: {five_second}')

print(f'RANGE FIRST: {range_first}')
print(f'RANGE SECOND: {range_second}')

print(f'DEVIATIONS FIRST: {deviations_first}')
print(f'DEVIATIONS SECOND: {deviations_second}')

print(f'RESIDUALS COMPARE: {residuals_compare}')

print(f'CORRELATION COMPARE: {correlation_compare}')
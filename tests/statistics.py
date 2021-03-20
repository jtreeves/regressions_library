from library.statistics.summation import summation
from library.statistics.sort import sort
from library.statistics.minimum import minimum
from library.statistics.maximum import maximum
from library.statistics.quartiles import quartiles
from library.statistics.median import median
from library.statistics.mean import mean
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

ranges_first = ranges(first_set)
ranges_second = ranges(second_set)

deviations_first = deviations(first_set)
deviations_second = deviations(second_set)

residuals_compare = residuals(first_set, second_set)

correlation_compare = correlation(first_set, second_set)

datsort = sort(first_set)
datmax = maximum(first_set)
datmin = minimum(first_set)
datran = ranges(first_set)
datsum = summation(first_set)
datmean = mean(first_set)
datmed = median(first_set)
datq = quartiles(first_set, 3)
datres = residuals(first_set, second_set)
datdev = deviations(first_set)
datcorr = correlation(first_set, second_set)

print(f'DATSORT: {datsort}') # => [1, 2, 3, 5, 8, 9, 9, 11, 13, 22]
print(f'DATMAX: {datmax}') # => 22
print(f'DATMIN: {datmin}') # => 1
print(f'DATRAN: {datran}') # => 21
print(f'DATSUM: {datsum}') # => 83
print(f'DATMEAN: {datmean}') # => 8.3
print(f'DATMED: {datmed}') # => 8.5
print(f'DATQ: {datq}') # => 11
print(f'DATRES: {datres}') # => [1, 1, -1, 1, -1, -2, 1, -3, 1, 0]
print(f'DATDEV: {datdev}') # => [-0.3000000000000007, -6.300000000000001, -3.3000000000000007, 0.6999999999999993, -7.300000000000001, -5.300000000000001, 13.7, 2.6999999999999993, 0.6999999999999993, 4.699999999999999]
print(f'DATCORR: {datcorr}') # => 0.9710167170159144
from library.statistics.sort import sort
from library.statistics.minimum import minimum
from library.statistics.maximum import maximum
from library.statistics.median import median
from library.statistics.quartiles import quartiles
from library.statistics.summation import summation
from library.statistics.mean import mean
from library.statistics.ranges import ranges
from library.statistics.residuals import residuals
from library.statistics.deviations import deviations
from library.statistics.correlation import correlation

dat1 = [8, 2, 5, 9, 1, 3, 22, 11, 9, 13]
dat2 = [7, 1, 6, 8, 2, 5, 21, 14, 8, 13]

datsort = sort(dat1)
datmax = maximum(dat1)
datmin = minimum(dat1)
datran = ranges(dat1)
datsum = summation(dat1)
datmean = mean(dat1)
datmed = median(dat1)
datq = quartiles(dat1, 3)
datres = residuals(dat1, dat2)
datdev = deviations(dat1)
datcorr = correlation(dat1, dat2)

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
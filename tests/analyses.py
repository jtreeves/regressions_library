from library.analyses.equations.linear import linear as lineq
from library.analyses.equations.quadratic import quadratic as quadeq
from library.analyses.equations.cubic import cubic as cubeq
from library.analyses.equations.hyperbolic import hyperbolic as hypeq
from library.analyses.equations.exponential import exponential as expeq
from library.analyses.equations.logarithmic import logarithmic as logeq
from library.analyses.roots.linear import linear as linroot
from library.analyses.roots.quadratic import quadratic as quadroot
from library.analyses.roots.cubic import cubic as cubroot
from library.analyses.roots.hyperbolic import hyperbolic as hyproot
from library.analyses.roots.exponential import exponential as exproot
from library.analyses.roots.logarithmic import logarithmic as logroot
from library.analyses.derivatives.linear import linear as linder
from library.analyses.derivatives.quadratic import quadratic as quader
from library.analyses.derivatives.cubic import cubic as cubder
from library.analyses.derivatives.hyperbolic import hyperbolic as hypder
from library.analyses.derivatives.exponential import exponential as expder
from library.analyses.derivatives.logarithmic import logarithmic as logder
from library.analyses.integrals.linear import linear as linint
from library.analyses.integrals.quadratic import quadratic as quadint
from library.analyses.integrals.cubic import cubic as cubint
from library.analyses.integrals.hyperbolic import hyperbolic as hypint
from library.analyses.integrals.exponential import exponential as expint
from library.analyses.integrals.logarithmic import logarithmic as logint
from library.analyses.accumulation import accumulation
from library.analyses.critical_points import critical_points
from library.analyses.critical_values import critical_values
from library.analyses.decreasing import decreasing
from library.analyses.extrema import extrema
from library.analyses.increasing import increasing
from library.analyses.inflections import inflections
from library.analyses.intervals import intervals
from library.analyses.maxima import maxima
from library.analyses.mean_values import mean_value_derivative, mean_value_integral
from library.analyses.minima import minima

coefficients = [2, 3, 5, 7]

test_lineq = lineq(coefficients[0], coefficients[1])
test_quadeq = quadeq(coefficients[0], coefficients[1], coefficients[2])
test_cubeq = cubeq(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hypeq = hypeq(coefficients[0], coefficients[1])
test_expeq = expeq(coefficients[0], coefficients[1])
test_logeq = logeq(coefficients[0], coefficients[1])

test_linroot = linroot(coefficients[0], coefficients[1])
test_quadroot = quadroot(coefficients[0], coefficients[1], coefficients[2])
test_cubroot = cubroot(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hyproot = hyproot(coefficients[0], coefficients[1])
test_exproot = exproot(coefficients[0], coefficients[1])
test_logroot = logroot(coefficients[0], coefficients[1])

test_linev = test_lineq(4)
test_quadev = test_quadeq(4)
test_cubev = test_cubeq(4)
test_hypev = test_hypeq(4)
test_expev = test_expeq(4)
test_logev = test_logeq(4)

test_linroot_arr = test_linroot
test_quadroot_arr = test_quadroot
test_cubroot_arr = test_cubroot
test_hyproot_arr = test_hyproot
test_exproot_arr = test_exproot
test_logroot_arr = test_logroot

print(f'TEST_LINEV: {test_linev}') # => 11
print(f'TEST_QUADEV: {test_quadev}') # => 49
print(f'TEST_CUBEV: {test_cubev}') # => 203
print(f'TEST_HYPEV: {test_hypev}') # => 3.5
print(f'TEST_EXPEV: {test_expev}') # => 162
print(f'TEST_LOGEV: {test_logev}') # => 6.1588830833596715

print(f'TEST_LINROOT_ARR: {test_linroot_arr}') # => [-1.5]
print(f'TEST_QUADROOT_ARR: {test_quadroot_arr}') # => [(-0.7499999999999999+1.3919410907075054j), (-0.7500000000000001-1.3919410907075054j)]
print(f'TEST_CUBROOT_ARR: {test_cubroot_arr}') # => [None]
print(f'TEST_HYPROOT_ARR: {test_hyproot_arr}') # => [-0.6666666666666666]
print(f'TEST_EXPROOT_ARR: {test_exproot_arr}') # => [None]
print(f'TEST_LOGROOT_ARR: {test_logroot_arr}') # => [0.513417119032592]
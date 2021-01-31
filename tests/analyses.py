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
from library.vectors.unify import unify

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

test_linder = linder(coefficients[0], coefficients[1])
test_quader = quader(coefficients[0], coefficients[1], coefficients[2])
test_cubder = cubder(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hypder = hypder(coefficients[0], coefficients[1])
test_expder = expder(coefficients[0], coefficients[1])
test_logder = logder(coefficients[0], coefficients[1])

test_linint = linint(coefficients[0], coefficients[1])
test_quadint = quadint(coefficients[0], coefficients[1], coefficients[2])
test_cubint = cubint(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hypint = hypint(coefficients[0], coefficients[1])
test_expint = expint(coefficients[0], coefficients[1])
test_logint = logint(coefficients[0], coefficients[1])

test_crit_lin1 = critical_points('linear', 1, coefficients)
test_crit_quad1 = critical_points('quadratic', 1, coefficients)
test_crit_cub1 = critical_points('cubic', 1, coefficients)
test_crit_hyp1 = critical_points('hyperbolic', 1, coefficients)
test_crit_exp1 = critical_points('exponential', 1, coefficients)
test_crit_log1 = critical_points('logarithmic', 1, coefficients)

test_crit_lin_val = critical_values('linear', test_crit_lin1, coefficients)
test_crit_quad_val = critical_values('quadratic', test_crit_quad1, coefficients)
test_crit_cub_val = critical_values('cubic', test_crit_cub1, coefficients)
test_crit_hyp_val = critical_values('hyperbolic', test_crit_hyp1, coefficients)
test_crit_exp_val = critical_values('exponential', test_crit_exp1, coefficients)
test_crit_log_val = critical_values('logarithmic', test_crit_log1, coefficients)

test_unify_lin = unify(test_crit_lin1, test_crit_lin_val)
test_unify_quad = unify(test_crit_quad1, test_crit_quad_val)
test_unify_cub = unify(test_crit_cub1, test_crit_cub_val)
test_unify_hyp = unify(test_crit_hyp1, test_crit_hyp_val)
test_unify_exp = unify(test_crit_exp1, test_crit_exp_val)
test_unify_log = unify(test_crit_log1, test_crit_log_val)

test_crit_lin2 = critical_points('linear', 2, coefficients)
test_crit_quad2 = critical_points('quadratic', 2, coefficients)
test_crit_cub2 = critical_points('cubic', 2, coefficients)
test_crit_hyp2 = critical_points('hyperbolic', 2, coefficients)
test_crit_exp2 = critical_points('exponential', 2, coefficients)
test_crit_log2 = critical_points('logarithmic', 2, coefficients)

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

test_linder_first = test_linder['first']
test_quader_first = test_quader['first']
test_cubder_first = test_cubder['first']
test_hypder_first = test_hypder['first']
test_expder_first = test_expder['first']
test_logder_first = test_logder['first']

test_linder_first_arr = test_linder['first']['constants']
test_quader_first_arr = test_quader['first']['constants']
test_cubder_first_arr = test_cubder['first']['constants']
test_hypder_first_arr = test_hypder['first']['constants']
test_expder_first_arr = test_expder['first']['constants']
test_logder_first_arr = test_logder['first']['constants']

test_linder_first_ev = test_linder['first']['evaluation'](4)
test_quader_first_ev = test_quader['first']['evaluation'](4)
test_cubder_first_ev = test_cubder['first']['evaluation'](4)
test_hypder_first_ev = test_hypder['first']['evaluation'](4)
test_expder_first_ev = test_expder['first']['evaluation'](4)
test_logder_first_ev = test_logder['first']['evaluation'](4)

test_linder_second = test_linder['second']
test_quader_second = test_quader['second']
test_cubder_second = test_cubder['second']
test_hypder_second = test_hypder['second']
test_expder_second = test_expder['second']
test_logder_second = test_logder['second']

test_linder_second_arr = test_linder['second']['constants']
test_quader_second_arr = test_quader['second']['constants']
test_cubder_second_arr = test_cubder['second']['constants']
test_hypder_second_arr = test_hypder['second']['constants']
test_expder_second_arr = test_expder['second']['constants']
test_logder_second_arr = test_logder['second']['constants']

test_linder_second_ev = test_linder['second']['evaluation'](4)
test_quader_second_ev = test_quader['second']['evaluation'](4)
test_cubder_second_ev = test_cubder['second']['evaluation'](4)
test_hypder_second_ev = test_hypder['second']['evaluation'](4)
test_expder_second_ev = test_expder['second']['evaluation'](4)
test_logder_second_ev = test_logder['second']['evaluation'](4)

test_linint_arr = test_linint['constants']
test_quadint_arr = test_quadint['constants']
test_cubint_arr = test_cubint['constants']
test_hypint_arr = test_hypint['constants']
test_expint_arr = test_expint['constants']
test_logint_arr = test_logint['constants']

test_linint_ev = test_linint['evaluation'](4)
test_quadint_ev = test_quadint['evaluation'](4)
test_cubint_ev = test_cubint['evaluation'](4)
test_hypint_ev = test_hypint['evaluation'](4)
test_expint_ev = test_expint['evaluation'](4)
test_logint_ev = test_logint['evaluation'](4)

test_linint_acc = accumulation(test_linint['evaluation'], 1, 10)
test_quadint_acc = accumulation(test_quadint['evaluation'], 1, 10)
test_cubint_acc = accumulation(test_cubint['evaluation'], 1, 10)
test_hypint_acc = accumulation(test_hypint['evaluation'], 1, 10)
test_expint_acc = accumulation(test_expint['evaluation'], 1, 10)
test_logint_acc = accumulation(test_logint['evaluation'], 1, 10)

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

print(f'TEST_LINDER_FIRST_ARR: {test_linder_first_arr}') # => [2]
print(f'TEST_QUADER_FIRST_ARR: {test_quader_first_arr}') # => [4, 3]
print(f'TEST_CUBDER_FIRST_ARR: {test_cubder_first_arr}') # => [6, 6, 5]
print(f'TEST_HYPDER_FIRST_ARR: {test_hypder_first_arr}') # => [-2]
print(f'TEST_EXPDER_FIRST_ARR: {test_expder_first_arr}') # => [2.1972245773362196, 3]
print(f'TEST_LOGDER_FIRST_ARR: {test_logder_first_arr}') # => [3, 0]

print(f'TEST_LINDER_FIRST_EV: {test_linder_first_ev}') # => 2
print(f'TEST_QUADER_FIRST_EV: {test_quader_first_ev}') # => 19
print(f'TEST_CUBDER_FIRST_EV: {test_cubder_first_ev}') # => 125
print(f'TEST_HYPDER_FIRST_EV: {test_hypder_first_ev}') # => -0.125
print(f'TEST_EXPDER_FIRST_EV: {test_expder_first_ev}') # => 177.9751907642338
print(f'TEST_LOGDER_FIRST_EV: {test_logder_first_ev}') # => 0.75

print(f'TEST_LINDER_SECOND_ARR: {test_linder_second_arr}') # => [0]
print(f'TEST_QUADER_SECOND_ARR: {test_quader_second_arr}') # => [4]
print(f'TEST_CUBDER_SECOND_ARR: {test_cubder_second_arr}') # => [12, 6]
print(f'TEST_HYPDER_SECOND_ARR: {test_hypder_second_arr}') # => [4]
print(f'TEST_EXPDER_SECOND_ARR: {test_expder_second_arr}') # => [2.413897921625164, 3]
print(f'TEST_LOGDER_SECOND_ARR: {test_logder_second_arr}') # => [-3, 0]

print(f'TEST_LINDER_SECOND_EV: {test_linder_second_ev}') # => 0
print(f'TEST_QUADER_SECOND_EV: {test_quader_second_ev}') # => 4
print(f'TEST_CUBDER_SECOND_EV: {test_cubder_second_ev}') # => 54
print(f'TEST_HYPDER_SECOND_EV: {test_hypder_second_ev}') # => 0.0625
print(f'TEST_EXPDER_SECOND_EV: {test_expder_second_ev}') # => 195.5257316516383
print(f'TEST_LOGDER_SECOND_EV: {test_logder_second_ev}') # => -0.1875

print(f'TEST_LININT_ARR: {test_linint_arr}') # => [1.0, 3]
print(f'TEST_QUADINT_ARR: {test_quadint_arr}') # => [0.6666666666666666, 1.5, 5]
print(f'TEST_CUBINT_ARR: {test_cubint_arr}') # => [0.5, 1.0, 2.5, 7]
print(f'TEST_HYPINT_ARR: {test_hypint_arr}') # => [2, 3]
print(f'TEST_EXPINT_ARR: {test_expint_arr}') # => [1.8204784532536746, 3]
print(f'TEST_LOGINT_ARR: {test_logint_arr}') # => [2, 3]

print(f'TEST_LININT_EV: {test_linint_ev}') # => 28.0
print(f'TEST_QUADINT_EV: {test_quadint_ev}') # => 86.66666666666666
print(f'TEST_CUBINT_EV: {test_cubint_ev}') # => 260.0
print(f'TEST_HYPINT_EV: {test_hypint_ev}') # => 14.772588722239782
print(f'TEST_EXPINT_EV: {test_expint_ev}') # => 147.45875471354765
print(f'TEST_LOGINT_EV: {test_logint_ev}') # => 12.635532333438686

print(f'TEST_LININT_ACC: {test_linint_acc}') # => 126.0
print(f'TEST_QUADINT_ACC: {test_quadint_acc}') # => 859.5
print(f'TEST_CUBINT_ACC: {test_cubint_acc}') # => 6309.0
print(f'TEST_HYPINT_ACC: {test_hypint_acc}') # => 31.605170185988094
print(f'TEST_EXPINT_ACC: {test_expint_acc}') # => 107491.97075081647
print(f'TEST_LOGINT_ACC: {test_logint_acc}') # => 60.077552789821375

print(f'TEST_CRIT_LIN1: {test_crit_lin1}') # => [None]
print(f'TEST_CRIT_QUAD1: {test_crit_quad1}') # => [-0.75]
print(f'TEST_CRIT_CUB1: {test_crit_cub1}') # => [(-0.49999999999999994+0.7637626158259733j), (-0.5000000000000001-0.7637626158259733j)]
print(f'TEST_CRIT_HYP1: {test_crit_hyp1}') # => [None]
print(f'TEST_CRIT_EXP1: {test_crit_exp1}') # => [None]
print(f'TEST_CRIT_LOG1: {test_crit_log1}') # => [None]

print(f'TEST_CRIT_LIN_VAL: {test_crit_lin_val}') # => [None]
print(f'TEST_CRIT_QUAD_VAL: {test_crit_quad_val}') # => [3.875]
print(f'TEST_CRIT_CUB_VAL: {test_crit_cub_val}') # => [(5+1.7821127702606043j), (5-1.7821127702606043j)]
print(f'TEST_CRIT_HYP_VAL: {test_crit_hyp_val}') # => [None]
print(f'TEST_CRIT_EXP_VAL: {test_crit_exp_val}') # => [None]
print(f'TEST_CRIT_LOG_VAL: {test_crit_log_val}') # => [None]

print(f'TEST_UNIFY_LIN: {test_unify_lin}') # => [None]
print(f'TEST_UNIFY_QUAD: {test_unify_quad}') # => [[-0.75, 3.875]]
print(f'TEST_UNIFY_CUB: {test_unify_cub}') # => [[(-0.49999999999999994+0.7637626158259733j), (5+1.7821127702606043j)], [(-0.5000000000000001-0.7637626158259733j), (5-1.7821127702606043j)]]
print(f'TEST_UNIFY_HYP: {test_unify_hyp}') # => [None]
print(f'TEST_UNIFY_EXP: {test_unify_exp}') # => [None]
print(f'TEST_UNIFY_LOG: {test_unify_log}') # => [None]

print(f'TEST_CRIT_LIN2: {test_crit_lin2}') # => [None]
print(f'TEST_CRIT_QUAD2: {test_crit_quad2}') # => [None]
print(f'TEST_CRIT_CUB2: {test_crit_cub2}') # => [-0.5]
print(f'TEST_CRIT_HYP2: {test_crit_hyp2}') # => [None]
print(f'TEST_CRIT_EXP2: {test_crit_exp2}') # => [None]
print(f'TEST_CRIT_LOG2: {test_crit_log2}') # => [None]
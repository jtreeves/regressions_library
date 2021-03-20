from library.analyses.equations.linear import linear as linear_equation
from library.analyses.equations.quadratic import quadratic as quadratic_equation
from library.analyses.equations.cubic import cubic as cubic_equation
from library.analyses.equations.hyperbolic import hyperbolic as hyperbolic_equation
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.equations.logarithmic import logarithmic as logarithmic_equation
from library.analyses.roots.linear import linear as linear_roots
from library.analyses.roots.quadratic import quadratic as quadratic_roots
from library.analyses.roots.cubic import cubic as cubic_roots
from library.analyses.roots.hyperbolic import hyperbolic as hyperbolic_roots
from library.analyses.roots.exponential import exponential as exponential_roots
from library.analyses.roots.logarithmic import logarithmic as logarithmic_roots
from library.analyses.derivatives.linear import linear as linear_derivatives
from library.analyses.derivatives.quadratic import quadratic as quadratic_derivatives
from library.analyses.derivatives.cubic import cubic as cubic_derivatives
from library.analyses.derivatives.hyperbolic import hyperbolic as hyperbolic_derivatives
from library.analyses.derivatives.exponential import exponential as exponential_derivatives
from library.analyses.derivatives.logarithmic import logarithmic as logarithmic_derivatives
from library.analyses.integrals.linear import linear as linear_integral
from library.analyses.integrals.quadratic import quadratic as quadratic_integral
from library.analyses.integrals.cubic import cubic as cubic_integral
from library.analyses.integrals.hyperbolic import hyperbolic as hyperbolic_integral
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.integrals.logarithmic import logarithmic as logarithmic_integral
from library.analyses.critical_points import critical_points
from library.analyses.critical_values import critical_values
from library.analyses.intervals import intervals
from library.analyses.maxima import maxima
from library.analyses.minima import minima
from library.analyses.extrema import extrema
from library.analyses.inflections import inflections
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values

coefficients = [2, 3, 5, 7]
other = [2, -3, -5, 7]

other_cubic_roots = cubic_roots(other[0], other[1], other[2], other[3])

print(f'OTHER_cubic_roots: {other_cubic_roots}')

test_linear_equation = linear_equation(coefficients[0], coefficients[1])
test_quadratic_equation = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
test_cubic_equation = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hyperbolic_equation = hyperbolic_equation(coefficients[0], coefficients[1])
test_exponential_equation = exponential_equation(coefficients[0], coefficients[1])
test_logarithmic_equation = logarithmic_equation(coefficients[0], coefficients[1])

test_linear_roots = linear_roots(coefficients[0], coefficients[1])
test_quadratic_roots = quadratic_roots(coefficients[0], coefficients[1], coefficients[2])
test_cubic_roots = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hyperbolic_roots = hyperbolic_roots(coefficients[0], coefficients[1])
test_exponential_roots = exponential_roots(coefficients[0], coefficients[1])
test_logarithmic_roots = logarithmic_roots(coefficients[0], coefficients[1])

test_linear_derivatives = linear_derivatives(coefficients[0], coefficients[1])
test_quadratic_derivatives = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])
test_cubic_derivatives = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hyperbolic_derivatives = hyperbolic_derivatives(coefficients[0], coefficients[1])
test_exponential_derivatives = exponential_derivatives(coefficients[0], coefficients[1])
test_logarithmic_derivatives = logarithmic_derivatives(coefficients[0], coefficients[1])

test_linear_integral = linear_integral(coefficients[0], coefficients[1])
test_quadratic_integral = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])
test_cubic_integral = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
test_hyperbolic_integral = hyperbolic_integral(coefficients[0], coefficients[1])
test_exponential_integral = exponential_integral(coefficients[0], coefficients[1])
test_logarithmic_integral = logarithmic_integral(coefficients[0], coefficients[1])

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

test_linev = test_linear_equation(4)
test_quadev = test_quadratic_equation(4)
test_cubev = test_cubic_equation(4)
test_hypev = test_hyperbolic_equation(4)
test_expev = test_exponential_equation(4)
test_logev = test_logarithmic_equation(4)

test_linear_roots_arr = test_linear_roots
test_quadratic_roots_arr = test_quadratic_roots
test_cubic_roots_arr = test_cubic_roots
test_hyperbolic_roots_arr = test_hyperbolic_roots
test_exponential_roots_arr = test_exponential_roots
test_logarithmic_roots_arr = test_logarithmic_roots

test_linear_derivatives_first = test_linear_derivatives['first']
test_quadratic_derivatives_first = test_quadratic_derivatives['first']
test_cubic_derivatives_first = test_cubic_derivatives['first']
test_hyperbolic_derivatives_first = test_hyperbolic_derivatives['first']
test_exponential_derivatives_first = test_exponential_derivatives['first']
test_logarithmic_derivatives_first = test_logarithmic_derivatives['first']

test_linear_derivatives_first_arr = test_linear_derivatives['first']['constants']
test_quadratic_derivatives_first_arr = test_quadratic_derivatives['first']['constants']
test_cubic_derivatives_first_arr = test_cubic_derivatives['first']['constants']
test_hyperbolic_derivatives_first_arr = test_hyperbolic_derivatives['first']['constants']
test_exponential_derivatives_first_arr = test_exponential_derivatives['first']['constants']
test_logarithmic_derivatives_first_arr = test_logarithmic_derivatives['first']['constants']

test_linear_derivatives_first_ev = test_linear_derivatives['first']['evaluation'](4)
test_quadratic_derivatives_first_ev = test_quadratic_derivatives['first']['evaluation'](4)
test_cubic_derivatives_first_ev = test_cubic_derivatives['first']['evaluation'](4)
test_hyperbolic_derivatives_first_ev = test_hyperbolic_derivatives['first']['evaluation'](4)
test_exponential_derivatives_first_ev = test_exponential_derivatives['first']['evaluation'](4)
test_logarithmic_derivatives_first_ev = test_logarithmic_derivatives['first']['evaluation'](4)

test_linear_derivatives_second = test_linear_derivatives['second']
test_quadratic_derivatives_second = test_quadratic_derivatives['second']
test_cubic_derivatives_second = test_cubic_derivatives['second']
test_hyperbolic_derivatives_second = test_hyperbolic_derivatives['second']
test_exponential_derivatives_second = test_exponential_derivatives['second']
test_logarithmic_derivatives_second = test_logarithmic_derivatives['second']

test_linear_derivatives_second_arr = test_linear_derivatives['second']['constants']
test_quadratic_derivatives_second_arr = test_quadratic_derivatives['second']['constants']
test_cubic_derivatives_second_arr = test_cubic_derivatives['second']['constants']
test_hyperbolic_derivatives_second_arr = test_hyperbolic_derivatives['second']['constants']
test_exponential_derivatives_second_arr = test_exponential_derivatives['second']['constants']
test_logarithmic_derivatives_second_arr = test_logarithmic_derivatives['second']['constants']

test_linear_derivatives_second_ev = test_linear_derivatives['second']['evaluation'](4)
test_quadratic_derivatives_second_ev = test_quadratic_derivatives['second']['evaluation'](4)
test_cubic_derivatives_second_ev = test_cubic_derivatives['second']['evaluation'](4)
test_hyperbolic_derivatives_second_ev = test_hyperbolic_derivatives['second']['evaluation'](4)
test_exponential_derivatives_second_ev = test_exponential_derivatives['second']['evaluation'](4)
test_logarithmic_derivatives_second_ev = test_logarithmic_derivatives['second']['evaluation'](4)

test_ints_lin = intervals(test_linear_derivatives_first['evaluation'], test_crit_lin1)
test_ints_quad = intervals(test_quadratic_derivatives_first['evaluation'], test_crit_quad1)
test_ints_cub = intervals(test_cubic_derivatives_first['evaluation'], test_crit_cub1)
test_ints_hyp = intervals(test_hyperbolic_derivatives_first['evaluation'], test_crit_hyp1)
test_ints_exp = intervals(test_exponential_derivatives_first['evaluation'], test_crit_exp1)
test_ints_log = intervals(test_logarithmic_derivatives_first['evaluation'], test_crit_log1)

test_ints2_lin = intervals(test_linear_derivatives_second['evaluation'], test_crit_lin2)
test_ints2_quad = intervals(test_quadratic_derivatives_second['evaluation'], test_crit_quad2)
test_ints2_cub = intervals(test_cubic_derivatives_second['evaluation'], test_crit_cub2)
test_ints2_hyp = intervals(test_hyperbolic_derivatives_second['evaluation'], test_crit_hyp2)
test_ints2_exp = intervals(test_exponential_derivatives_second['evaluation'], test_crit_exp2)
test_ints2_log = intervals(test_logarithmic_derivatives_second['evaluation'], test_crit_log2)

test_max_lin = maxima(test_ints_lin)
test_max_quad = maxima(test_ints_quad)
test_max_cub = maxima(test_ints_cub)
test_max_hyp = maxima(test_ints_hyp)
test_max_exp = maxima(test_ints_exp)
test_max_log = maxima(test_ints_log)

test_min_lin = minima(test_ints_lin)
test_min_quad = minima(test_ints_quad)
test_min_cub = minima(test_ints_cub)
test_min_hyp = minima(test_ints_hyp)
test_min_exp = minima(test_ints_exp)
test_min_log = minima(test_ints_log)

test_extr_lin = extrema(test_ints_lin)
test_extr_quad = extrema(test_ints_quad)
test_extr_cub = extrema(test_ints_cub)
test_extr_hyp = extrema(test_ints_hyp)
test_extr_exp = extrema(test_ints_exp)
test_extr_log = extrema(test_ints_log)

test_infl_lin = inflections(test_ints2_lin)
test_infl_quad = inflections(test_ints2_quad)
test_infl_cub = inflections(test_ints2_cub)
test_infl_hyp = inflections(test_ints2_hyp)
test_infl_exp = inflections(test_ints2_exp)
test_infl_log = inflections(test_ints2_log)

test_linear_integral_arr = test_linear_integral['constants']
test_quadratic_integral_arr = test_quadratic_integral['constants']
test_cubic_integral_arr = test_cubic_integral['constants']
test_hyperbolic_integral_arr = test_hyperbolic_integral['constants']
test_exponential_integral_arr = test_exponential_integral['constants']
test_logarithmic_integral_arr = test_logarithmic_integral['constants']

test_linear_integral_ev = test_linear_integral['evaluation'](4)
test_quadratic_integral_ev = test_quadratic_integral['evaluation'](4)
test_cubic_integral_ev = test_cubic_integral['evaluation'](4)
test_hyperbolic_integral_ev = test_hyperbolic_integral['evaluation'](4)
test_exponential_integral_ev = test_exponential_integral['evaluation'](4)
test_logarithmic_integral_ev = test_logarithmic_integral['evaluation'](4)

test_linear_integral_acc = accumulation(test_linear_integral['evaluation'], 1, 10)
test_quadratic_integral_acc = accumulation(test_quadratic_integral['evaluation'], 1, 10)
test_cubic_integral_acc = accumulation(test_cubic_integral['evaluation'], 1, 10)
test_hyperbolic_integral_acc = accumulation(test_hyperbolic_integral['evaluation'], 1, 10)
test_exponential_integral_acc = accumulation(test_exponential_integral['evaluation'], 1, 10)
test_logarithmic_integral_acc = accumulation(test_logarithmic_integral['evaluation'], 1, 10)

test_av_der_lin = average_value_derivative(test_linear_equation, 1, 10)
test_av_der_quad = average_value_derivative(test_quadratic_equation, 1, 10)
test_av_der_cub = average_value_derivative(test_cubic_equation, 1, 10)
test_av_der_hyp = average_value_derivative(test_hyperbolic_equation, 1, 10)
test_av_der_exp = average_value_derivative(test_exponential_equation, 1, 10)
test_av_der_log = average_value_derivative(test_logarithmic_equation, 1, 10)

test_av_int_lin = average_value_integral(test_linear_integral['evaluation'], 1, 10)
test_av_int_quad = average_value_integral(test_quadratic_integral['evaluation'], 1, 10)
test_av_int_cub = average_value_integral(test_cubic_integral['evaluation'], 1, 10)
test_av_int_hyp = average_value_integral(test_hyperbolic_integral['evaluation'], 1, 10)
test_av_int_exp = average_value_integral(test_exponential_integral['evaluation'], 1, 10)
test_av_int_log = average_value_integral(test_logarithmic_integral['evaluation'], 1, 10)

test_m_der_lin = mean_values_derivative('linear', test_linear_equation, 1, 10, test_linear_derivatives_first_arr)
test_m_der_quad = mean_values_derivative('quadratic', test_quadratic_equation, 1, 10, test_quadratic_derivatives_first_arr)
test_m_der_cub = mean_values_derivative('cubic', test_cubic_equation, 1, 10, test_cubic_derivatives_first_arr)
test_m_der_hyp = mean_values_derivative('hyperbolic', test_hyperbolic_equation, 1, 10, test_hyperbolic_derivatives_first_arr)
test_m_der_exp = mean_values_derivative('exponential', test_exponential_equation, 1, 10, test_exponential_derivatives_first_arr)
test_m_der_log = mean_values_derivative('logarithmic', test_logarithmic_equation, 1, 10, test_logarithmic_derivatives_first_arr)

test_m_int_lin = mean_values_integral('linear', test_linear_integral['evaluation'], 1, 10, coefficients)
test_m_int_quad = mean_values_integral('quadratic', test_quadratic_integral['evaluation'], 1, 10, coefficients)
test_m_int_cub = mean_values_integral('cubic', test_cubic_integral['evaluation'], 1, 10, coefficients)
test_m_int_hyp = mean_values_integral('hyperbolic', test_hyperbolic_integral['evaluation'], 1, 10, coefficients)
test_m_int_exp = mean_values_integral('exponential', test_exponential_integral['evaluation'], 1, 10, coefficients)
test_m_int_log = mean_values_integral('logarithmic', test_logarithmic_integral['evaluation'], 1, 10, coefficients)

print(f'TEST_LINEV: {test_linev}') # => 11
print(f'TEST_QUADEV: {test_quadev}') # => 49
print(f'TEST_CUBEV: {test_cubev}') # => 203
print(f'TEST_HYPEV: {test_hypev}') # => 3.5
print(f'TEST_EXPEV: {test_expev}') # => 162
print(f'TEST_LOGEV: {test_logev}') # => 6.1588830833596715

print(f'TEST_linear_roots_ARR: {test_linear_roots_arr}') # => [-1.5]
print(f'TEST_quadratic_roots_ARR: {test_quadratic_roots_arr}') # => [(-0.7499999999999999+1.3919410907075054j), (-0.7500000000000001-1.3919410907075054j)]
print(f'TEST_cubic_roots_ARR: {test_cubic_roots_arr}') # => [None]
print(f'TEST_hyperbolic_roots_ARR: {test_hyperbolic_roots_arr}') # => [-0.6666666666666666]
print(f'TEST_exponential_roots_ARR: {test_exponential_roots_arr}') # => [None]
print(f'TEST_logarithmic_roots_ARR: {test_logarithmic_roots_arr}') # => [0.513417119032592]

print(f'TEST_linear_derivatives_FIRST_ARR: {test_linear_derivatives_first_arr}') # => [2]
print(f'TEST_quadratic_derivatives_FIRST_ARR: {test_quadratic_derivatives_first_arr}') # => [4, 3]
print(f'TEST_cubic_derivatives_FIRST_ARR: {test_cubic_derivatives_first_arr}') # => [6, 6, 5]
print(f'TEST_hyperbolic_derivatives_FIRST_ARR: {test_hyperbolic_derivatives_first_arr}') # => [-2]
print(f'TEST_exponential_derivatives_FIRST_ARR: {test_exponential_derivatives_first_arr}') # => [2.1972245773362196, 3]
print(f'TEST_logarithmic_derivatives_FIRST_ARR: {test_logarithmic_derivatives_first_arr}') # => [3, 0]

print(f'TEST_linear_derivatives_FIRST_EV: {test_linear_derivatives_first_ev}') # => 2
print(f'TEST_quadratic_derivatives_FIRST_EV: {test_quadratic_derivatives_first_ev}') # => 19
print(f'TEST_cubic_derivatives_FIRST_EV: {test_cubic_derivatives_first_ev}') # => 125
print(f'TEST_hyperbolic_derivatives_FIRST_EV: {test_hyperbolic_derivatives_first_ev}') # => -0.125
print(f'TEST_exponential_derivatives_FIRST_EV: {test_exponential_derivatives_first_ev}') # => 177.9751907642338
print(f'TEST_logarithmic_derivatives_FIRST_EV: {test_logarithmic_derivatives_first_ev}') # => 0.75

print(f'TEST_linear_derivatives_SECOND_ARR: {test_linear_derivatives_second_arr}') # => [0]
print(f'TEST_quadratic_derivatives_SECOND_ARR: {test_quadratic_derivatives_second_arr}') # => [4]
print(f'TEST_cubic_derivatives_SECOND_ARR: {test_cubic_derivatives_second_arr}') # => [12, 6]
print(f'TEST_hyperbolic_derivatives_SECOND_ARR: {test_hyperbolic_derivatives_second_arr}') # => [4]
print(f'TEST_exponential_derivatives_SECOND_ARR: {test_exponential_derivatives_second_arr}') # => [2.413897921625164, 3]
print(f'TEST_logarithmic_derivatives_SECOND_ARR: {test_logarithmic_derivatives_second_arr}') # => [-3, 0]

print(f'TEST_linear_derivatives_SECOND_EV: {test_linear_derivatives_second_ev}') # => 0
print(f'TEST_quadratic_derivatives_SECOND_EV: {test_quadratic_derivatives_second_ev}') # => 4
print(f'TEST_cubic_derivatives_SECOND_EV: {test_cubic_derivatives_second_ev}') # => 54
print(f'TEST_hyperbolic_derivatives_SECOND_EV: {test_hyperbolic_derivatives_second_ev}') # => 0.0625
print(f'TEST_exponential_derivatives_SECOND_EV: {test_exponential_derivatives_second_ev}') # => 195.5257316516383
print(f'TEST_logarithmic_derivatives_SECOND_EV: {test_logarithmic_derivatives_second_ev}') # => -0.1875

print(f'TEST_linear_integral_ARR: {test_linear_integral_arr}') # => [1.0, 3]
print(f'TEST_quadratic_integral_ARR: {test_quadratic_integral_arr}') # => [0.6666666666666666, 1.5, 5]
print(f'TEST_cubic_integral_ARR: {test_cubic_integral_arr}') # => [0.5, 1.0, 2.5, 7]
print(f'TEST_hyperbolic_integral_ARR: {test_hyperbolic_integral_arr}') # => [2, 3]
print(f'TEST_exponential_integral_ARR: {test_exponential_integral_arr}') # => [1.8204784532536746, 3]
print(f'TEST_logarithmic_integral_ARR: {test_logarithmic_integral_arr}') # => [2, 3]

print(f'TEST_linear_integral_EV: {test_linear_integral_ev}') # => 28.0
print(f'TEST_quadratic_integral_EV: {test_quadratic_integral_ev}') # => 86.66666666666666
print(f'TEST_cubic_integral_EV: {test_cubic_integral_ev}') # => 260.0
print(f'TEST_hyperbolic_integral_EV: {test_hyperbolic_integral_ev}') # => 14.772588722239782
print(f'TEST_exponential_integral_EV: {test_exponential_integral_ev}') # => 147.45875471354765
print(f'TEST_logarithmic_integral_EV: {test_logarithmic_integral_ev}') # => 12.635532333438686

print(f'TEST_linear_integral_ACC: {test_linear_integral_acc}') # => 126.0
print(f'TEST_quadratic_integral_ACC: {test_quadratic_integral_acc}') # => 859.5
print(f'TEST_cubic_integral_ACC: {test_cubic_integral_acc}') # => 6309.0
print(f'TEST_hyperbolic_integral_ACC: {test_hyperbolic_integral_acc}') # => 31.605170185988094
print(f'TEST_exponential_integral_ACC: {test_exponential_integral_acc}') # => 107491.97075081647
print(f'TEST_logarithmic_integral_ACC: {test_logarithmic_integral_acc}') # => 60.077552789821375

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

print(f'TEST_INTS_LIN: {test_ints_lin}') # => ['increasing']
print(f'TEST_INTS_QUAD: {test_ints_quad}') # => ['decreasing', -0.75, 'increasing']
print(f'TEST_INTS_CUB: {test_ints_cub}') # => [None]
print(f'TEST_INTS_HYP: {test_ints_hyp}') # => ['increasing']
print(f'TEST_INTS_EXP: {test_ints_exp}') # => ['increasing']
print(f'TEST_INTS_LOG: {test_ints_log}') # => ['increasing']

print(f'TEST_MAX_LIN: {test_max_lin}') # => [None]
print(f'TEST_MAX_QUAD: {test_max_quad}') # => [None]
print(f'TEST_MAX_CUB: {test_max_cub}') # => [None]
print(f'TEST_MAX_HYP: {test_max_hyp}') # => [None]
print(f'TEST_MAX_EXP: {test_max_exp}') # => [None]
print(f'TEST_MAX_LOG: {test_max_log}') # => [None]

print(f'TEST_MIN_LIN: {test_min_lin}') # => [None]
print(f'TEST_MIN_QUAD: {test_min_quad}') # => [-0.75]
print(f'TEST_MIN_CUB: {test_min_cub}') # => [None]
print(f'TEST_MIN_HYP: {test_min_hyp}') # => [None]
print(f'TEST_MIN_EXP: {test_min_exp}') # => [None]
print(f'TEST_MIN_LOG: {test_min_log}') # => [None]

print(f'TEST_EXTR_LIN: {test_extr_lin}') # => {'maxima': [None], 'minima': [None]}
print(f'TEST_EXTR_QUAD: {test_extr_quad}') # => {'maxima': [None], 'minima': [-0.75]}
print(f'TEST_EXTR_CUB: {test_extr_cub}') # => {'maxima': [None], 'minima': [None]}
print(f'TEST_EXTR_HYP: {test_extr_hyp}') # => {'maxima': [None], 'minima': [None]}
print(f'TEST_EXTR_EXP: {test_extr_exp}') # => {'maxima': [None], 'minima': [None]}
print(f'TEST_EXTR_LOG: {test_extr_log}') # => {'maxima': [None], 'minima': [None]}

print(f'TEST_INFL_LIN: {test_infl_lin}') # => [None]
print(f'TEST_INFL_QUAD: {test_infl_quad}') # => [None]
print(f'TEST_INFL_CUB: {test_infl_cub}') # => [-0.5]
print(f'TEST_INFL_HYP: {test_infl_hyp}') # => [None]
print(f'TEST_INFL_EXP: {test_infl_exp}') # => [None]
print(f'TEST_INFL_LOG: {test_infl_log}') # => [None]

print(f'TEST_AV_DER_LIN: {test_av_der_lin}') # => 2.0
print(f'TEST_AV_DER_QUAD: {test_av_der_quad}') # => 25.0
print(f'TEST_AV_DER_CUB: {test_av_der_cub}') # => 260.0
print(f'TEST_AV_DER_HYP: {test_av_der_hyp}') # => -0.19999999999999998
print(f'TEST_AV_DER_EXP: {test_av_der_exp}') # => 13121.333333333334
print(f'TEST_AV_DER_LOG: {test_av_der_log}') # => 0.7675283643313485

print(f'TEST_M_DER_LIN: {test_m_der_lin}') # => [None]
print(f'TEST_M_DER_QUAD: {test_m_der_quad}') # => [5.5]
print(f'TEST_M_DER_CUB: {test_m_der_cub}') # => [6.0383484153110105]
print(f'TEST_M_DER_HYP: {test_m_der_hyp}') # => [3.1622776601683795]
print(f'TEST_M_DER_EXP: {test_m_der_exp}') # => [7.91434773200577]
print(f'TEST_M_DER_LOG: {test_m_der_log}') # => [3.9086503371292665]

print(f'TEST_AV_INT_LIN: {test_av_int_lin}') # => 14.0
print(f'TEST_AV_INT_QUAD: {test_av_int_quad}') # => 95.5
print(f'TEST_AV_INT_CUB: {test_av_int_cub}') # => 701.0
print(f'TEST_AV_INT_HYP: {test_av_int_hyp}') # => 3.5116855762208994
print(f'TEST_AV_INT_EXP: {test_av_int_exp}') # => 11943.552305646275
print(f'TEST_AV_INT_LOG: {test_av_int_log}') # => 6.675283643313486

print(f'TEST_M_INT_LIN: {test_m_int_lin}') # => [5.5]
print(f'TEST_M_INT_QUAD: {test_m_int_quad}') # => [6.018493185340442]
print(f'TEST_M_INT_CUB: {test_m_int_cub}') # => [None]
print(f'TEST_M_INT_HYP: {test_m_int_hyp}') # => [3.908650337129264]
print(f'TEST_M_INT_EXP: {test_m_int_exp}') # => [7.91434773200577]
print(f'TEST_M_INT_LOG: {test_m_int_log}') # => [4.751345690108391]
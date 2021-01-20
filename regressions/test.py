from .run_all import run_all

set_20 = [[1, 78], [2, 64], [3, 97], [4, 34], [5, 53], [6, 65], [7, 79], [8, 201], [9, 123], [10, 145], [11, 356], [12, 77], [13, 478], [14, 598], [15, 376], [16, 294], [17, 401], [18, 532], [19, 607], [20, 752]]

sinusoidal_set = [[1, 7], [2, 12], [3, 19], [4, 25], [5, 32], [6, 28], [7, 21], [8, 14], [9, 9], [10, 6], [11, 10], [12, 17], [13, 18], [14, 25], [15, 31], [16, 35], [17, 26], [18, 22], [19, 15], [20, 8]]

all_solutions = run_all(set_20)
sinusoidal_solutions = run_all(sinusoidal_set)

print(f"Linear Constants: {all_solutions['options']['linear']['constants']}") # => [[32.98796992481202], [-75.87368421052619]]
print(f"Linear Error: {all_solutions['options']['linear']['error']}") # => 22.312581356511483

print(f"Quadratic Constants: {all_solutions['options']['quadratic']['constants']}") # => [[1.697653223969002], [-2.6627477785371454], [54.84561403508843]]
print(f"Quadratic Error: {all_solutions['options']['quadratic']['error']}") # => 21.07459477444664

print(f"Cubic Constants: {all_solutions['options']['cubic']['constants']}") # => [[-0.040814661624975546], [2.9833150651558444], [-13.727602545073111], [76.53044375644211]]
print(f"Cubic Error: {all_solutions['options']['cubic']['error']}") # => 21.05493315315674

print(f"Hyperbolic Constants: {all_solutions['options']['hyperbolic']['constants']}") # => [[-476.2476028415365], [356.17074436813056]]
print(f"Hyperbolic Error: {all_solutions['options']['hyperbolic']['error']}") # => 29.489660900232142

print(f"Exponential Constants: {all_solutions['options']['exponential']['constants']}") # => [[39.79809056464346], [1.154903969011854]]
print(f"Exponential Error: {all_solutions['options']['exponential']['error']}") # => 21.55169894398324

print(f"Logarithmic Constants: {all_solutions['options']['logarithmic']['constants']}") # => [[-154.60728466072027], [200.8272561968283]]
print(f"Logarithmic Error: {all_solutions['options']['logarithmic']['error']}") # => 26.11858512913022

print(f"Sinusoidal Constants: {all_solutions['options']['sinusoidal']['constants']}") # => [[-10637.7607716477], [1.041350832607493], [1.0384915217851285], [11620.027599096207]] // AFTER ASSUMING D WAS AVERAGE: [[2890.419345573162], [1.5332781974044583], [0.8563639472894197], [270.5]]
print(f"Sinusoidal Error: {all_solutions['options']['sinusoidal']['error']}") # => 242.7427759867437 // AFTER ASSUMING D WAS AVEAGE: 95.84704471142422

print(f"Best Choice Function: {all_solutions['optimal']['function']}") # => cubic
print(f"Best Choice Error: {all_solutions['optimal']['error']}") # => 21.05493315315674

print(f"Sinusoidal Constants from Sinusoidal Set: {sinusoidal_solutions['options']['sinusoidal']['constants']}") # => [[576.5683893876746], [0.6418752091287842], [1.2166595719545568], [-589.9653924694346]] // AFTER ASSUMING D WAS AVERAGE: [[-88.2760618749577], [1.4280482601704372], [0.8824477899791447], [19.0]]
print(f"Sinusoidal Error from Sinusoidal Set: {sinusoidal_solutions['options']['sinusoidal']['error']}") # => 57.12687660827426 // AFTER ASSUMING D WAS AVERAGE: 16.832572222493752

# agnostic_set = [[1, 3], [2, 147], [3, 286], [4, 352], [5, 423], [6, 510], [7, 591], [8, 451], [9, 689], [10, 862]]
# # cyclic_set = [[1, 33], [2, 27], [3, 45], [4, 56], [5, 69], [6, 84], [7, 88], [8, 75], [9, 57], [10, 42], [11, 39], [12, 28]]

# all_solutions = run_all(agnostic_set)
# # cyclic_solution = sinusoidal(cyclic_set)

# print(f"Linear Constants: {all_solutions['options']['linear']['constants']}") # => [[79.7212], [−7.0667]]
# print(f"Linear Error: {all_solutions['options']['linear']['error']}") # => 15.0577

# print(f"Quadratic Constants: {all_solutions['options']['quadratic']['constants']}") # => [[−1.6515], [97.8879], [−43.4000]]
# print(f"Quadratic Error: {all_solutions['options']['quadratic']['error']}") # => 14.9511

# print(f"Cubic Constants: {all_solutions['options']['cubic']['constants']}") # => [[2.7704], [−47.3631], [308.7150], [−281.1000]]
# print(f"Cubic Error: {all_solutions['options']['cubic']['error']}") # => 12.7299

# print(f"Hyperbolic Constants: {all_solutions['options']['hyperbolic']['constants']}") # => [[-766.8421], [656.0056]]
# print(f"Hyperbolic Error: {all_solutions['options']['hyperbolic']['error']}") # => 20.2718

# print(f"Exponential Constants: {all_solutions['options']['exponential']['constants']}") # => [[29.2304], [1.4898]]
# print(f"Exponential Error: {all_solutions['options']['exponential']['error']}") # => 30.7182

# print(f"Logarithmic Constants: {all_solutions['options']['logarithmic']['constants']}") # => [[−58.7194], [324.4875]]
# print(f"Logarithmic Error: {all_solutions['options']['logarithmic']['error']}") # => 16.0616

# print(f"Sinusoidal Constants: {all_solutions['options']['sinusoidal']['constants']}") # => [[-3514.2353], [0.9678], [0.0], [9935.7845]]
# print(f"Sinusoidal Error: {all_solutions['options']['sinusoidal']['error']}") # => 170.4962

# print(f"Best Choice Function: {all_solutions['optimal']['function']}") # => cubic
# print(f"Best Choice Error: {all_solutions['optimal']['error']}") # => 12.7299

# # print(f"Sinusoidal Constants: {cyclic_solution['constants']}") # => [[28.2382], [0.5236], [-1.8948], [53.5833]] // VERSUS WHAT I GOT: [[1126.9119], [1.1709], [-2.1711], [1290.0787]] // NEW VALUES: [[-22022.99146071105], [0.6013015109266755], [0.6276552476317352], [13293.135715281009]] // NEWER VALUES: [[15430.83920235599], [0.6013015109266755], [0.6276552476317352], [-8701.570750628009]] // VALUES AFTER AVERAGING A & B: [[-152.7393206522671], [0.6903501429559035], [0.34884660006533247], [412.3751222003216]] // VALUES AFTER AVERAGING C TOO: [[-143.53948777894792], [0.6903501429559035], [0.0005912281158484189], [360.2515322553028]] // AFTER SUPER AVERAGING C: [[-143.5394626917854], [0.6903501429559035], [0.0], [360.1666676793375]]
# # print(f"Sinusoidal Error: {cyclic_solution['error']}") # => NOT SURE WHAT I SHOULD HAVE EXPECTED, BUT I GOT: 69.6112 // NEW ERROR: 258.3859834434484 // NEWER ERROR: 214.2937082641205 // ERROR AFTER AVERAGING A & B: 34.296893836130046 // AFTER AVERAGING C TOO: 31.688095114749128 // AFTER SUPER AVERAGING C: 31.683858436939786
from math import cos, inf, pi, sqrt
from itertools import tee

# simplified implementation for binary coded individual
# since individual is essentially a list of "0" and "1", then all of those values are within a range (-5.12, +5.12)
# parameters products_data, hyperparams are not used but needed for a correct usage with our custom GA 
def rastrigin(individual, products_data, hyperparams):
    return 10*len(individual) + sum(x**2 - 10*cos(2*pi*x) for x in individual),

# simplified implementation for binary coded individual
# since individual is essentially a list of "0" and "1", then all of those values are within a range (-5.12, +5.12)
# parameters products_data, hyperparams are not used but needed for a correct usage with our custom GA 
def deJong1(individual, products_data, hyperparams):
        return sum(x**2 for x in individual),

# simplified implementation for binary coded individual
# since individual is essentially a list of "0" and "1", then all of those values are within a range (-600, +600)
# parameters products_data, hyperparams are not used but needed for a correct usage with our custom GA 
def griewank(individual, products_data, hyperparams):
    return sum(((x*100)**2) / 4000 for x in individual) + \
        product(cos((x*100) / sqrt(i)) for i, x in enumerate(individual, 1)),

def product(iterable):
    result = 1
    for number in iterable:
        result *= number
    return result


# find more test functions there https://www.sfu.ca/~ssurjano/griewank.html
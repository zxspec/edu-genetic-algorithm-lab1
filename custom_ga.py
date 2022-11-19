import numpy
import random
from products_data import ProductsData
from hyperparams import Hyperparams
from deap import base, creator, algorithms, tools


def is_valid_individual(individual, products_data, hyperparams, show_stats_when_valid=False):
    cost = 0
    sum_space = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            cost += products_data.prices[i]
            sum_space += products_data.spaces[i]
            if sum_space > hyperparams.space_limit:
                print('### ❌ sum_space: ', sum_space)
                print('### ❌ individual: ', individual)
                return False
    if show_stats_when_valid == True:
        print('### 🔥 individual: ', individual)
        print('### 🔥 sum_space: ', sum_space)
        print('### 🔥 cost: ', cost)
    return True


def get_custom_ga(params: Hyperparams, products_data: ProductsData, fitness, hall_of_fame):
    genes_number = len(products_data.names)
    toolbox = base.Toolbox()
    creator.create('FitnessMax', base.Fitness, weights=(1.0,))
    creator.create('Individual', list, fitness=creator.FitnessMax)

    toolbox.register('random_binary', random.randint, 0, 1)
    # create function which initializes an individual
    toolbox.register('individual', tools.initRepeat,
                     creator.Individual, toolbox.random_binary, genes_number)
    # create function which initializes a population
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    # create fitness function, name `evaluate` required by `eaSimple` algorithm
    toolbox.register('evaluate', fitness,
                     products_data=products_data, hyperparams=params)
    toolbox.register('feasible', is_valid_individual,
                     products_data=products_data, hyperparams=params)
    toolbox.decorate("evaluate", tools.DeltaPenalty(toolbox.feasible, 1.0))

    # create crossover function, name `mate` required by `eaSimple` algorithm
    toolbox.register('mate', tools.cxOnePoint)
    # create mutation function, name `mutate` required by `eaSimple` algorithm
    toolbox.register('mutate', tools.mutFlipBit,
                     indpb=params.mutation_probability)
    # create selection function, name `select` required by `eaSimple` algorithm
    toolbox.register('select', tools.selRoulette)

    population = toolbox.population(params.population_size)

    statistics = prepare_statistics_params()

    population, info = algorithms.eaSimple(population, toolbox, params.crossover_probability,
                                           params.mutation_probability, params.number_of_generations, statistics, verbose=True, halloffame=hall_of_fame)

    # print Hall of Fame info:
    print("Hall of Fame Individuals = ", *hall_of_fame.items, sep="\n")
    print("Best Ever Individual = ", hall_of_fame.items[0])
    print(is_valid_individual(
        hall_of_fame.items[0], products_data, params, show_stats_when_valid=True))
    # def is_valid_individual(individual, products_data, hyperparams):

    return (population, info)


def prepare_statistics_params():
    statistics = tools.Statistics(
        key=lambda individual: individual.fitness.values)

    statistics.register('max', numpy.max)
    statistics.register('min', numpy.min)
    statistics.register('med', numpy.mean)
    statistics.register('std', numpy.std)

    return statistics

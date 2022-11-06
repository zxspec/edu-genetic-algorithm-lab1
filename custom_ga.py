import numpy
import random
from products_data import ProductsData
from hyperparams import Hyperparams
from deap import base, creator, algorithms, tools


def get_custom_ga(params: Hyperparams, products_data: ProductsData, fitness):
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
                                           params.mutation_probability, params.number_of_generations, statistics)

    return (population, info)


def prepare_statistics_params():
    statistics = tools.Statistics(
        key=lambda individual: individual.fitness.values)

    statistics.register('max', numpy.max)
    statistics.register('min', numpy.min)
    statistics.register('med', numpy.mean)
    statistics.register('std', numpy.std)

    return statistics

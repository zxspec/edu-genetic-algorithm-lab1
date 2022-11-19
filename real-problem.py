from products_data import ProductsData, init_real_products
from hyperparams import Hyperparams
from contextlib import redirect_stdout
from deap import tools

from analytics import get_best_solutions, print_best_solutions, render_statistic_in_browser
from custom_ga import get_custom_ga

products_data = ProductsData(init_real_products())
params = Hyperparams(space_limit=10)
# params.mutation_probability = 0


def fitness(solution, products_data, hyperparams):
    cost = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            cost += products_data.prices[i]

    return (cost,)


HALL_OF_FAME_SIZE = 10
hof = tools.HallOfFame(HALL_OF_FAME_SIZE)
for i in range(0, 5):
    population, info = get_custom_ga(params, products_data, fitness, hall_of_fame=hof)
    render_statistic_in_browser(info)
    best_solutions = get_best_solutions(population)
    file_name = 'result-' + str(i) + '.txt'
    with open(file_name, 'w') as f:
        with redirect_stdout(f):
            print_best_solutions(
                best_solutions, products_data.names, products_data.prices)

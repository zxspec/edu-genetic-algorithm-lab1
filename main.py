from products_data import ProductsData
from hyperparams import Hyperparams

from analytics import get_best_solutions, print_best_solutions, render_statistic_in_browser
from custom_ga import get_custom_ga

products_data = ProductsData()
params = Hyperparams(space_limit=80)


def fitness(solution, products_data, hyperparams):
    cost = 0
    sum_space = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            cost += products_data.prices[i]
            sum_space += products_data.spaces[i]
    if sum_space > hyperparams.space_limit:
        cost = 1

    return (cost,)


population, info = get_custom_ga(params, products_data, fitness)

best_solutions = get_best_solutions(population)
print_best_solutions(best_solutions, products_data.names, products_data.prices)
render_statistic_in_browser(info)

from products_data import ProductsData, init_test_products
from hyperparams import Hyperparams
from test_functions import rastrigin, deJong1, griewank
from deap import tools

from custom_ga import get_custom_ga
from analytics import get_best_solutions, print_best_solutions, render_statistic_in_browser

products_data = ProductsData(init_test_products())
params = Hyperparams(space_limit=80)

#use rastrigin function instead of regular fitness function
population, info = get_custom_ga(params, products_data, rastrigin)
render_statistic_in_browser(info)
best_solutions = get_best_solutions(population)
print_best_solutions(best_solutions, products_data.names, products_data.prices)

#use dejong1 function instead of regular fitness function
population, info = get_custom_ga(params, products_data, deJong1)
render_statistic_in_browser(info)
best_solutions = get_best_solutions(population)
print_best_solutions(best_solutions, products_data.names, products_data.prices)

#use griewank function instead of regular fitness function
population, info = get_custom_ga(params, products_data, griewank)
render_statistic_in_browser(info)
best_solutions = get_best_solutions(population)
print_best_solutions(best_solutions, products_data.names, products_data.prices)
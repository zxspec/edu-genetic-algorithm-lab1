import plotly.express as px
from deap.tools import Logbook, selBest


def get_best_solutions(population, n=1):
    return selBest(population, 1)


def print_best_solutions(best_solutions: list, names: list, prices: list):
    for individual in best_solutions:
        print(individual)
        print(individual.fitness)
        for i in range(len(individual)):
            if individual[i] == 1:
                print('Name: ', names[i], ' - Price: ', prices[i])


def render_statistic_in_browser(info: Logbook):
    figure = px.line(
        x=range(0, 101),
        y=info.select('max'),
        title='Genetic algorithm results')

    figure.show()

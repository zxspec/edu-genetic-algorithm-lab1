import plotly.express as px
import pandas as pd
from deap.tools import Logbook, selBest


def get_best_solutions(population, n=1):
    return selBest(population, n)


def print_best_solutions(best_solutions: list, names: list, prices: list):
    for individual in best_solutions:
        print('\n')
        print('### best individual:', individual)
        print('### best individual fitness value: ', individual.fitness)
        print('### items: ', )
        for i in range(len(individual)):
            if individual[i] == 1:
                print('Name: ', names[i], ' - Price: ', prices[i])

def render_statistic_in_browser(info: Logbook):
    df = pd.DataFrame({
        'generations': info.select('gen'),
        'min': info.select('min'),
        'average': info.select('med'),
        'best': info.select('max'),
    })

    fig = px.line(df, x='generations', y=['best', 'average', 'min'])

    fig.show()

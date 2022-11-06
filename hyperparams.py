class Hyperparams:
    def __init__(self, space_limit: float):
        self.space_limit = space_limit
        self.population_size: int = 20
        self.number_of_generations: int = 100
        self.crossover_probability: float = 1.0
        self.mutation_probability: float = 0.01

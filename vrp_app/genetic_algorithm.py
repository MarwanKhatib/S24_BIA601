import random
import logging

logger = logging.getLogger('vrp_app')

class GeneticAlgorithm:
    def __init__(self, location_points, vehicle_capacities, depot=(0, 0)):
        self.location_points = location_points
        self.vehicle_capacities = vehicle_capacities
        self.depot = depot
        self.population_size = 50
        self.generations = 100
        self.mutation_rate = 0.02
        self.elite_size = 10
        self.customer_points = [point for point in location_points if point != depot]

    def distance(self, point1, point2):
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

    def initial_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self.customer_points[:]
            random.shuffle(individual)
            individual = [self.depot] + individual + [self.depot]
            population.append(individual)
        return population

    def fitness(self, individual):
        return sum(self.distance(individual[i], individual[i + 1]) for i in range(len(individual) - 1))

    def select_population(self, population):
        return sorted(population, key=self.fitness)[:self.elite_size]

    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
        child_p1 = parent1[start:end]
        child_p2 = [item for item in parent2 if item not in child_p1]
        return [self.depot] + child_p2[:start] + child_p1 + child_p2[start:] + [self.depot]

    def mutate(self, individual):
        for i in range(1, len(individual) - 1):
            if random.random() < self.mutation_rate:
                j = random.randint(1, len(individual) - 2)
                individual[i], individual[j] = individual[j], individual[i]

    def get_best_route(self):
        population = self.initial_population()
        for _ in range(self.generations):
            elites = self.select_population(population)
            population = elites[:]
            while len(population) < self.population_size:
                parent1, parent2 = random.sample(elites, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                population.append(child)
        return min(population, key=self.fitness)

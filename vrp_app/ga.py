import random
import logging

class GeneticAlgorithm:
    def __init__(self, location_points, vehicle_capacity):
        self.location_points = location_points
        self.vehicle_capacity = vehicle_capacity
        self.population_size = 100
        self.generations = 500
        self.mutation_rate = 0.01
        self.elite_size = 20

    def initial_population(self):
        logging.debug("Generating initial population...")
        population = []
        for _ in range(self.population_size):
            individual = self.location_points[:]
            random.shuffle(individual)
            population.append(individual)
        return population

    def fitness(self, route):
        logging.debug(f"Calculating fitness for route: {route}")
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance(route[i], route[i + 1])
        return total_distance

    def distance(self, point1, point2):
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

    def select_population(self, population):
        logging.debug("Selecting population based on fitness...")
        sorted_population = sorted(population, key=self.fitness)
        return sorted_population[:self.elite_size]

    def crossover(self, parent1, parent2):
        logging.debug("Performing crossover...")
        child = parent1[:len(parent1) // 2] + parent2[len(parent2) // 2:]
        return child

    def mutate(self, individual):
        logging.debug("Mutating individual...")
        if random.random() < self.mutation_rate:
            idx1 = random.randint(0, len(individual) - 1)
            idx2 = random.randint(0, len(individual) - 1)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    def get_best_route(self):
        logging.debug("Running genetic algorithm to get best route...")
        population = self.initial_population()

        for generation in range(self.generations):
            population = self.select_population(population)
            new_population = population[:]

            for i in range(len(population) - 1):
                parent1, parent2 = population[i], population[i + 1]
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            population = new_population

        best_route = min(population, key=self.fitness)
        return best_route

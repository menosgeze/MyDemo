from random import choice
import numpy as np

class Genetics:

    def __init__(self, population_size, chromosome_length):
        self.population_size = population_size
        self.chromosome_length = chromosome_length

    def generate_population(self):
        """
        Generates a population of chromosomes or binary arrays of specific length.

        Sets attribute:
            - population (list[list[int]]):
              binary array of shape (population_size, chromosome_length).
        """
        self.population = [
            list(element) for element in np.random.randint(
                low=0, high=2,
                size=(population_size, chromosome_length))]

    @static_method
    def get_ingredients_of_chromosome(chromosome, ingredients):
        assert len(ingredients) == len(chromosome)
        return [
            element for index, element in enumerate(ingredients)
            if chromosome[index] == 1]

    def grading(self, chromosome, ingredients, customers):
        """
        """
        chosen_ingredients = self.get_ingredients_of_chromosome(
            chromosome, ingredients)
        pass

    def cross_over(self, chromosome1, chromosome2, n_points):
        """
        Cross over two chromosomes based on multiple split points.

        Arguments:
            chromosome1 (list[int]): first chromosome.
            chromosome2 (list[int]): second chromosome.

        """
        split_points = [0] + sorted(np.random.choice(
            range(1, chromosome_length),
            size=n_points, replace=False)) + [chromosome_length]

        child1, child2 = [], []
        for index, split_point in enumerate(split_points[1:]):
            if index % 2 == 1:
                child1 += list(chromosome2[split_points[index]: split_point])
                child2 += list(chromosome1[split_points[index]: split_point])
            else:
                child1 += list(chromosome1[split_points[index]: split_point])
                child2 += list(chromosome2[split_points[index]: split_point])

        return child1, child2

    @static_method
    def mutation(chromosome):
        """
        Mutates inplace a chromosome by flipping one value selected at random.

        Arguments:
            chromosome (list[int]): binary array.

        Returns:
            (list[int]): the mutated chromosome.
        """

        mutation_point = np.random.choice(range(len(chromosome)))
        chromosome[mutation_point] = (chromosome[mutation_point] + 1) % 2
        return chromosome




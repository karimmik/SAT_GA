from SAT_Instance import SAT_Instance
from Solution import Solution

import random
import statistics
import math


class SAT_SE_Instance(SAT_Instance):
    def __init__(self):
        self.potential_parents = []
        self.random_generation_pass = False
        self.pop_reborn = False
        self.mutation_chance = 2

        self.mean_limit = 0.15

        self.tournament_size_history = []

        self.champs_list = []
        self.value_evolution = []
        self.mean_list = []
        self.deviation_list = []
        super(SAT_SE_Instance, self).__init__()

    def set_configuration(self,
                          pop_reborn=False,
                          mean_limit=0.2,
                          population_multiple=2,
                          recombination_multiple=4,
                          tournament_size_multiple=1/10):
        self.mean_limit = mean_limit
        self.pop_reborn = pop_reborn
        self.population_multiple = population_multiple
        self.recombination_multiple = recombination_multiple
        self.tournament_size_multiple = tournament_size_multiple

    def __generate_pop(self):
        """
        Generate initial population
        :return: None
        """
        self.population = [Solution(self.var_count) for i in range(self.population_size)]

    def __evaluate(self):
        """
        Evaluate every pop from Population
        :return: None
        """
        for pop in self.population:
            pop.set_value(self.get_solution_value(pop.solution_vector))

    def __tournament_round(self, tournament_size):
        """
        Selection subround
        :param tournament_size: pool size
        :return: round champion
        """
        tournament_pool = random.sample(self.population, k=tournament_size)[:]
        max_index = 0

        for index, elem in enumerate(tournament_pool):
            if elem.value > tournament_pool[max_index].value:
                max_index = index

        return tournament_pool[max_index].copy()

    def __tournament(self):
        """
        Selection of potential parents by tournament
        :return: None
        """
        potential_parents = []

        if self.mean_list[-1] != 0 and abs(
                self.deviation_list[-1] / self.mean_list[-1]) > self.mean_limit and self.tournament_size > 2:
            self.tournament_size = math.floor(self.tournament_size * 0.9)
        # elif self.tournament_size < self.population_size:
        #     self.tournament_size += 1

        while len(potential_parents) < self.population_size:
            potential_parents.append(self.__tournament_round(self.tournament_size))

        self.potential_parents = potential_parents[:]

    def __mortal_combat(self):
        """
        Log the most valuable pop of current population
        :return: None
        """
        max_index = 0

        for index, elem in enumerate(self.population):
            if elem.value > self.population[max_index].value:
                max_index = index

        self.champs_list.append(self.population[max_index].copy())
        self.value_evolution.append(self.population[max_index].value)

    def __mutation(self):
        """
        Do mutation in random Solution and lets hope for new Hulk
        :return: None
        """
        random_index = random.randint(0, len(self.population) - 1)
        self.population[random_index].mutation()
        self.population[random_index].set_value(self.get_solution_value(self.population[random_index].solution_vector))

    def __do_babies(self):
        """
        Get away kids from the screen, 18+
        :return: None
        """
        babies = []
        for i in range(self.recombination_amount):
            # TODO: refactor with random.sample?
            babies.extend(random.choice(self.potential_parents) + random.choice(self.potential_parents))

        # evaluate new kids
        for pop in babies:
            pop.set_value(self.get_solution_value(pop.solution_vector))

        self.potential_parents.clear()
        self.population = self.population[:] + babies[:]

    def __generation_pass(self):
        """
        Restore origin size of Population
        :return: None
        """
        if self.random_generation_pass:
            self.population = random.sample(self.population, k=self.population_size)[:]
        else:
            self.population = sorted(self.population, key=lambda x: x.value)[2 * self.recombination_amount:]

    def __log(self):
        """
        Log some important statistic of current generation
        :return: None
        """
        mean = statistics.mean(pop.value for pop in self.population)
        deviation = statistics.stdev(pop.value for pop in self.population)

        self.mean_list.append(mean)
        self.deviation_list.append(deviation)
        self.tournament_size_history.append(self.tournament_size)

    def print_log(self):
        print("--LOG-------------------")
        print("--CHAMPS----")
        for elem in self.champs_list:
            print(elem.solution_to_string())

        print([elem.value for elem in self.champs_list])

        print("--MEAN-------")
        print(self.mean_list)

        print("--DISP-------")
        print(self.deviation_list)

        print("--TOUR-SIZE--")
        print(self.tournament_size_history)

        print("--BEST-VALUE-")
        print(max(champ.value for champ in self.champs_list))

    def get_best_value(self):
        return max(champ.value for champ in self.champs_list)

    def __replace_the_worst(self):
        """
        Replace the worst possible solutions in population to a random Solution and evaluate it
        :return: None
        """
        for index, pop in enumerate(self.population):
            if pop.value <= -0.95:
                self.population[index] = Solution(self.var_count)
                self.population[index].set_value(self.get_solution_value(self.population[index].solution_vector))

    def run(self):
        # create our Adams and Eves
        self.__generate_pop()
        # evaluate of each Adam adn Eva power
        self.__evaluate()
        # log our first champ of first mortal combat(Come on, J. Cage!)
        self.__mortal_combat()
        # log our history
        self.__log()

        # print(f'----generation: {len(self.deviation_list)}----')
        # for elem in self.population:
        #     print(elem.solution_to_string())

        # until full convergence/degradation of population
        while self.deviation_list[-1] > 0:
            if self.pop_reborn:
                # GET RID OF TROUBLEMAKERS!
                self.__replace_the_worst()
            # LETS THE BATTLE BEGIN!
            self.__tournament()
            # Then God blessed Noah and his sons: “Be fruitful and increase in number and fill the earth."
            self.__do_babies()
            # TEENAGE MUTANT NINJA TURTLES! TEENAGE MUTANT NINJA TURTLES!
            if self.mutation_chance > random.random():
                self.__mutation()
            # IT IS A CIRCLE OF LIVE, SIMBA
            self.__generation_pass()
            # BRING ME A BOOK
            self.__log()

            # print(f'----generation: {len(self.deviation_list)}----')
            # for elem in self.population:
            #     print(elem.solution_to_string())

            # AND ONE OF YOU WILL BECOME A LEGEND
            self.__mortal_combat()

import math


def negation(value):
    return int(math.copysign(1, value) == -1)


class SAT_Instance:
    def __init__(self):
        self.clause = []
        self.weights = []
        self.var_count = 0

        self.population_size = 0
        self.tournament_size = 0
        self.recombination_amount = 0
        self.generations_limit = 100

        self.population_multiple = 2
        self.recombination_multiple = 4
        self.tournament_size_multiple = 1 / 10

    def load_from_file(self, filename):
        parsing_clause = False
        with open(filename) as inputFile:
            for line in inputFile:
                if parsing_clause:
                    if line.startswith("%"):
                        parsing_clause = False
                        continue
                    self.__load_clause(line)

                if not parsing_clause:
                    if (line.startswith("c r") or line.startswith("c    weight generation ")) and self.var_count != 0:
                        parsing_clause = True
                        continue
                    if line.startswith("c"):
                        continue
                    if line.startswith("p"):
                        _, _, var_count, _ = line.split()
                        self.var_count = int(var_count)
                        continue
                    if line.startswith("w"):
                        self.__load_weights(line)
                        continue

        self.population_size = math.ceil(self.var_count * self.population_multiple)
        self.recombination_amount = math.ceil(self.population_size * self.recombination_multiple)
        self.tournament_size = math.ceil(self.population_size * self.tournament_size_multiple)

    def __load_weights(self, weights_string):
        self.weights.extend(
            map(int, weights_string.split()[1:-1])
        )

    def __load_clause(self, clause_string):
        """
        Parse single clause and load into SAT_Instance
        :param clause_string: single clause as String
        :return: None
        """
        clause = []

        for elem in clause_string.split():
            if int(elem) == 0:
                break
            clause.append(int(elem))
        self.clause.append(clause[:])

    def __evaluate_solution(self, is_solution, true_clause_count, solution_vector):
        """
        Return value of solution, relaxation included.
        :param is_solution: True if solution
        :param solution_vector: Configuration vector
        :return: value of solution as Int
        """
        if is_solution:
            value = 0
            for index, elem in enumerate(solution_vector):
                if elem:
                    value = value + self.weights[index]
            return value

        value = -1 * (
                (len(self.clause)-true_clause_count)/len(self.clause)
        )
        return value

    def __test_solution_vector(self, solution_vector):
        """
        Test if solution_vector is the CNF solution
        :param solution_vector: vector of 0 and 1
        :return: 0: not solution, 1: solution, -1: clause is empty; true_clause_count
        """
        true_clause_count = 0
        if not self.clause:
            return 0, 0

        value = 1
        for clause in self.clause:
            clause_value = 0
            if not clause:
                clause_value = 1
            for elem in clause:
                elem_value = solution_vector[abs(elem)-1] ^ negation(elem)  # XOR
                clause_value = clause_value or elem_value
            true_clause_count = true_clause_count + clause_value
            value = value and clause_value

        return value, true_clause_count

    def get_solution_value(self, solution_vector):
        """
        Return value of given solution
        :param solution_vector: configuration vector
        :return: value of solution as Int
        """
        value, true_clause_count = self.__test_solution_vector(solution_vector)
        solution_value = self.__evaluate_solution(
            value,
            true_clause_count,
            solution_vector
        )
        return solution_value

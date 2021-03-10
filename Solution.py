import random


class Solution:
    value = 0

    def __init__(self, solution_length):
        """
        generate a random unevaluated solution of given length

        :param solution_length: length of new generated solution
        """
        self.solution_vector = [random.randint(0, 1) for i in range(solution_length)]

    def mutation(self):
        """
        flip a random bit and re-evaluate solution
        """

        index = random.randint(0, len(self.solution_vector) - 1)
        self.solution_vector[index] = 1 - self.solution_vector[index]

    def solution_to_string(self):
        """
        return a solution_vector as string
        """
        solution_vector_index_format = [index+1 if elem == 1 else -index-1 for index, elem in enumerate(self.solution_vector)]
        return " ".join(map(str, solution_vector_index_format))

    def __add__(self, o):
        """
        solution crossing

        :param o: another solution
        :return: solutions crossing - new_solution
        """
        crossing_index = [random.randint(0, 1) for i in range(len(self.solution_vector))]
        new_solution_vector_1 = []
        new_solution_vector_2 = []
        for i in range(len(self.solution_vector)):
            new_solution_vector_1.append(self.solution_vector[i] if crossing_index[i] else o.solution_vector[i])
            new_solution_vector_2.append(o.solution_vector[i] if crossing_index[i] else self.solution_vector[i])

        new_solution1, new_solution2 = Solution(len(self.solution_vector)), Solution(len(self.solution_vector))
        new_solution1.solution_vector = new_solution_vector_1[:]
        new_solution2.solution_vector = new_solution_vector_2[:]

        return new_solution1, new_solution2

    def set_value(self, new_value):
        self.value = new_value

    def copy(self):
        copy = Solution(len(self.solution_vector))
        copy.value = self.value
        copy.solution_vector = self.solution_vector[:]

        return copy

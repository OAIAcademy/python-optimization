import random

import numpy as np

SIZE = 10
degree2 = np.random.randint(0, 100, size=(SIZE))
degree4 = np.random.randint(0, 100, size=(SIZE))
degree6 = np.random.randint(0, 100, size=(SIZE))


def random_solution():
    return np.random.rand(SIZE) * 100 - 50


def score(solution):
    score = 0
    score += (solution ** 2 * degree2).sum()
    score += (solution ** 2 * degree4).sum()
    score += (solution ** 2 * degree6).sum()
    return score


def mutation(solution):
    ret = np.copy(solution)
    i = random.randint(0, solution.size)
    ret[i] += ret[i] * np.random.normal(0, 0.1)
    return ret

if __name__ == '__main__':
    print(random_solution())
    print(score(random_solution()))
    print(mutation(random_solution()))

import random
import numpy as np
np.random.seed(0)
random.seed(0)

SIZE = 100
CAPACITY = 100

values = np.random.randint(1, 100, size=SIZE)
weight = np.random.randint(1, 10, size=SIZE)

RELAX_COST = 100


def random_solution():
    return np.random.randint(0, 2, size=SIZE)


def score(solution):
    score = (solution * values).sum()
    score -= 0 if (solution * weight).sum() <= CAPACITY else ((solution * weight).sum() - CAPACITY) * RELAX_COST
    return -score


def mutation(solution):
    i = random.randint(0, solution.size-1)
    ret = np.copy(solution)
    ret[i] = (solution[i] + 1) % 2
    return ret


def all_neighbourhood(solution):
    for i in range(0, SIZE):
        ret = np.copy(solution)
        ret[i] = (solution[i] + 1) % 2
        yield ret


if __name__ == '__main__':
    print(random_solution())
    print(score(random_solution()))
    print(mutation(random_solution()))
    print(score(random_solution()))

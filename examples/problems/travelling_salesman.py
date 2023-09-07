import numpy as np
import random

np.random.seed(0)
random.seed(0)
SIZE = 40

graph = np.random.randint(0, 100, size=(SIZE, SIZE))


def random_solution():
    sol = np.zeros(SIZE - 1).astype(int)
    for i in range(0, SIZE - 1):
        sol[i] = i
    np.random.shuffle(sol)
    return sol


def score(solution):
    score = 0
    for i in range(0, SIZE - 2):
        score += graph[solution[i]][solution[i + 1]]
    score += graph[solution[-1]][SIZE - 1]
    score += graph[SIZE - 1][solution[1]]
    return score


def mutation(solution):
    ret = np.copy(solution)
    i, j = np.random.choice(solution.size, 2, replace=False)
    ret[i], ret[j] = solution[j], solution[i]
    return ret


def all_neighbourhood(solution):
    for i in range(0, SIZE - 2):
        for j in range(i + 1, SIZE - 1):
            ret = np.copy(solution)
            ret[i], ret[j] = ret[j], ret[i]
            yield ret


if __name__ == '__main__':
    print(random_solution())
    print(score(random_solution()))
    print(mutation(random_solution()))
    print(len([i for i in all_neighbourhood(random_solution())]))

import random
import numpy as np

np.random.seed(0)
random.seed(0)

DIVISION_NUM = 2
TURN_NUM = 200
PEOPLE_NUM = 5

UNFEASIBILITY_COST = 1


def random_solution():
    ret = np.zeros(TURN_NUM * DIVISION_NUM)
    for turn in range(0, TURN_NUM):
        ret[turn * DIVISION_NUM:(turn + 1) * DIVISION_NUM] = np.random.choice(np.array(range(0, PEOPLE_NUM)),
                                                                              size=DIVISION_NUM, replace=False)
    return ret


def score(solution):
    score = 0

    count = np.zeros(PEOPLE_NUM)
    dist = np.zeros(PEOPLE_NUM)
    rest = np.zeros(PEOPLE_NUM)
    for turn in range(0, TURN_NUM):
        ass = solution[turn * DIVISION_NUM:(turn + 1) * DIVISION_NUM]
        if np.unique(ass).size < DIVISION_NUM:
            score -= UNFEASIBILITY_COST

        for person in range(0, PEOPLE_NUM):
            if np.isin(person, ass):
                count[person] += 1
                dist[person] += rest[person]
                rest[person] = 0
            else:
                rest[person] += 1

    score += (dist / count).sum()

    return -score


def mutation(solution):
    ret = np.copy(solution)
    i, j = np.random.choice(solution.size, 2, replace=False)
    ret[i], ret[j] = solution[j], solution[i]
    return ret


def all_neighbourhood(solution):
    for i in range(0, solution.size - 1):
        for j in range(i + 1, solution.size):
            ret = np.copy(solution)
            ret[i], ret[j] = ret[j], ret[i]
            yield ret


def hybrid(sol1, sol2):
    ret = np.copy(sol1)
    for i in np.random.choice(np.array([i for i in range(0, len(sol1))]), size=random.randint(0, len(sol1)),
                              replace=False):
        ret[i] = sol2[i]
    return ret


if __name__ == '__main__':
    print(random_solution())
    print(score(random_solution()))
    print(mutation(random_solution()))
    print(len([i for i in all_neighbourhood(random_solution())]))

import random

import numpy as np

random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman, polynomial, scheduling


def genetic(random_sol, mutation, hybrid, score, max_time,pop_size=1000, data=None):
    pop = [random_sol() for _ in range(0, pop_size)]
    best = min([(score(i), i) for i in pop], key=lambda x: x[0])[1]
    t = time.time()
    while True:
        if time.time() - t >= max_time:
            break
        fitnesses = np.array([score(i) for i in pop])
        if data is not None:
            data.append((np.copy(fitnesses), pop.copy()))
        fitnesses = -(fitnesses - max(fitnesses))
        fitnesses = fitnesses / fitnesses.sum()
        couples = np.random.choice(np.array([i for i in range(0, len(pop))]), size=len(pop) * 2, p=fitnesses)
        pop = [mutation(hybrid(pop[couples[i]], pop[couples[i + 1]])) for i in range(0, len(couples), 2)]
        pop_score, best_of_pop = min([(score(i), i) for i in pop], key=lambda x: x[0])
        if score(best) > pop_score:
            best = best_of_pop
            yield pop_score, best


if __name__ == '__main__':

    print("Knapsack")

    for score, sol in genetic(knapsack.random_solution, knapsack.mutation, knapsack.hybrid, knapsack.score, max_time=5):
        print(score)

    print("poli")
    for score, sol in genetic(polynomial.random_solution, polynomial.mutation, knapsack.hybrid,
                              polynomial.score, max_time=5):
        print(score)

    print("scheduling")
    for score, sol in genetic(scheduling.random_solution, scheduling.mutation, scheduling.hybrid,
                              scheduling.score, max_time=5):
        print(score)

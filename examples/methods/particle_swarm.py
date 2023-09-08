import random
import numpy as np
random.seed(0)
np.random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman, polynomial, scheduling


def particle_swarm(random_sol, mutation, score, max_time,pop_size=100, data=None):
    T = 100
    sol = [random_sol() for _ in range(0, pop_size)]
    best = sol[0]
    t = time.time()
    while True:
        if data is not None:
            data.append((np.array([score(sol[i]) for i in range(len(sol))]), sol.copy()))
        if time.time() - t >= max_time:
            break
        for part in range(0, len(sol)):
            new_sol = min([(score(i), i) for i in [mutation(sol[part]) for _ in range(len(sol))]], key=lambda x: x[0])[1]
            if score(new_sol) < score(best):
                best = new_sol
                yield score(best), best
            if score(sol[part]) < score(new_sol) or random.randint(0, 100) < T:
                sol[part] = new_sol

        T -= 1
        if T < 0:
            T = 100


if __name__ == '__main__':

    print("Knapsack")

    for score, sol in particle_swarm(knapsack.random_solution, knapsack.mutation, knapsack.score, max_time=5):
        print(score)

    print("salesman")
    for score, sol in particle_swarm(travelling_salesman.random_solution, travelling_salesman.mutation,
                                     travelling_salesman.score, max_time=5):
        print(score)

    print("poli")
    for score, sol in particle_swarm(polynomial.random_solution, polynomial.mutation,
                                     polynomial.score, max_time=5):
        print(score)
    print("scheduling")
    for score, sol in particle_swarm(scheduling.random_solution, scheduling.mutation,
                                     scheduling.score, 3):
        print(score)

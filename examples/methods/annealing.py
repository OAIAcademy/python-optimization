import random

random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman, polynomial, scheduling


def anealing(start, mutation, score, max_time):
    T = 100
    best = start
    sol = start
    t = time.time()
    while True:
        if time.time() - t >= 5:
            break
        new_sol = min([(score(i), i) for i in [mutation(sol) for _ in range(0, 50)]], key=lambda x: x[0])[1]
        if score(new_sol) < score(best):
            best = new_sol
            yield score(best), best
        if score(sol) < score(new_sol) or random.randint(0, 100) < T:
            sol = new_sol

        T -= 1
        if T < 0:
            T = 100


if __name__ == '__main__':

    print("Knapsack")

    for score, sol in anealing(knapsack.random_solution(), knapsack.mutation, knapsack.score, max_time=5):
        print(score)

    print("salesman")
    for score, sol in anealing(travelling_salesman.random_solution(), travelling_salesman.mutation,
                               travelling_salesman.score, max_time=5):
        print(score)

    print("poli")
    for score, sol in anealing(polynomial.random_solution(), polynomial.mutation,
                               polynomial.score, max_time=5):
        print(score)

    print("scheduling")
    for score, sol in anealing(scheduling.random_solution(), scheduling.mutation,
                               scheduling.score, 3):
        print(score)

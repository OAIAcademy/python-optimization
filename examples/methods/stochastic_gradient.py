import random

random.seed(0)

import time

from examples.problems import knapsack, travelling_salesman, polynomial, scheduling


def stochastics_gradient(start, mutation, score):
    best = score(start)
    sol = start
    while True:
        yield score(sol), sol
        sol = min([(score(i), i) for i in [mutation(sol) for _ in range(0, 50)]], key=lambda x: x[0])[1]
        if best < score(sol):
            yield score(sol), sol
            break
        else:
            best = score(sol)


if __name__ == '__main__':

    print("Knapsack")
    t = time.time()
    for score, sol in stochastics_gradient(knapsack.random_solution(), knapsack.mutation, knapsack.score):
        print(score)
        if time.time() - t >= 10:
            break
    print("salesman")
    t = time.time()
    for score, sol in stochastics_gradient(travelling_salesman.random_solution(), travelling_salesman.mutation,
                                           travelling_salesman.score):
        print(score)
        if time.time() - t >= 10:
            break
    print("scheduling")
    t = time.time()
    for score, sol in stochastics_gradient(scheduling.random_solution(), scheduling.mutation,
                                           scheduling.score):
        print(score)
        if time.time() - t >= 10:
            break
    print("Poli")
    for score, sol in stochastics_gradient(polynomial.random_solution(), polynomial.mutation,
                                           polynomial.score):
        print(score)
        if time.time() - t >= 3:
            break
